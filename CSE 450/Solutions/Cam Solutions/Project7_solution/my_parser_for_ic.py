#! /usr/bin/env python3
import sys
from sys import exit

import ply.yacc as yacc
import lexer_for_ic
from lexer_for_ic import tokens
import ic


def p_program(p):
    """
    program : entries
    """
    p[0] = ic.Program(p[1])


def p_entries_empty(p):
    """
    entries :
    """
    p[0] = []


def p_entries(p):
    """
    entries : entries entry
    """
    p[0] = p[1] + [p[2]]


def p_entry(p):
    """
    entry : opt_label op_instruction opt_comment NEWLINE
    """
    if p[2]:
        command = p[2][0]
        args = p[2][1]
    else:
        command = None
        args = []
    p[0] = ic.Instruction(label=p[1], command=command,
                          arguments=args, comment=p[3])


def p_instruction(p):
    """
    op_instruction : COMMAND opt_arguments
    """
    p[0] = [p[1], p[2]]


def p_instruction_empty(p):
    """
    op_instruction :
    """


def p_label(p):
    """
    opt_label : ID ':'
    """
    p[0] = p[1]


def p_label_empty(p):
    """
    opt_label :
    """


def p_comment(p):
    """
    opt_comment : COMMENT
    """
    p[0] = p[1]


def p_comment_empty(p):
    """
    opt_comment :
    """


def p_arguments_empty(p):
    """
    opt_arguments :
    """
    p[0] = []


def p_arguments(p):
    """
    opt_arguments : opt_arguments argument
    """
    p[0] = p[1] + [p[2]]


def p_argument(p):
    """
    argument : ID
             | S_ADDRESS
             | A_ADDRESS
             | VAL_LITERAL
             | CHAR_LITERAL
    """
    p[0] = p[1]


def p_error(p):
    line = 0 if p is None else p.lineno
    print("ERROR(line {}): syntax error".format(line))
    print(p)
    sys.exit(1)


def parse(source, debug_mode=False):
    if debug_mode:
        parser = yacc.yacc()
    else:
        parser = yacc.yacc(debug=False, errorlog=yacc.NullLogger())
    parse_tree = parser.parse(source, lexer=lexer_for_ic.lexer)
    return parse_tree
