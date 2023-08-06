import threading
import types
import warnings
import inspect

from lovpy.exceptions import PropertyNotHoldsException
import lovpy.logic.properties as lovpy_properties
from lovpy.logic import prover
from .monitored_predicate import *
from .time_source import global_stamp_and_increment
from ..graphs.dynamic_temporal_graph import EvaluatedDynamicGraph

MONITOR_ONLY_MONITORED_PREDICATES = True
DISABLE_MONITORING_WHEN_PROPERTY_EXCEPTION_RAISED = True
KEEP_TRACK_OF_LAST_VERIFIED_FRAME = True

_SPECIAL_NAMES = [
    '__abs__', '__add__', '__and__', '__call__', '__cmp__', '__coerce__',
    '__contains__', '__delitem__', '__delslice__', '__div__', '__divmod__',
    '__eq__', '__floordiv__', '__ge__', '__getitem__',
    '__getslice__', '__gt__', '__hex__', '__iadd__', '__iand__',
    '__idiv__', '__idivmod__', '__ifloordiv__', '__ilshift__', '__imod__',
    '__imul__', '__invert__', '__ior__', '__ipow__', '__irshift__',
    '__isub__', '__iter__', '__itruediv__', '__ixor__', '__le__',
    '__long__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__',
    '__neg__', '__oct__', '__or__', '__pos__', '__pow__', '__len__',
    '__radd__',
    '__float__', '__int__', '__bool__', '__hash__', '__str__',
    '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__',
    '__reversed__', '__rfloorfiv__', '__rlshift__', '__rmod__',
    '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__',
    '__rtruediv__', '__rxor__', '__setitem__', '__setslice__', '__sub__',
    '__truediv__', '__xor__', '__next__',  # '__repr__',  # comment to not create string errors
]
_PRIMITIVE_CONVERTERS = {'__float__', '__int__', '__bool__', '__str__', '__hash__', '__len__'}

_property_exception_raised = False

__lovpy_past_warnings = set()


class LogipyMethod:
    """Wrapper for every callable object that should be monitored."""

    def __init__(self, method, parent_object=None):
        # Prohibit double wrapping of a callable.
        if isinstance(method, LogipyMethod):
            exception_text = "LogipyMethod cannot call an instance of itself. "
            exception_text += "Consider using lovpy_call function instead."
            raise Exception(exception_text)

        self.__parent_object = parent_object
        self.__method = method  # Wrapped callable object.
        self.__doc__ = method.__doc__
        if hasattr(method, "__name__"):
            self.__name__ = method.__name__
        if hasattr(method, "__module__"):
            self.__module__ = method.__module__

    def __call__(self, globs, locs, *args, **kwargs):
        """Wrapper method for monitoring the calls on a callable object."""
        # A graph to include the state of caller, the state of args and the new steps.
        total_execution_graph = TimedPropertyGraph()

        total_execution_graph = self.__monitor_call__(total_execution_graph, globs, locs)
        total_execution_graph = self.__monitor_called_by__(args, kwargs, total_execution_graph,
                                                           globs, locs)
        return self.__monitor_returned_by__(args, kwargs, total_execution_graph, globs, locs)

    def __get__(self, instance, cls):
        return types.MethodType(self, instance) if instance else self

    def __monitor_call__(self, total_execution_graph, globs, locs):
        """Monitor "call" predicate on parent object."""
        if self.__parent_object is not None and isinstance(self.__parent_object, LogipyPrimitive):
            current_timestamp = Timestamp(global_stamp_and_increment())
            call_predicate = Call(self.__method.__name__)
            if is_predicate_monitored(call_predicate) or not MONITOR_ONLY_MONITORED_PREDICATES:
                call_graph = call_predicate.convert_to_graph()
                call_graph.set_timestamp(current_timestamp)

                # Update the state of parent object and verify it.
                self.__parent_object.__get_lock__().acquire()
                self.__parent_object.get_execution_graph().logical_and(call_graph)
                _verify_object_when_no_exception(self.__parent_object, globs, locs)
                self.__parent_object.__get_lock__().release()

            total_execution_graph.logical_and(self.__parent_object.get_execution_graph())

        return total_execution_graph

    def __monitor_called_by__(self, args, kwargs, total_execution_graph, globs, locs):
        """Monitor "called by" predicate on arguments passed to current call."""
        args_list = list(args)
        args_list.extend(kwargs.values())
        for arg in args_list:
            if isinstance(arg, LogipyPrimitive):
                current_timestamp = Timestamp(global_stamp_and_increment())
                called_by_predicate = CalledBy(self.__method.__name__)
                if (is_predicate_monitored(called_by_predicate)
                        or not MONITOR_ONLY_MONITORED_PREDICATES):
                    # Add the called by predicate to the execution graphs of all arguments.
                    called_by_graph = called_by_predicate.convert_to_graph()
                    called_by_graph.set_timestamp(current_timestamp)

                    arg.__get_lock__().acquire()
                    arg.get_execution_graph().logical_and(called_by_graph)
                    _verify_object_when_no_exception(arg, globs, locs)
                    arg.__get_lock__().release()

                total_execution_graph.logical_and(arg.get_execution_graph())

        return total_execution_graph

    def __monitor_returned_by__(self, args, kwargs, total_execution_graph, globs, locs):
        global _property_exception_raised

        # TODO: FIND THE BEST WAY TO DO THE FOLLOWING
        try:
            ret = self.__method(*args, **kwargs)
        except Exception as err:
            if not isinstance(err, prover.PropertyNotHoldsException):
                # args = [arg.get_lovpy_value() if isinstance(arg, LogipyPrimitive) else arg for arg
                #         in args]
                # kwargs = {key: arg.get_lovpy_value() if isinstance(arg, LogipyPrimitive) else arg
                #           for key, arg in kwargs.items()}
                # ret = self.__method(*args, **kwargs)
                # lovpy_warning(
                #     "A method " + self.__method.__name__ +
                #     " was called a second time at least once by casting away LogipyPrimitive " +
                #     "due to invoking the error: " + str(err))
                raise err
            else:
                _property_exception_raised = True
                raise err

        # TODO: Find a better way to handle predicates from arguments and caller objects.
        ret = LogipyPrimitive(ret, total_execution_graph)

        returned_by_predicate = ReturnedBy(self.__method.__name__)
        current_timestamp = Timestamp(global_stamp_and_increment())
        if is_predicate_monitored(returned_by_predicate) or not MONITOR_ONLY_MONITORED_PREDICATES:
            returned_by_graph = returned_by_predicate.convert_to_graph()
            returned_by_graph.set_timestamp(current_timestamp)

            ret.__get_lock__().acquire()
            ret.get_execution_graph().logical_and(returned_by_graph)
            _verify_object_when_no_exception(ret, globs, locs)
            ret.__get_lock__().release()

        return ret


