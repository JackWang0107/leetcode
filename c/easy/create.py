import os
import argparse
import sys

if __name__ == "__main__":
    assert sys.argv[-1] in ["py", "c"], "Please specify a legal extension"

    path = os.getcwd()
    idx = sys.argv.pop(1)
    sys.argv.insert(1, idx[:-1])
    problem_name = "_".join(sys.argv[1:-1])
    problem_name+= f".{sys.argv[-1]}"

    if os.path.exists(problem_name):
        assert False, f"FileAlready exist: {problem_name}"
    else:
        print(f"Create file: {problem_name}")
        os.system(f"touch {problem_name}")