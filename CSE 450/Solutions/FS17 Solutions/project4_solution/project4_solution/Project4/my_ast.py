from . import symbol_table
import itertools


def type_check_entries(table_entry_a, table_entry_b):
    type_a = table_entry_a.expression_type
    type_b = table_entry_b.expression_type
    type_check_types(type_a, type_b)


def type_check_types(type_a, type_b):
    if type_a != type_b:
        err = "Type Mismatch in Assignment ({} != {})".format(type_a, type_b)
        raise TypeError(err)


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

    def generate_ic(self, ic_instructions):
        raise NotImplementedError()


class StatementsNode(Node):

    def __init__(self, children=None):
        if children is None:
            children = []
        super(StatementsNode, self).__init__("Statements", None, children)

    def generate_ic(self, ic_instructions):
        for child in self.children:
            child.generate_ic(ic_instructions)


class RandomNode(Node):

    def __init__(self, children):
        super(RandomNode, self).__init__("Random", "val", children)

    def generate_ic(self, ic_instructions):
        child = self.children[0]
        assert len(self.children) == 1
        child_table_entry = child.generate_ic(ic_instructions)
        result_table_entry = symbol_table.declare_variable(
            self.expression_type)
        type_check_entries(child_table_entry, result_table_entry)
        ic_instructions.append("random {} {}".format(
            child_table_entry, result_table_entry))
        return result_table_entry


class PrintNode(Node):

    def __init__(self, children):
        super(PrintNode, self).__init__("Print", None, children)

    def generate_ic(self, ic_instructions):
        for child in self.children:
            result = child.generate_ic(ic_instructions)
            if result.expression_type == "val":
                print_op = "out_val"
            elif result.expression_type == "char":
                print_op = "out_char"
            else:
                error_message = ("ERROR trying to print " +
                    "illegal expression ({})".format(result.expression_type))
                raise TypeError(error_message)
            ic_instructions.append("{} {}".format(print_op, result))
        ic_instructions.append("out_char '\\n'")


class VariableUsageNode(Node):

    def __init__(self, var_name):
        self.table_entry = symbol_table.get_variable_table_entry(var_name)
        super(VariableUsageNode, self).__init__(
            "VariableUsageNode", self.table_entry.expression_type)

    def __str__(self):
        return "{} {}".format(
            super(VariableUsageNode, self).__str__(),
            self.table_entry.symbol)

    def generate_ic(self, ic_instructions):
        return self.table_entry


class VariableDeclarationNode(Node):

    def __init__(self, var_type, var_name):
        self.table_entry = symbol_table.declare_variable(var_type, var_name)
        super(VariableDeclarationNode, self).__init__(
            "VariableDeclarationNode", var_type)

    def __str__(self):
        return "{} {}".format(
            super(VariableDeclarationNode, self).__str__(),
            self.table_entry.symbol)

    def generate_ic(self, ic_instructions):
        return self.table_entry


class ValLiteralNode(Node):

    def __init__(self, value):
        super(ValLiteralNode, self).__init__("ValLiteral", "val")
        self.value = value

    def __str__(self):
        return super(ValLiteralNode, self).__str__() + " " + self.value

    def generate_ic(self, ic_instructions):
        table_entry = symbol_table.declare_variable(self.expression_type)
        ic_instructions.append(
            "val_copy {} {}".format(self.value, table_entry))
        return table_entry


class CharLiteralNode(Node):

    def __init__(self, value):
        super(CharLiteralNode, self).__init__("CharLiteral", "char")
        self.value = value

    def __str__(self):
        return super(CharLiteralNode, self).__str__() + " " + self.value

    def generate_ic(self, ic_instructions):
        table_entry = symbol_table.declare_variable(self.expression_type)
        ic_instructions.append(
            "val_copy {} {}".format(self.value, table_entry))
        return table_entry