class LogipyPrimitive:
    """Wrapper for every python object, in order to be monitored by lovpy."""

    __lovpy_id_count = 0  # Counter for each instantiated LogipyPrimitive so far.

    def __init__(self, value, previous_execution_graph=None):
        if isinstance(value, LogipyPrimitive):
            # If given value is already a LogipyPrimitive, copy its execution graph.
            self.__lovpy_value = value.__lovpy_value
            self.__execution_graph = value.get_execution_graph().get_copy()
            self.__timestamp = value.__timestamp
        else:
            # If given value is not a LogipyPrimitive, instantiate a new set of properties.
            self.__lovpy_value = value
            self.__execution_graph = TimedPropertyGraph()
            self.__timestamp = global_stamp_and_increment()

        self.__lock = threading.Lock()  # Lock for performing thread-safe state modifications.

        if previous_execution_graph is not None:
            previous_copy = previous_execution_graph.get_copy()
            previous_copy.logical_and(self.__execution_graph)
            self.__execution_graph = previous_copy

        # Initialize a mapping between all properties to prove and the last frame they found
        # to hold.
        self.__properties_last_proved_frame = dict.fromkeys(
            [(p for p in group.properties) for group in lovpy_properties.get_global_rule_sets()]
        )

        self.__lovpy_id = str(LogipyPrimitive.__lovpy_id_count)
        LogipyPrimitive.__lovpy_id_count += 1  # TODO: Make it thread safe.

    def get_lovpy_id(self):
        return self.__lovpy_id

    def get_lovpy_value(self):
        return self.__lovpy_value

    def get_timestamp(self):
        return self.__timestamp

    def increase_time(self):
        self.__timestamp += 1

    def get_execution_graph(self):
        return self.__execution_graph

    def __get_property_last_proved_frame__(self, prop):
        return self.__properties_last_proved_frame.get(prop, None)

    def __update_property_last_proved_frame__(self, prop, frame):
        self.__properties_last_proved_frame[prop] = frame

    def __getattr__(self, method_name):
        # TODO: Rewrite function with a single exit point.
        # Delegate attribute lookup from wrapper to the wrapped object.
        if hasattr(self.__lovpy_value, method_name):
            if _is_callable(getattr(self.__lovpy_value, method_name)):
                # Wrap callable attributes into a LogipyMethod wrapper.
                return LogipyMethod(getattr(self.__lovpy_value, method_name), self)
            else:
                # Wrap non-callables into a LogipyPrimitive wrapper.
                value = getattr(self.__lovpy_value, method_name)
                if isinstance(value, LogipyPrimitive):
                    return value
                return LogipyPrimitive(value, self.__execution_graph)
        else:
            raise AttributeError()

        # def method(self, *args, **kw):
        #     return LogipyPrimitive(getattr(self.__lovpy_value, method_name)(*args, **kw))
        # return method
        # return object.__getattribute__(self, method_name)

    # def __setattr__(self, key, value):
        # self.__dict__["_LogipyPrimitive__lovpy_value"].__dict__[key] = value
        # self.__dict__[key] = value

    def __get_lock__(self):
        return self.__lock

    def __nonzero__(self):
        return bool(self.value())  # TODO: value() method?????

    # def __hash__(self):
    #     return hash(self.__lovpy_value)

    def __repr__(self) -> str:
        return repr(self.__lovpy_value)


