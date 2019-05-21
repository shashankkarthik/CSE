#! /usr/bin/env python3
import sys

import ply.yacc as yacc
from . import lexer as my_lexer
from .lexer import tokens
from . import my_ast as ast
from . import symbol_table

precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'FLOW_ELSE'),
    ('right', '=', "ASSIGN_ADD", "ASSIGN_SUB", "ASSIGN_MULT", "ASSIGN_DIV"),
    ('left', 'BOOL_OR'),
    ('left', 'BOOL_AND'),
    ('nonassoc', 'COMP_EQU', 'COMP_NEQU',
     'COMP_LESS', 'COMP_LTE', 'COMP_GTR', 'COMP_GTE'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('nonassoc', '!', 'UMINUS')
)


def p_program(p):
    """
    program : statements_or_functions
    """
    p[0] = p[1]


def p_statements_or_functions_empty(p):
    """
    statements_or_functions :
    """
    p[0] = ast.StatementsNode()


def p_statements_or_functions(p):
    """
    statements_or_functions : statements_or_functions statement_or_function
    """
    statements = p[1].children + [p[2]]
    p[0] = ast.StatementsNode(children=statements)


def p_statement_or_function(p):
    """
    statement_or_function : statement
                          | function_definition

    """
    p[0] = p[1]

def p_function_call(p):
    """
    expression : ID '(' empty_or_more_comma_sep_expr ')'
    """
    p[0] = ast.FunctionCallNode(p[1], p[3])

def p_function_definition(p):
    """
    function_definition : DEFINE_KEYWORD type ID new_scope '(' empty_or_more_comma_sep_typed_args ')' statement
    """
    symbol_table.pop_scope()
    p[0] = ast.FunctionDeclarationNode(p[3], p[2], p[6], p[8])


def p_empty_or_more_comma_sep_typed_args(p):
    """
    empty_or_more_comma_sep_typed_args :
    """
    p[0] = []


def p_empty_or_more_comma_sep_typed_args_more(p):
    """
    empty_or_more_comma_sep_typed_args : one_or_more_comma_sep_typed_args
    """
    p[0] = p[1]


def p_one_or_more_comma_sep_typed_args_1(p):
    """
    one_or_more_comma_sep_typed_args : simple_declaration
    """
    p[0] = [p[1]]


def p_one_or_more_comma_sep_typed_args_more(p):
    """
    one_or_more_comma_sep_typed_args : simple_declaration ',' one_or_more_comma_sep_typed_args
    """
    p[0] = [p[1]] + p[3]


def p_return_statement(p):
    """
    return_statement : RETURN_KEYWORD expression
    """
    p[0] = ast.ReturnNode(p[2])


def p_functions_empty(p):
    """
    functions :
    """
    p[0] = ast.StatementsNode()

def p_statements_empty(p):
    """
    statements :
    """
    p[0] = ast.StatementsNode()


def p_statements_nonempty(p):
    """
    statements : statements statement
    """
    statements = p[1].children + [p[2]]
    p[0] = ast.StatementsNode(children=statements)

def p_statement_rules(p):
    """
    statement : expression ';'
              | print_statement ';'
              | declaration ';'
              | block
              | if_statement
              | while_statement
              | return_statement ';'
    """
    p[0] = p[1]


def p_empty_statement(p):
    """
    statement : ';'
    """
    p[0] = ast.StatementsNode()


def p_break(p):
    """
    statement : FLOW_BREAK ';'
    """
    p[0] = ast.BreakNode()




def p_if_statement(p):
    """
    if_statement : FLOW_IF '(' expression ')' statement %prec IFX
    """
    p[0] = ast.IfStatementNode([p[3], p[5], ast.StatementsNode()])


def p_if_else_statement(p):
    """
    if_statement : FLOW_IF '(' expression ')' statement FLOW_ELSE statement
    """
    p[0] = ast.IfStatementNode([p[3], p[5], p[7]])


def p_while_statement(p):
    """
    while_statement : FLOW_WHILE '(' expression ')' statement
    """
    p[0] = ast.WhileStatementNode([p[3], p[5]])


def p_block(p):
    """
    block : '{' new_scope statements '}'
    """
    symbol_table.pop_scope()
    p[0] = p[3]


def p_new_scope(p):
    "new_scope :"
    symbol_table.push_scope()


def p_print_statement(p):
    """
    print_statement : COMMAND_PRINT '(' non_empty_comma_sep_expr ')'
    """
    children = p[3].children
    p[0] = ast.PrintNode(children=children)


def p_comma_sep_expression_0(p):
    """
    empty_or_more_comma_sep_expr :
    """
    p[0] = ast.Node(children=[])


def p_comma_sep_expression_0_or_more(p):
    """
    empty_or_more_comma_sep_expr : non_empty_comma_sep_expr
    """
    p[0] = p[1]

