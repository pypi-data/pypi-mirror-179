import threading
from pathlib import Path
from typing import Dict

import lovpy
from lovpy.exceptions import PropertyNotHoldsException
from lovpy.runner import run

EXAMPLES_DIR: Path = Path(__file__).parent.parent.parent / "examples"
LONGEST_ESTIMATED_SCRIPT_RUNTIME: float = 120.  # 120 seconds


def evaluate_proving_methods():
    valid_script_paths = list(Path(EXAMPLES_DIR).glob("valid_*.py"))
    invalid_script_paths = list(Path(EXAMPLES_DIR).glob("invalid_*.py"))

    print("-" * 64)
    print("Testing {} scripts:".format(len(valid_script_paths)+len(invalid_script_paths)))
    # print("\t-{} scripts are valid.".format(len(valid_script_paths)))
    print("\t- {} scripts contain a bug".format((len(invalid_script_paths))))

    print("-" * 64)
    print("Evaluating deterministic prover.")
    print("-" * 64)
    lovpy.config.set_theorem_selector(lovpy.config.TheoremSelector.DETERMINISTIC)
    evaluate_on_examples(valid_script_paths, invalid_script_paths)

    tensorflow_enabled = True
    try:
        import tensorflow
    except ImportError:
        tensorflow_enabled = False

    if tensorflow_enabled:
        print("-" * 64)
        print("Evaluating fully-connected NN based prover.")
        print("-" * 64)
        lovpy.config.set_theorem_selector(lovpy.config.TheoremSelector.SIMPLE_NN)
        evaluate_on_examples(valid_script_paths, invalid_script_paths)

        print("-" * 64)
        print("Evaluating DGCNN based prover.")
        print("-" * 64)
        lovpy.config.set_theorem_selector(lovpy.config.TheoremSelector.DGCNN)
        evaluate_on_examples(valid_script_paths, invalid_script_paths)

        print("-" * 64)
        print("Evaluating Hybrid prover.")
        print("-" * 64)
        lovpy.config.set_theorem_selector(lovpy.config.TheoremSelector.HYBRID)
        evaluate_on_examples(valid_script_paths, invalid_script_paths)


def evaluate_on_examples(valid_script_paths, invalid_script_paths):
    valid_to_valid = []  # TP
    valid_to_invalid = []  # FP
    invalid_to_valid = []  # FN
    invalid_to_invalid = []  # TN
    # for p in valid_script_paths:
    #     print("\t\tEvaluating {}".format(p))
    #     if evaluate_script(p):
    #         valid_to_valid.append(p)
    #     else:
    #         valid_to_invalid.append(p)
    for p in invalid_script_paths:
        print("\t\tEvaluating {}".format(p))
        if evaluate_script(p, timeout=LONGEST_ESTIMATED_SCRIPT_RUNTIME):
            invalid_to_valid.append(p)
        else:
            invalid_to_invalid.append(p)

    print("-" * 64)
    # print("\t-{} out of {} valid scripts evaluated wrong.".format(
    #     len(valid_to_invalid), len(valid_script_paths)))
    # for fp in valid_to_invalid:
    #     print("\t\t{}".format(str(fp)))
    print("\t- {} out of {} invalid scripts evaluated wrong".format(
        len(invalid_to_valid), len(invalid_script_paths)))
    for fn in invalid_to_valid:
        print("\t\t{}".format(str(fn)))


def evaluate_script(script: Path, timeout: float = None) -> bool:
    # Workaround to escape deadlocks and keep testing, since calls to lock.acquire()
    # cannot be interrupted. Drawback: deadlocked threads are not killed.
    return_dict = {}
    t = threading.Thread(target=run_script, args=(script, return_dict))
    t.daemon = True
    t.start()
    t.join(timeout)
    if not t.is_alive():
        is_valid: bool = return_dict["is_valid"]
    else:
        # Never raised exception on an invalid script, so it was labeled as valid.
        is_valid: bool = True
        print("\t\t\t-->Terminated due to timeout.")

    lovpy.clear_previous_raised_exceptions()

    return is_valid


def run_script(script: Path, return_dict: Dict[str, bool]) -> None:
    return_dict["is_valid"] = True
    try:
        run(script, EXAMPLES_DIR)
    except PropertyNotHoldsException:
        return_dict["is_valid"] = False


if __name__ == "__main__":
    evaluate_proving_methods()
