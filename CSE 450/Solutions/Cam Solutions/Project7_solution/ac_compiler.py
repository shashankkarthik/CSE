#! /usr/bin/env python3
import sys
import argparse
import my_parser as parser
import my_parser_for_ic as ic_parser
import symbol_table

DEBUG_MODE = False


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("tubular_source_path",
                        help="The path to the Tubular (.tube) file.")
    parser.add_argument("output_path",
                        help="The path to the output file.")
    parser.add_argument("--debug", action='store_true',
                        help="Debug Mode")
    parser.add_argument("-ic", action='store_true',
                        help="Output Intermediate Code")
    return parser.parse_args()


def convert_ic_to_ac(ic):
    if DEBUG_MODE:
        print("IC output")
        print(ic)
        with open("debug_ic.txt", "w") as handle:
            handle.write(ic)
    program = ic_parser.parse(ic, DEBUG_MODE)
    if DEBUG_MODE:
        print("IC Parsed")
        print(program)
    return program.convert_to_ac(DEBUG_MODE)


def compile_to_ic(tree):
    ic_instructions = []
    parse_tree.generate_ic(ic_instructions)
    symbol_table.compile_functions(ic_instructions)
    for i in range(len(ic_instructions)):
        if ':' not in ic_instructions[i]:
            ic_instructions[i] = "  " + ic_instructions[i]
    ic_str = "\n".join(ic_instructions) + "\n"
    return ic_str


if __name__ == "__main__":
    args = get_args()
    if args.debug:
        DEBUG_MODE = True

    parse_tree = parser.parse(args.tubular_source_path, DEBUG_MODE)

    if DEBUG_MODE:
        with open("debug_ast.txt", "w") as handle:
            handle.write(str(parse_tree))
    ic_str = compile_to_ic(parse_tree)
    if args.ic:
        output = ic_str
    else:
        output = convert_ic_to_ac(ic_str)
        if DEBUG_MODE:
            print("AC output")
            print(output)
    with open(args.output_path, "w") as handle:
        handle.write(output)
