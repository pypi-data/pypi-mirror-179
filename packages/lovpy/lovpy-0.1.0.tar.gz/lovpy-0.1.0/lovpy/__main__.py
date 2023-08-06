from sys import argv
from pathlib import Path

from lovpy.runner import run
from lovpy.config import VERSION


def main():
    if len(argv) > 1 and argv[1].endswith(".py"):
        print("-" * 80)
        print(f"Running {argv[1]} under lovpy's verification.")
        print("-" * 80)
        run(Path(argv[1]), *argv[1:])

    elif len(argv) > 1 and (argv[1] == "--train" or argv[1] == "-t"):
        from .models.train_model import train_models

        if len(argv) > 2 and argv[2] == "simple":
            train_models(arch="simple")
        elif len(argv) > 2 and argv[2] == "gnn":
            train_models(arch="gnn")
        else:
            train_models()

    elif len(argv) > 1 and (argv[1] == "--eval" or argv[1] == "-e"):
        if len(argv) > 2 and argv[2] == "examples":
            from .evaluation.evaluate_on_examples import \
                evaluate_proving_methods as eval_on_examples
            eval_on_examples()
        elif len(argv) > 2 and argv[2] == "synthetics":
            from .evaluation.evaluate_on_synthetics import evaluate as eval_on_synthetics
            eval_on_synthetics()

    elif len(argv) > 1 and (argv[1] == "--version" or argv[1] == "-v"):
        print(f"Lovpy version: {VERSION}")

    else:
        print("Usage: python -m lovpy <script.py>|((-t|--train) [simple|gnn])")
        print("")
        print("Arguments:")
        print("\t-t | --train : Trains available all neural architectures. If one of")
        print("\t               the following modifiers are given, trains only selected")
        print("\t               architecture.")
        print("\t\tsimple : Trains only the simple neural architecture.")
        print("\t\tgnn : Trains only the gnn-based neural architecture.")
        print("\t-e | --eval : Evaluates installed proving systems.")
        print("\t\texamples : Evaluation is performed on code snippets.")
        print("\t\tsynthetics : Evaluation is performed on synthetic samples.")
        print("\t-h | --help : Displays this message.")
        print("\t-v | --version : Displays lovpy's version.")


main()
