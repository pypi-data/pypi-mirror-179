import re
from pathlib import Path
from typing import List

from lovpy.logic.properties import RuleSet, add_global_rule_set
from lovpy.monitor.monitored_predicate import MonitoredPredicate, add_predicate_to_monitor
from lovpy.graphs.timed_property_graph import *
from lovpy.graphs.timestamps import RelativeTimestamp, LesserThanRelativeTimestamp


class GherkinImporter:
    """A mechanism that converts Gherkin-like rules to temporal graphs."""
    def __init__(self):
        self.import_paths: List[Path] = []

    def add_import_path(self, path: Path) -> 'GherkinImporter':
        """Adds a Gherkin file to the list of files to be imported.

        :param path: Path of the Gherkin file.
        :type path: Path
        :returns: A reference to current instance.
        :rtype: GherkinImporter
        """
        self.import_paths.append(path)
        return self

    def discover(self, root: Path) -> 'GherkinImporter':
        """Automatically finds and adds all Gherkin files under root path.

        Valid Gherkin files are considered the ones ending in `.gherkin`.

        :param root: Root path under which will search for Gherkin files.
        :type root: Path
        :returns: A reference to current instance.
        :rtype: GherkinImporter
        """
        self.import_paths.extend(Path(root).rglob("*.gherkin"))
        return self

    def import_rules(self) -> List[RuleSet]:
        """Imports the rules of all available Gherkin files.

        Gherkin files should have been previously added to the importer by
        using either `add_import_path` or `discover` methods.

        The rules of each file are added to a separate `RulesSet`.

        :returns: Rule sets containing the imported rules.
        :rtype: list[RuleSet]
        """
        repositories: List[RuleSet] = []

        for p in self.import_paths:
            with open(p, "r") as file:
                gherkin = file.read()

            rules: List[TimedPropertyGraph] = convert_gherkin_to_graphs(gherkin)

            # For each file create a new rules repository.
            rules_repo = RuleSet()
            for r in rules:
                rules_repo.add_rule(r.freeze())

            repositories.append(rules_repo)

        return repositories


def import_gherkin_path(root_path=""):
    """Imports the rules from all .gherkin files under root_path."""
    for gherkin_file in Path(root_path).rglob("*.gherkin"):
        if gherkin_file.is_file():
            import_gherkin_file(str(gherkin_file))


def import_gherkin_file(path):
    """Imports the rules of given .gherkin file."""
    if not path.endswith(".gherkin"):
        raise Exception("Can only import .gherkin files: " + path)

    with open(path, "r") as file:
        gherkin = file.read()

    rules = convert_gherkin_to_graphs(gherkin)

    # For each file create a new rules repository.
    rules_repo = RuleSet()
    for r in rules:
        rules_repo.add_rule(r.freeze())
    add_global_rule_set(rules_repo)


def convert_gherkin_to_graphs(gherkin):
    """Converts given gherkin text to a sequence of property graphs."""
    lines = gherkin.split("\n")
    # Remove comment lines.
    lines = [line for line in lines if not line.startswith("#")]
    # Remove preceding and trailing whitespaces.
    lines = [line.strip() for line in lines]
    return convert_gherkin_lines_to_graphs(lines)


def convert_gherkin_lines_to_graphs(lines):
    """Converts given gherkin lines to a sequence of property graphs."""
    graphs = []
    for rule in (" ".join(lines)).split("SCENARIO:"):
        rule = rule.strip()
        if rule:
            graph = convert_specification_to_graph(rule)
            graph.set_property_textual_representation(rule)
            graphs.append(graph)
    return graphs


def convert_specification_to_graph(formula):
    """Converts a specification formula to a specification graph."""
    given_clause, when_clause, then_clause = get_fundamental_clauses(formula)

    when_property = convert_clause_to_graph(when_clause)
    then_property = convert_clause_to_graph(then_clause)

    final_property = when_property
    if given_clause:
        given_property = convert_clause_to_graph(given_clause)
        given_property.set_timestamp(LesserThanRelativeTimestamp(-1))
        final_property.logical_and(given_property)

    final_property.logical_implication(then_property)

    return final_property


def get_fundamental_clauses(formula):
    """Extracts the fundamental step subformulas out of a specification formula."""
    regex = re.compile(
        r"^(GIVEN (?P<given_clause>.*) )?(WHEN (?P<when_clause>.*) )(THEN (?P<then_clause>.*))")

    matches = regex.match(formula).groupdict()
    given_clause = matches['given_clause']
    when_clause = matches['when_clause']
    then_clause = matches['then_clause']

    if when_clause is None or then_clause is None:
        exc_text = "WHEN and THEN clauses are required in specifications syntax.\n"
        exc_text += "The following specifications is invalid:\n"
        exc_text += formula
        raise Exception(exc_text)

    return given_clause, when_clause, then_clause


def convert_clause_to_graph(clause):
    """Converts a fundamental step clause, to property graph.

    A fundamental step clause, is the text that follows GIVEN, WHEN, THEN steps.

    Steps are allowed to contain SHOULD modifier.
    """
    subclauses = clause.split(" AND ")
    clause_graph = TimedPropertyGraph()

    for subclause in subclauses:
        # TODO: Support PRINT statement
        if subclause.startswith("PRINT "):
            continue

        # Remove any SHOULD modifier and parse the predicate part.
        starts_with_should = subclause.startswith("SHOULD ")
        if starts_with_should:
            subclause = subclause.lstrip("SHOULD ")

        # Remove any preceding negation and parse the positive predicate.
        is_negated = subclause.startswith("NOT ")
        if is_negated:
            subclause = subclause.lstrip("NOT ")

        subclause_graph = convert_predicate_to_graph(subclause)

        if starts_with_should:
            # SHOULD modifier means that a predicate should already have been TRUE.
            subclause_graph.set_timestamp(LesserThanRelativeTimestamp(-1))
        else:
            # Without SHOULD modifier, a predicate becomes TRUE at current time step.
            subclause_graph.set_timestamp(RelativeTimestamp(0))

        # If original subclause was negated, negate the total graph of the subclause.
        if is_negated:
            subclause_graph.logical_not()

        clause_graph.logical_and(subclause_graph)

    return clause_graph


def convert_predicate_to_graph(predicate):
    """Converts a predicate to a graph representation."""
    # Check if predicate is a defined function.
    monitored_predicate = MonitoredPredicate.find_text_matching_monitored_predicate(predicate)

    if monitored_predicate is None:
        predicate_graph = PredicateGraph(predicate, MonitoredVariable("VAR"))
    else:
        predicate_graph = monitored_predicate.convert_to_graph()
        add_predicate_to_monitor(monitored_predicate)

    return predicate_graph