def p_comma_sep_expression_1(p):
    """
    non_empty_comma_sep_expr : expression
    """
    p[0] = ast.Node(children=[p[1]])


def p_comma_sep_expression_many(p):
    """
    non_empty_comma_sep_expr : non_empty_comma_sep_expr ',' expression
    """
    p[1].children.append(p[3])
    p[0] = p[1]


def p_assignment(p):
    """
    expression : var_usage '=' expression
    """
    p[0] = ast.AssignNode(p[1], p[3])


def p_binary_math(p):
    """
    expression : expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
    """
    p[0] = ast.BinaryMathNode(p[1], p[2], p[3])


def p_unary_minus(p):
    """
    expression : '-' expression %prec UMINUS
    """
    negative_one = ast.ValLiteralNode("-1")
    p[0] = ast.BinaryMathNode(negative_one, "*", p[2])


def p_not(p):
    """
    expression : '!' expression
    """
    p[0] = ast.NotNode(p[2])


def p_compound_math(p):
    """
    expression : var_usage ASSIGN_ADD expression
               | var_usage ASSIGN_SUB expression
               | var_usage ASSIGN_DIV expression
               | var_usage ASSIGN_MULT expression
    """
    operator = p[2][0]
    math_node = ast.BinaryMathNode(p[1], operator, p[3])
    p[0] = ast.AssignNode(p[1], math_node)


def p_comparisons(p):
    """
    expression : expression COMP_EQU expression
               | expression COMP_NEQU expression
               | expression COMP_LTE expression
               | expression COMP_LESS expression
               | expression COMP_GTR expression
               | expression COMP_GTE expression
    """
    p[0] = ast.BinaryMathNode(p[1], p[2], p[3])


def p_boolean_operators(p):
    """
    expression : expression BOOL_AND expression
               | expression BOOL_OR expression
    """
    p[0] = ast.BooleanNode(p[1], p[2], p[3])


def p_simple_declaration(p):
    """
    simple_declaration : type ID
    """
    p[0] = ast.VariableDeclarationNode(p[1], p[2])


def p_assign_declaration(p):
    """
    assign_declaration : simple_declaration '=' expression
    """
    p[0] = ast.AssignNode(p[1], p[3])


def p_declaration(p):
    """
    declaration : simple_declaration
                | assign_declaration
    """
    p[0] = p[1]


def p_var_usage(p):
    """
    var_usage : ID
    """
    p[0] = ast.VariableUsageNode(p[1])


def p_value(p):
    """
    expression : var_usage
    """
    p[0] = p[1]


def p_char_literal(p):
    """
    expression : CHAR_LITERAL
    """
    p[0] = ast.CharLiteralNode(p[1])


def p_val_literal(p):
    """
    expression : VAL_LITERAL
    """
    p[0] = ast.ValLiteralNode(p[1])


def p_parentheses(p):
    """
    expression : '(' expression ')'
    """
    p[0] = p[2]


def p_type(p):
    """
    type : TYPE
    """
    p[0] = p[1]


def p_random(p):
    """
    expression : COMMAND_RANDOM '(' expression ')'
    """
    p[0] = ast.RandomNode([p[3]])


def p_array_size(p):
    """
    expression : ID '.' ID '(' ')'
    """
    object_ = p[1]
    method = p[3]
    if method == 'size':
        p[0] = ast.ArraySizeNode(p[1])
    else:
        raise NameError("Unknown method ({})".format(method))

def p_array_resize(p):
    """
    statement : ID '.' ID '(' expression ')'
    """
    object_ = p[1]
    method = p[3]
    expr = p[5]
    if method == 'resize':
        p[0] = ast.ArrayResizeNode(p[1], p[5])
    else:
        raise NameError("Unknown method ({})".format(method))


def p_string_literal(p):
    """
    expression : STRING_LITERAL
    """
    p[0] = ast.StringLiteralNode(p[1])


def p_array_type(p):
    """
    type : ARRAY_KEYWORD '(' TYPE ')'
    """
    p[0] = "array({})".format(p[3])


def p_indexing(p):
    """
    var_usage : ID '[' expression ']'
    """
    p[0] = ast.IndexingNode(p[1], p[3])


def p_string_type(p):
    """
    type : STRING_KEYWORD
    """
    p[0] = "array(char)"


def p_error(p):
    line = 0 if p is None else p.lineno
    error_message = "ERROR(line {}): syntax error {}".format(line, p)
    raise SyntaxError(error_message)


def parse(input_, debug_mode=False):
    if debug_mode:
        parser = yacc.yacc()
    else:
        parser = yacc.yacc(debug=False, errorlog=yacc.NullLogger())
    parse_tree = parser.parse(input_, lexer=my_lexer.lexer_object)
    return parse_tree
