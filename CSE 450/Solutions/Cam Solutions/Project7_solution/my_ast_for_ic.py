import symbol_table
from sys import exit
import ic


class Node:
    def __init__(self, node_name="Node", children=None):
        self.node_name = node_name
        if children:
            self.children = children
        else:
            self.children = []

    def __str__(self):
        lines = ["{}".format(self.node_name)]

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
        super(StatementsNode, self).__init__("Statements", children)

    def generate_ic(self, ic_instructions):
        for child in self.children:
            child.generate_ic(ic_instructions)


class DroppedLabelNode(Node):
    def __init__(self, label):
        super(DroppedLabelNode, self).__init__("DroppedLabelNode")
        self.label = label

    def __str__(self):
        base = super(DroppedLabelNode, self).__str__()
        return "{} label={}".format(base, self.label)

    def generate_ic(self, ac_instructions):
        ac_instructions.append("{}:".format(self.label))


class ValCopyNode(Node):
    def __init__(self, source, dest):
        super(ValCopyNode, self).__init__("ValCopyNode", [source, dest])

    def generate_ic(self, ac_instructions):
        ac_instructions.append("{}:".format(self.label))


class SAddressNode(Node):
    def __init__(self, address):
        super(SAddressNode, self).__init__("SAddressNode", [address])


class LiteralNode(Node):
    def __init__(self, value):
        super(LiteralNode, self).__init__("LiteralNode", [value])


class BinaryMathNode(Node):
    def __init__(self, children):
        super(BinaryMathNode, self).__init__("BinaryMathNode", children)


class RandomNode(Node):
    def __init__(self, child):
        super(RandomNode, self).__init__("RandomNode", [child])


class JumpNode(Node):
    def __init__(self, label):
        super(JumpNode, self).__init__("JumpNode", [label])


class JumpIfNode(Node):
    def __init__(self, jump_if_true, variable, label):
        super(JumpIfNode, self).__init__("JumpIfNode",
                                         [jump_if_true, variable, label])