def lovpy_call(globs, locs, method, *args, **kwargs):
    """Call a callable object inside a LogipyMethod wrapper.

    :param globs: Dictionary of available global vars.
    :param locs: Dictionary of available local vars.
    :param method: The callable object to be wrapped and called.
    :param args: Arguments to be passed to the callable object.
    :param kwargs: Keyword arguments to be passed to the callable object.

    # TODO: Better return comment.
    :return: Upon successful verification, returns the value returned
    by the callable.
    """
    if isinstance(method, LogipyMethod):
        return method(globs, locs, *args, **kwargs)
    return LogipyMethod(method)(globs, locs, *args, **kwargs)


def lovpy_value(obj):
    if isinstance(obj, LogipyPrimitive):
        return obj.get_lovpy_value()
    return obj


def error(message):
    raise Exception(message)


def lovpy_warning(lovpy_warning_message):
    if lovpy_warning_message in __lovpy_past_warnings:
        return
    __lovpy_past_warnings.add(lovpy_warning_message)
    warnings.warn(lovpy_warning_message)


def clear_previous_raised_exceptions():
    global _property_exception_raised
    _property_exception_raised = False


def _verify_object_when_no_exception(o: LogipyPrimitive, globs, locs):
    if not _property_exception_raised or not DISABLE_MONITORING_WHEN_PROPERTY_EXCEPTION_RAISED:
        _verify_object(o, globs, locs)


def _verify_object(o: LogipyPrimitive, globs, locs):
    _prove_negative_properties(o, globs, locs)
    if KEEP_TRACK_OF_LAST_VERIFIED_FRAME:
        _prove_positive_properties(o, globs, locs)


def _prove_negative_properties(o: LogipyPrimitive, globs, locs):
    for rule_set in lovpy_properties.get_global_rule_sets():
        # First, evaluate dynamic properties and theorems.
        neg_properties = rule_set.get_evaluated_properties(globs, locs, negatives=True)
        theorems = rule_set.get_evaluated_theorems(globs, locs)

        for p in neg_properties:
            proved, theorems_applied, intermediate_graphs = prover.prove_property(
                o.get_execution_graph(), p, theorems)

            if proved:
                if prover.full_visualization_enabled:
                    prover.visualize_proving_process(intermediate_graphs, theorems_applied, p)
                key = p.dynamic_graph if isinstance(p, EvaluatedDynamicGraph) else p
                positive_property = rule_set.neg_to_pos_property_mapping[key]
                raise PropertyNotHoldsException(
                    p.get_property_textual_representation(),
                    o.__get_property_last_proved_frame__(positive_property)
                )


def _prove_positive_properties(o: LogipyPrimitive, globs, locs):
    for rule_set in lovpy_properties.get_global_rule_sets():
        # First, evaluate dynamic properties and theorems.
        properties = rule_set.get_evaluated_properties(globs, locs)
        theorems = rule_set.get_evaluated_theorems(globs, locs)

        for p in properties:
            proved, _, _ = prover.prove_property(
                o.get_execution_graph(),
                p,
                theorems
            )
            if proved:
                o.__update_property_last_proved_frame__(
                    p.dynamic_graph if isinstance(p, EvaluatedDynamicGraph) else p, inspect.stack())


def _make_primitive_method(method_name):
    def method(self, *args, **kwargs):
        if method_name in _PRIMITIVE_CONVERTERS:
            return getattr(self.get_lovpy_value(), method_name)(*args, **kwargs)
        return LogipyMethod(getattr(self.get_lovpy_value(), method_name), self)(globals(), locals(),
                                                                                *args, **kwargs)

        # _apply_method_rules(method_name, self, call_rules, *args, **kwargs)
        # for arg in args:
        #     graph_logic = graph_logic.union(_properties(arg))
        #     _apply_method_rules(method_name, arg, call_rules, *args, **kwargs)
        # for arg in kwargs.values():
        #     graph_logic = graph_logic.union(_properties(arg))
        #     _apply_method_rules(method_name, arg, call_rules, *args, **kwargs)
        # ret = LogipyPrimitive(getattr(self.lovpy_value(), method_name)(*args, **kwargs),
        #                       graph_logic)
        # _apply_method_rules(method_name, ret, return_rules, *args, **kwargs)
        # return ret
    return method


def _is_callable(obj):
    """Returns true if given object is a callable.

    Provides support for wrapped objects.
    """
    if isinstance(obj, LogipyPrimitive):
        return callable(obj.get_lovpy_value())
    return callable(obj)


for method_name in _SPECIAL_NAMES:
    setattr(LogipyPrimitive, method_name, _make_primitive_method(method_name))

# unbound_variable = LogipyPrimitive(None)
