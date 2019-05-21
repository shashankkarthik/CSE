#! /usr/bin/env python3
import ply.lex as lex
import sys

commands = {
    'val_copy',
    'add',
    'sub',
    'mult',
    'div',
    'test_less',
    'test_gtr',
    'test_equ',
    'test_nequ',
    'test_gte',
    'test_lte',
    'jump',
    'jump_if_0',
    'jump_if_n0',
    'random',
    'out_val',
    'out_char',
    'nop',
    'push',
    'pop',
    'ar_get_idx',
    'ar_set_idx',
    'ar_get_size',
    'ar_set_size',
    'ar_copy',
    'ar_push',
    'ar_pop'
}

tokens = [
    'ID',
    'S_ADDRESS',
    'A_ADDRESS',
    'VAL_LITERAL',
    'CHAR_LITERAL',
    'COMMENT',
    'COMMAND',
    'NEWLINE'
]


def t_NEWLINE(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    return t


def t_S_ADDRESS(t):
    r's[0-9]+'
    return t


def t_A_ADDRESS(t):
    r'a[0-9]+'
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in commands:
        t.type = "COMMAND"
    return t


def t_VAL_LITERAL(t):
    r'-?((\d+)(\.\d+)?)|(\.\d+)'
    return t


def t_CHAR_LITERAL(t):
    r"'([^\\']|\\n|\\t|\\'|\\\\)'"
    return t


def t_WHITESPACE(t):
    r'[ \t]'
    pass


def t_COMMENT(t):
    r'\#[^\n]*'
    t.value = t.value[1:]
    return t

literals = [':']


def t_error(t):
    print("Unknown token on line {}: {}".format(t.lexer.lineno, t.value[0]))
    exit(1)

lexer = lex.lex()

if __name__ == "__main__":
    data = sys.stdin.read()
    lexer.input(data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type in literals:
            print("ASCII_CHAR: {}".format(tok.value))
        else:
            print("{0.type}: {0.value}".format(tok))
    print("Line Count: {}".format(lexer.lineno - 1))
