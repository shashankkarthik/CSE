#! /usr/bin/env python3.6
import sys
import ply.lex as lex
import ply.yacc as yacc
import itertools

SYMBOL_TABLE = {}
ALLOCATED_ADDRESSES = 0

reserved = {
    'val': 'TYPE',
    'char': 'TYPE',
    'string': 'TYPE',
    'print': 'COMMAND_PRINT',
    'random': 'COMMAND_RANDOM'
}

tokens = [
    'ID',
    'VAL_LITERAL',
    'CHAR_LITERAL',
    'STRING_LITERAL',
    'ASSIGN_ADD',
    'ASSIGN_SUB',
    'ASSIGN_MULT',
    'ASSIGN_DIV',
    'COMP_EQU',
    'COMP_NEQU',
    'COMP_LESS',
    'COMP_LTE',
    'COMP_GTR',
    'COMP_GTE',
    'BOOL_AND',
    'BOOL_OR',
    ] + list(set(reserved.values()))

precedence = (
    ('right', '=', "ASSIGN_ADD", "ASSIGN_SUB", "ASSIGN_MULT", "ASSIGN_DIV"),
    ('left', 'BOOL_OR'),
    ('left', 'BOOL_AND'),
    ('nonassoc', 'COMP_EQU', 'COMP_NEQU', 'COMP_LESS',
        'COMP_LTE', 'COMP_GTR', 'COMP_GTE'),
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('nonassoc', 'UMINUS')
)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_VAL_LITERAL(t):
    r'((\d+)(\.\d+)?)|(\.\d+)'
    return t


def t_CHAR_LITERAL(t):
    r"'.'"
    return t


def t_STRING_LITERAL(t):
    r'"[^\n"]*"'
    return t


def t_ASSIGN_ADD(t):
    r'\+='
    return t


def t_ASSIGN_SUB(t):
    r'\-='
    return t


def t_ASSIGN_MULT(t):
    r'\*='
    return t


def t_ASSIGN_DIV(t):
    r'/='
    return t


def t_COMP_EQU(t):
    r'=='
    return t


def t_COMP_NEQU(t):
    r'!='
    return t


def t_COMP_LTE(t):
    r'<='
    return t


def t_COMP_GTE(t):
    r'>='
    return t


def t_COMP_LESS(t):
    r'<'
    return t


def t_COMP_GTR(t):
    r'>'
    return t


def t_BOOL_AND(t):
    r'&&'
    return t


def t_BOOL_OR(t):
    r'\|\|'
    return t


literals = '+-*/()=,{}[].;'


def t_WHITESPACE(t):
    r'[ \t]'
    pass


def t_COMMENT(t):
    r'\#[^\n]*'
    pass


def t_error(t):
    err_message = "Unknown token on line {}: {}".format(t.lexer.lineno, t.value[0])
    raise SyntaxError(err_message)


def comment(multiline_str):
    result = []
    for line in multiline_str.splitlines():
        line = "##" + line
        result.append(line)
    return "\n".join(result) + "\n"

class Node:
    def __init__(self, node_name="Node", expression_type=None, children=None):
        self.node_name = node_name
        self.expression_type = expression_type
        if children:
            self.children = children
        else:
            self.children = []

    def __str__(self):
        lines = ["{} type={}".format(self.node_name, self.expression_type)]

        for child in self.children:
            child_str = str(child)
            child_lines = child_str.splitlines()
            for child_line in child_lines:
                lines.append("  " + child_line)
        return "\n".join(lines)

    def generate_bad_code(self, bad_instructions):
        raise NotImplementedError()


class BlockNode(Node):
    def __init__(self, children=None):
        if children is None:
            children = []
        super().__init__("Statements", None, children)

    def generate_bad_code(self, bad_instructions):
        for child in self.children:
            child.generate_bad_code(bad_instructions)


class RandomNode(Node):
    def __init__(self, children):
        super().__init__("Random", "val", children)

    def generate_bad_code(self, bad_instructions):
        bad_instructions.append("# Randoming:\n{}".format(comment(str(self))))
        child = self.children[0]
        child_table_entry = child.generate_bad_code(bad_instructions)
        result_table_entry = declare_variable(
            self.expression_type)
        bad_instructions.append("random {} {}".format(
            child_table_entry, result_table_entry))
        return result_table_entry


