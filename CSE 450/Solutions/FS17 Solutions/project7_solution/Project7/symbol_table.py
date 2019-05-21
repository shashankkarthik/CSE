SCALAR_TYPES = {"val", "char"}
ARRAY_TYPES = {"array(val)", "array(char)"}

class SymbolTable:
    def __init__(self):
        self.scope_stack = [{}]
        self.allocated_addresses = 1
        self.label_count = 0
        self.while_label_stack = []
        self.functions = {}
        self.current_function = None
        self.active_entries = None

    def declare_variable(self, expression_type, symbol=None,
                         array=None, index=None):
        address = self.allocated_addresses
        self.allocated_addresses += 1
        if expression_type in SCALAR_TYPES:
            var_letter = "s"
        elif expression_type in ARRAY_TYPES:
            var_letter = "a"
        else:
            message = "expression_type not allowed ({})".format(expression_type)
            raise TypeError(message)
        table_entry = TableEntry(symbol, address, var_letter,
                                 expression_type, array, index)
        if symbol is not None:
            symbol_dict = self.scope_stack[-1]
            if symbol in symbol_dict:
                message = "Symbol ({}) already in symbol table ({})".format(
                    symbol, symbol_dict)
                raise NameError(message)
            symbol_dict[symbol] = table_entry
        if self.active_entries is not None:
            self.active_entries.append(table_entry)
        return table_entry

    def declare_label(self, prefix, comment=None):
        """
        Returns a label and a line with the label
        Example:
        label, line = declare_label("if", "If Label")
        label = "if"
        line = "if_1: # If Label"
        """
        label_num = self.label_count
        self.label_count += 1
        if comment is None:
            comment = ""
        else:
            comment = " # " + comment
        label = "{}_{}".format(prefix, label_num)
        line = "{}:{}".format(label, comment)
        return label, line

    def get_variable_table_entry(self, var_name):
        entry = None
        for symbol_dict in reversed(self.scope_stack):
            if var_name in symbol_dict:
                entry = symbol_dict[var_name]
                break
        if entry is None:
            err = ("Error: unknown variable '{}'; Not in ({})".format(
                var_name, self.scope_stack))
            raise NameError(err)
        return entry

    def push_scope(self):
        self.scope_stack.append({})

    def pop_scope(self):
        self.scope_stack.pop()

    def push_while_label(self, while_label):
        self.while_label_stack.append(while_label)

    def pop_while_label(self):
        return self.while_label_stack.pop()

    def top_while_label(self):
        if len(self.while_label_stack) == 0:
            raise SyntaxError("Break outside of loop")
        return self.while_label_stack[-1]

    def declare_function(self, name, return_type,
                         argument_name_type_pairs, ast_body=None):
        label = "function_{}".format(name)
        return_entry = self.declare_variable(return_type)
        func = FunctionEntry(name,
                             return_type,
                             argument_name_type_pairs,
                             ast_body,
                             label,
                             return_entry)

        self.functions[name] = func
        return func

    def get_function_entry(self, func_name):
        return self.functions[func_name]

    def compile_functions(self, ic_instructions):
        if not self.functions.values():
            return
        ic_instructions += ["",
                            "# Function Definitions:",
                            "jump define_functions_end"]
        for func_entry in self.functions.values():
            self.current_function = func_entry
            ic_instructions.append(func_entry.label + ":")
            self.active_entries = []
            func_entry.ast_body.generate_ic(ic_instructions)
            self.active_entries = None
            ic_instructions.append("")
        ic_instructions.append("define_functions_end:")


class TableEntry:

    def __init__(self, symbol=None, address=None,
                 address_type="s", expression_type=None,
                 array=None, index=None):
        self.symbol = symbol
        self.address = address
        self.address_type = address_type
        self.expression_type = expression_type
        self.array = array
        self.index = index

    def __str__(self):
        return "{}{}".format(self.address_type, self.address)

    __repr__ = __str__


class FunctionEntry:

    def __init__(self, name, return_type,
                 argument_name_type_pairs, ast_body, label, return_entry):
        self.name = name
        self.return_type = return_type
        self.argument_name_type_pairs = argument_name_type_pairs
        self.ast_body = ast_body
        self.label = label
        self.return_entry = return_entry

    def __str__(self):
        return "Function named {}".format(self.name)

    __repr__ = __str__



def declare_variable(expression_type, symbol=None, array=None, index=None):
    return SYMBOL_TABLE.declare_variable(expression_type, symbol, array, index)


def get_variable_table_entry(var_name):
    return SYMBOL_TABLE.get_variable_table_entry(var_name)


def declare_label(prefix, comment=None):
    return SYMBOL_TABLE.declare_label(prefix, comment)


def pop_scope():
    return SYMBOL_TABLE.pop_scope()


def push_scope():
    return SYMBOL_TABLE.push_scope()


def push_while_label(while_label):
    return SYMBOL_TABLE.push_while_label(while_label)


def pop_while_label():
    return SYMBOL_TABLE.pop_while_label()


def top_while_label():
    return SYMBOL_TABLE.top_while_label()


def declare_function(name, return_type,
                     argument_name_type_pairs, ast_body=None):
    return SYMBOL_TABLE.declare_function(name,
                                         return_type,
                                         argument_name_type_pairs, ast_body)


def compile_functions(ic_instructions):
    return SYMBOL_TABLE.compile_functions(ic_instructions)


def get_current_function_entry():
    return SYMBOL_TABLE.current_function


def get_function_entry(func_name):
    return SYMBOL_TABLE.get_function_entry(func_name)

SYMBOL_TABLE = SymbolTable()
ALLOCATED_ADDRESSES = 0
LABEL_COUNT = 0

def reset():
    global SYMBOL_TABLE
    SYMBOL_TABLE = SymbolTable()
    global ALLOCATED_ADDRESSES
    ALLOCATED_ADDRESSES = 0
    global LABEL_COUNT
    LABEL_COUNT = 0
