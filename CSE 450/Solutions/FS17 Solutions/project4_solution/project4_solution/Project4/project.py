#! /usr/bin/env python3
import sys
import argparse
from . import my_parser as parser
from . import symbol_table

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action='store_true',
                        help="Debug Mode")
    return parser.parse_args()

def generate_bad_code_from_string(input_, debug_mode=False):
    symbol_table.reset()
    parse_tree = parser.parse(input_, debug_mode)

    if debug_mode:
        with open("debug_ast.txt", "w") as handle:
            handle.write(str(parse_tree))

    ic_instructions = []
    parse_tree.generate_ic(ic_instructions)
    return "\n".join(ic_instructions) + "\n"

if __name__ == "__main__":
    args = get_args()
    if args.debug:
        print("Debug Mode!")

    input_ = sys.stdin.read()

    bc = generate_bad_code_from_string(input_, args.debug)
    print(bc)