class PrintNode(Node):
    def __init__(self, children):
        super().__init__("Print", None, children)

    def generate_bad_code(self, bad_instructions):
        bad_instructions.append("# Printing:\n{}".format(comment(str(self))))
        for child in self.children:
            result = child.generate_bad_code(bad_instructions)
            if result.expression_type == "val":
                print_op = "out_val"
            elif result.expression_type == "char":
                print_op = "out_char"
            else:
                raise SyntaxError("ERROR trying to print illegal expression ({})".format(
                                  result.expression_type))
            bad_instructions.append("{} {}".format(print_op, result))
        bad_instructions.append("out_char '\\n'")


class VariableNode(Node):
    def __init__(self, table_entry):
        self.table_entry = table_entry
        expression_type = table_entry.expression_type
        super().__init__("Variable", expression_type)

    def __str__(self):
        return "{} {}".format(
                super().__str__(),
                self.table_entry.symbol)

    def generate_bad_code(self, bad_instructions):
        return self.table_entry


class LiteralNode(Node):
    def __init__(self, expression_type, value):
        super().__init__("Literal", expression_type)
        self.value = value

    def __str__(self):
        return super().__str__() + " " + self.value

    def generate_bad_code(self, bad_instructions):
        bad_instructions.append("# Literaling:\n{}".format(comment(str(self))))
        table_entry = declare_variable(self.expression_type)
        bad_instructions.append(
            "val_copy {} {}".format(self.value, table_entry))
        return table_entry


class AssignNode(Node):
    def __init__(self, variable, expression):
        super().__init__(
            "Assign", expression.expression_type, [variable, expression])

    def generate_bad_code(self, bad_instructions):
        bad_instructions.append("# Assigning:\n{}".format(comment(str(self))))
        variable, expression = self.children
        variable_table_entry = variable.generate_bad_code(bad_instructions)
        expression_table_entry = expression.generate_bad_code(bad_instructions)
        bad_instructions.append("val_copy {} {}".format(
            expression_table_entry, variable_table_entry))
        return variable_table_entry


class BinaryMathNode(Node):
    operator_to_instruction = {
        '+': "add",
        '-': "sub",
        '*': "mult",
        '/': "div",
        '<': "test_less",
        '>': "test_gtr",
        '==': "test_equ",
        '!=': "test_nequ",
        '>=': "test_gte",
        '<=': "test_lte"
    }

    def __init__(self, lhs, operator, rhs):
        super().__init__("BinaryMath({})".format(operator),
                         "val", [lhs, rhs])
        self.operator = operator

    def generate_bad_code(self, bad_instructions):
        bad_instructions.append("# Mathing:\n{}".format(comment(str(self))))
        instruction = self.operator_to_instruction[self.operator]
        lhs, rhs = self.children
        lhs_table_entry = lhs.generate_bad_code(bad_instructions)
        rhs_table_entry = rhs.generate_bad_code(bad_instructions)
        result_table_entry = declare_variable("val")
        bad_instructions.append("{} {} {} {}".format(
                instruction,
                lhs_table_entry,
                rhs_table_entry,
                result_table_entry))
        return result_table_entry


class BooleanNode(Node):
    def __init__(self, lhs, operator, rhs):
        super().__init__("BooleanNode({})".format(operator),
                         "val", [lhs, rhs])
        self.operator = operator

    def generate_bad_code(self, bad_instructions):
        bad_instructions.append("# Booling:\n{}".format(comment(str(self))))
        lhs, rhs = self.children
        lhs_table_entry = lhs.generate_bad_code(bad_instructions)
        rhs_table_entry = rhs.generate_bad_code(bad_instructions)
        temp_non_zero_lhs = declare_variable("val")
        temp_non_zero_rhs = declare_variable("val")
        bad_instructions.append("test_nequ 0 {} {}".format(
            lhs_table_entry, temp_non_zero_lhs))
        bad_instructions.append("test_nequ 0 {} {}".format(
            rhs_table_entry, temp_non_zero_rhs))
        result_table_entry = declare_variable("val")
        if self.operator == "&&":
            bad_instructions.append("mult {} {} {}".format(
                temp_non_zero_lhs, temp_non_zero_rhs, result_table_entry))
        else:  # self.operator == "||":
            bad_instructions.append("add {} {} {}".format(
                temp_non_zero_lhs, temp_non_zero_rhs, result_table_entry))
            bad_instructions.append("test_nequ 0 {0} {0}".format(
                result_table_entry))
        return result_table_entry