class AssignNode(Node):

    def __init__(self, variable, expression):
        super(AssignNode, self).__init__(
            "Assign", expression.expression_type, [variable, expression])

    def generate_ic(self, ic_instructions):
        variable, expression = self.children
        variable_table_entry = variable.generate_ic(ic_instructions)
        expression_table_entry = expression.generate_ic(ic_instructions)
        type_check_entries(variable_table_entry, expression_table_entry)
        ic_instructions.append("val_copy {} {}".format(
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

    comparisons = {'<', '>', '==', '!=', '>=', '<='}

    def __init__(self, lhs, operator, rhs):
        super(BinaryMathNode, self).__init__("BinaryMath({})".format(operator),
                                             "val", [lhs, rhs])
        self.operator = operator

    def generate_ic(self, ic_instructions):
        instruction = self.operator_to_instruction[self.operator]
        lhs, rhs = self.children
        lhs_table_entry = lhs.generate_ic(ic_instructions)
        rhs_table_entry = rhs.generate_ic(ic_instructions)

        type_check_entries(lhs_table_entry, rhs_table_entry)

        result_table_entry = symbol_table.declare_variable("val")
        if self.operator not in self.comparisons:
            type_check_entries(lhs_table_entry, result_table_entry)

        ic_instructions.append("{} {} {} {}".format(
            instruction,
            lhs_table_entry,
            rhs_table_entry,
            result_table_entry))
        return result_table_entry


class NotNode(Node):

    def __init__(self, child):
        super(NotNode, self).__init__("NotNode({})".format(child),
                                      "val",
                                      [child])

    def generate_ic(self, ic_instructions):
        child = self.children[0]
        child_entry = child.generate_ic(ic_instructions)
        result_table_entry = symbol_table.declare_variable("val")
        ic_instructions.append("test_equ 0 {} {}".format(
            child_entry,
            result_table_entry))
        return result_table_entry


class BooleanNode(Node):

    def __init__(self, lhs, operator, rhs):
        super(BooleanNode, self).__init__("BooleanNode({})".format(operator),
                                          "val", [lhs, rhs])
        self.operator = operator

    def generate_ic(self, ic_instructions):
        result_table_entry = symbol_table.declare_variable("val")

        lhs, rhs = self.children

        lhs_table_entry = lhs.generate_ic(ic_instructions)
        ic_instructions.append("test_nequ 0 {} {}".format(
            lhs_table_entry, result_table_entry))

        jump_label, jump_line = symbol_table.declare_label(
            "BooleanOperator", "Jump Boolean Operator")

        if self.operator == "&&":
            line = "jump_if_0 {} {}".format(result_table_entry, jump_label)

        else:  # self.operator == "||"
            line = "jump_if_n0 {} {}".format(result_table_entry, jump_label)

        ic_instructions.append(line)

        rhs_table_entry = rhs.generate_ic(ic_instructions)
        ic_instructions.append("test_nequ 0 {} {}".format(
            rhs_table_entry, result_table_entry))
        ic_instructions.append(jump_line)
        return result_table_entry


class IfStatementNode(Node):

    def __init__(self, children):
        super(IfStatementNode, self).__init__(
            "IfStatementNode({})".format(children), None, children)

    def generate_ic(self, ic_instructions):
        expression = self.children[0]

        type_check_types(expression.expression_type, "val")

        if_body = self.children[1]
        else_body = self.children[2]

        if_false_label, if_false_line = symbol_table.declare_label(
            "If_False", "If Expression Is False")

        expression_entry = expression.generate_ic(ic_instructions)
        ic_instructions.append("jump_if_0 {} {}".format(
            expression_entry, if_false_label))

        if_body.generate_ic(ic_instructions)

        if_end_label, if_end_line = symbol_table.declare_label(
                "If_End", "End Of If")
        ic_instructions.append("jump {}".format(if_end_label))
        ic_instructions.append(if_false_line)

        else_body.generate_ic(ic_instructions)

        ic_instructions.append(if_end_line)
        return None


class WhileStatementNode(Node):

    def __init__(self, children):
        super(WhileStatementNode, self).__init__(
            "WhileStatementNode({})".format(children), None, children)

    def generate_ic(self, ic_instructions):
        expression = self.children[0]

        type_check_types(expression.expression_type, "val")

        body = self.children[1]

        start_label, start_line = symbol_table.declare_label(
            "While_Start", "While Start")
        ic_instructions.append(start_line)

        expression_entry = expression.generate_ic(ic_instructions)

        end_label, end_line = symbol_table.declare_label(
            "While_End", "While End")
        symbol_table.push_while_label(end_label)

        ic_instructions.append("jump_if_0 {} {}".format(
            expression_entry, end_label))

        body.generate_ic(ic_instructions)

        ic_instructions.append("jump {}".format(start_label))
        ic_instructions.append(end_line)

        symbol_table.pop_while_label()
        return None


class BreakNode(Node):

    def __init__(self):
        super(BreakNode, self).__init__(
            "BreakNode")

    def generate_ic(self, ic_instructions):
        while_label = symbol_table.top_while_label()
        ic_instructions.append("jump {}".format(while_label))
        return None