class TableEntry:
    def __init__(self, symbol=None, address=None,
                 address_type="s", expression_type=None):
        self.symbol = symbol
        self.address = address
        self.address_type = address_type
        self.expression_type = expression_type

    def __str__(self):
        return "{}{}".format(self.address_type, self.address)


def declare_variable(expression_type, symbol=None):
    global ALLOCATED_ADDRESSES
    address = ALLOCATED_ADDRESSES
    ALLOCATED_ADDRESSES += 1
    table_entry = TableEntry(symbol, address, "s", expression_type)
    if symbol is not None:
        SYMBOL_TABLE[symbol] = table_entry
    return table_entry


def p_program(p):
    """
    program : statements
    """
    p[0] = p[1]


def p_statements_empty(p):
    """
    statements :
    """
    p[0] = BlockNode()


def p_statements_nonempty(p):
    """
    statements : statements statement
    """
    statements = p[1].children + [p[2]]
    p[0] = BlockNode(children=statements)


def p_statement_rules(p):
    """
    statement : expression ';'
              | print_statement ';'
              | declaration ';'
    """
    p[0] = p[1]


def p_print_statement(p):
    """
    print_statement : COMMAND_PRINT '(' non_empty_comma_sep_expr ')'
    """
    children = p[3].children
    p[0] = PrintNode(children=children)


def p_comma_sep_expression_1(p):
    """
    non_empty_comma_sep_expr : expression
    """
    p[0] = Node(children=[p[1]])


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
    p[0] = AssignNode(p[1], p[3])


def p_binary_math(p):
    """
    expression : expression '+' expression
               | expression '-' expression
               | expression '*' expression
               | expression '/' expression
    """
    p[0] = BinaryMathNode(p[1], p[2], p[3])


def p_unary_minus(p):
    """
    expression : '-' expression %prec UMINUS
    """
    negative_one = LiteralNode("val", "-1")
    p[0] = BinaryMathNode(negative_one, "*", p[2])


def p_compound_math(p):
    """
    expression : var_usage ASSIGN_ADD expression
               | var_usage ASSIGN_SUB expression
               | var_usage ASSIGN_DIV expression
               | var_usage ASSIGN_MULT expression
    """
    operator = p[2][0]
    math_node = BinaryMathNode(p[1], operator, p[3])
    p[0] = AssignNode(p[1], math_node)


def p_comparisons(p):
    """
    expression : expression COMP_EQU expression
               | expression COMP_NEQU expression
               | expression COMP_LTE expression
               | expression COMP_LESS expression
               | expression COMP_GTR expression
               | expression COMP_GTE expression
    """
    p[0] = BinaryMathNode(p[1], p[2], p[3])


def p_boolean_operators(p):
    """
    expression : expression BOOL_AND expression
               | expression BOOL_OR expression
    """
    p[0] = BooleanNode(p[1], p[2], p[3])


def p_simple_declaration(p):
    """
    simple_declaration : type ID
    """
    var_name = p[2]
    if var_name in SYMBOL_TABLE:
        raise NameError("{} is already declared!".format(var_name))
    table_entry = declare_variable(p[1], p[2])
    p[0] = VariableNode(table_entry)


def p_assign_declaration(p):
    """
    assign_declaration : simple_declaration '=' expression
    """
    p[0] = AssignNode(p[1], p[3])


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
    var_name = p[1]
    if var_name not in SYMBOL_TABLE:
        raise NameError("Error: unknown variable '{}'".format(var_name))
    p[0] = VariableNode(SYMBOL_TABLE[p[1]])


def p_value(p):
    """
    expression : CHAR_LITERAL
               | STRING_LITERAL
               | var_usage
    """
    p[0] = p[1]


def p_val_literal(p):
    """
    expression : VAL_LITERAL
    """
    p[0] = LiteralNode("val", p[1])


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
    p[0] = RandomNode([p[3]])


def p_error(p):
    line = 0 if p is None else p.lineno
    error_message = "ERROR(line {}): syntax error".format(line)
    raise SyntaxError(error_message)


def generate_bad_code_from_string(input_):
    global SYMBOL_TABLE
    SYMBOL_TABLE.clear()

    lexer = lex.lex()
    parser = yacc.yacc()
    program = parser.parse(input_, lexer=lexer)

    output = []
    program.generate_bad_code(output)
    return "\n".join(output) + "\n"


if __name__ == "__main__":
    source = sys.stdin.read()
    result = generate_bad_code_from_string(source)
    print(result)
