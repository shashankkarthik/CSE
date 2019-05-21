import re
import string
import symbol_table

DEBUG_MODE = False


class Argument:
    def __init__(self, value):
        self.value = str(value)

    def is_scalar(self):
        return re.fullmatch(r"s[0-9]+", self.value)

    def is_array(self):
        return re.fullmatch(r"a[0-9]+", self.value)

    def is_register(self):
        return re.fullmatch(r"reg.*", self.value)

    def is_constant(self):
        return (not self.is_scalar() and
                not self.is_array() and
                not self.is_register())

    def get_address(self):
        assert self.is_scalar() or self.is_array()
        return int(self.value[1:])

    def __str__(self):
        return self.value


class Instruction:

    ic_commands_attributes = {
        "val_copy": {"load1", "store2"},
        "jump": {"load1"},
        "jump_if_0": {"load1", "load2"},
        "jump_if_n0": {"load1", "load2"},
        "nop": set(),
        "random": {"load1", "store2"},
        "out_val": {"load1"},
        "out_char": {"load1"},
        "ar_get_idx": {"load1", "load2", "store3"},
        "ar_set_idx": {"load1", "load2", "load3"},
        "ar_get_size": {"load1", "store2"},
        "ar_set_size": {"load1", "load2"},
        "ar_copy": {"load1", "store2"},
        "push": {"load1"},
        "pop": {"store1"},
        "ar_push": {"load1"},
        "ar_pop": {"store1"},
        "ar_copy": {"load1", "store2"},
        }
    math_commands = {"add", "sub", "mult", "div",
                     "test_less", "test_gtr", "test_equ",
                     "test_nequ", "test_gte", "test_lte"}
    for math_command in math_commands:
        ic_commands_attributes[math_command] = {
            "load1", "load2", "store3"}

    registers = ["reg" + string.ascii_uppercase[i] for i in range(8)]

    def __init__(self, command=None, arguments=None,
                 label=None, comment=None):
        if arguments:
            assert command

        self.command = command
        if self.command:
            assert self.command in self.ic_commands_attributes
            self.attrs = self.ic_commands_attributes[self.command]
        self.arguments = [Argument(arg) for arg in arguments]
        self.label = label
        self.comment = comment
        self.register_args = []
        for i, arg in enumerate(self.arguments):
            if arg.is_constant():
                new_arg = arg
            else:
                new_arg = Argument(self.registers[i])
            self.register_args.append(new_arg)

    def __str__(self):
        parts = []
        if self.label:
            parts.append("{}:".format(self.label))
        else:
            parts.append("  ")
        if self.command:
            parts.append(self.command)
        if self.arguments:
            for arg in self.arguments:
                parts.append(str(arg))
        if self.comment:
            parts.append("#")
            parts.append(self.comment)
        return " ".join(parts)

    def __repr__(self):
        return str(self)

    def get_tca_lines(self):
        lines = []
        lines.append("### Converting: {}".format(self))
        if self.label:
            lines.append("{}:".format(self.label))
        if not self.command:
            return lines
        if self.command == "ar_push":
            self.command = "push"
        elif self.command == "ar_pop":
            self.command = "pop"
        if re.fullmatch("ar.*", self.command):
            self._array_commands_conversion(lines)
            return lines
        self._load_registers(lines)
        if self.command in {"push", "pop"}:
            self._call_stack_conversion(lines)
        else:
            self._normal_command_conversion(lines)
        self._unload_registers(lines)
        return lines

    def _array_commands_conversion(self, lines):
        assert self.arguments[0].is_array()
        if self.command == "ar_copy":
            source_address = self.arguments[0].get_address()
            assert self.arguments[1].is_array()
            dest_address = self.arguments[1].get_address()

            self._initalize_arrays(lines, source_address)

            copy_start_label, copy_start_line = symbol_table.declare_label(
                prefix="copy_start")
            copy_end_label, copy_end_line = symbol_table.declare_label(
                prefix="copy_end")
            source_ptr = "regA"
            lines.append("load {} {}".format(source_address, source_ptr))
            new_ptr = "regC"
            lines.append("load 0 {}".format(new_ptr))

            lines.append("store {} {}".format(new_ptr, dest_address))

            dest_ptr = "regB"
            lines.append("val_copy {} {}".format(new_ptr, dest_ptr))
            size = "regD"
            lines.append("load {} {}".format(source_ptr, size))
            end_ptr = "regE"
            lines.append("add {} 1 {}".format(new_ptr, end_ptr))
            lines.append("add {0} {1} {0}".format(end_ptr, size))
            lines.append("store {} 0".format(end_ptr))

            lines.append(copy_start_line)
            is_done = "regD"
            lines.append("test_equ {} {} {}".format(new_ptr, end_ptr, is_done))
            lines.append("jump_if_n0 {} {}".format(is_done, copy_end_label))
            lines.append("mem_copy {} {}".format(source_ptr, new_ptr))
            lines.append("add {0} 1 {0}".format(source_ptr))
            lines.append("add {0} 1 {0}".format(new_ptr))
            lines.append("jump {}".format(copy_start_label))
            lines.append(copy_end_line)
            return
        elif self.command == "ar_set_size":
            should_copy_label, should_copy_line = symbol_table.declare_label(
                prefix="should_copy")
            copy_start_label, copy_start_line = symbol_table.declare_label(
                prefix="resize_copy_start")
            copy_end_label, copy_end_line = symbol_table.declare_label(
                prefix="resize_copy_end")

            old_address = self.arguments[0].get_address()
            self._initalize_arrays(lines, old_address)
            old_pointer = "regA"
            lines.append("load {} {}".format(old_address, old_pointer))
            new_size = "regB"
            if self.arguments[1].is_constant():
                new_size = self.arguments[1]
            else:
                lines.append("load {} {}".format(
                    self.arguments[1].get_address(), new_size))

            old_size = "regC"
            lines.append("# Load old array size into {}".format(old_size))
            lines.append("load {} {}".format(old_pointer, old_size))

            is_bigger = "regD"
            lines.append("# {} = new_size > old_size?".format(is_bigger))
            lines.append("test_gtr {} {} {}".format(new_size,
                                                    old_size,
                                                    is_bigger))

            lines.append("# Jump to array copy if new size is bigger.")
            lines.append("jump_if_n0 {} {}".format(is_bigger,
                                                   should_copy_label))

            lines.append("# Otherwise, replace old size w/ new size.  Done.")
            lines.append("store {} {}".format(new_size, old_pointer))
            lines.append("# Skip copying contents.")
            lines.append("jump {}".format(copy_end_label))

            lines.append(should_copy_line)

            new_pointer = "regD"
            lines.append("# Set {} = free mem position".format(new_pointer))
            lines.append("load 0 {}".format(new_pointer))
            lines.append("# Set indirect pointer to new mem pos.")
            lines.append("store {} {}".format(new_pointer, old_address))

            lines.append("# Store new size at new array start")
            lines.append("store {} {}".format(new_size, new_pointer))

            new_free_memory = "regE"
            lines.append("# Set {} = first pos. in new array".format(
                new_free_memory))
            lines.append("add {} 1 {}".format(new_pointer, new_free_memory))
            lines.append("# Add the size of the array to new free memory")
            lines.append("add {0} {1} {0}".format(new_free_memory, new_size))
            lines.append("# Set 0 (free memory) to the new value")
            lines.append("store {} 0".format(new_free_memory))

            lines.append("# Loop to copy old array pointer in {}".format(
                old_pointer))
            lines.append("# To new array pointer in {}".format(new_pointer))
            lines.append("# Copy until old pointer ({}) is at end ({})".format(
                old_pointer, old_size))

            end_index = "regE"
            lines.append("add {} {} {}".format(old_pointer,
                                               old_size,
                                               end_index))
            lines.append(copy_start_line)

            lines.append("# Increment pointer for OLD array and NEW arrays")
            lines.append("add {0} 1 {0}".format(old_pointer))
            lines.append("add {0} 1 {0}".format(new_pointer))

            lines.append("# Check if we are done copying")

            is_done = "regF"
            lines.append("test_gtr {} {} {}".format(old_pointer,
                                                    end_index,
                                                    is_done))
            lines.append("jump_if_n0 {} {}".format(is_done, copy_end_label))

            lines.append("# Do the copy")
            lines.append("mem_copy {} {}".format(old_pointer, new_pointer))
            lines.append("jump {}".format(copy_start_label))
            lines.append(copy_end_line)
            return
        elif self.command == "ar_get_size":
            self._load_registers(lines)
            lines.append("load regA regB")
            self._unload_registers(lines)
            return
        elif self.command == "ar_set_idx":
            self._load_registers(lines)
            lines.append("add regA 1 regD")
            lines.append("add regD {} regD".format(self.register_args[1]))
            lines.append("store {} regD".format(self.register_args[2]))
            self._unload_registers(lines)
            return
        elif self.command == "ar_get_idx":
            self._load_registers(lines)
            lines.append("add regA 1 regD")
            lines.append("add regD regB regD")
            lines.append("load regD regC")
            self._unload_registers(lines)
            return
        raise NotImplementedError("Don't know command {}".format(self.command))

    def _normal_command_conversion(self, lines):
        parts = [self.command]
        for arg, reg in zip(self.arguments, self.register_args):
            if arg.is_constant():
                new_arg = arg
            else:
                new_arg = reg
            parts.append(str(new_arg))
        lines.append(" ".join(parts))

    def _call_stack_conversion(self, lines):
        arg = self.register_args[0]
        if self.command == "push":
            lines.append("store {} regH".format(arg))
            lines.append("add 1 regH regH")
        else:
            lines.append("sub regH 1 regH")
            lines.append("load regH {}".format(arg))

    def _load_registers(self, lines):
        for i, arg in enumerate(self.arguments):
            load_attr = "load{}".format(i + 1)
            if not arg.is_constant() and load_attr in self.attrs:
                address = arg.get_address()
                reg = self.register_args[i]
                lines.append("load {} {}".format(address, reg))

    def _unload_registers(self, lines):
        for i, arg in enumerate(self.arguments):
            store_attr = "store{}".format(i + 1)
            if not arg.is_constant() and store_attr in self.attrs:
                address = arg.get_address()
                reg = self.register_args[i]
                lines.append("store {} {}".format(reg, address))

    def _initalize_arrays(self, lines, address):
        init_end_lab, init_end_line = symbol_table.declare_label(
            prefix="initialize_end")
        lines.append("# Check for uninitialized array at address {}.".format(
            address))
        lines.append("load {} regA".format(address))
        lines.append("jump_if_n0 regA {}".format(init_end_lab))
        lines.append("mem_copy 0 {}".format(address))
        lines.append("load 0 regA".format(address))
        lines.append("add regA 1 regA")
        lines.append("store regA 0")
        lines.append(init_end_line)
        if DEBUG_MODE:
            lines.append("debug_status")


HEAP_START = 20000
CALL_STACK_START = 10000


class Program:
    def __init__(self, ic_instructions=None):
        if ic_instructions is None:
            ic_instructions = []
        self.ic_instructions = ic_instructions

    def add(self, command=None, arguments=None, label=None, comment=None):
        entry = Instruction(command, arguments, label, comment)
        self.ic_instructions.append(entry)

    def convert_to_ac(self, debug=False):
        global DEBUG_MODE
        DEBUG_MODE = debug
        lines = []
        lines.append("store {0} 0 # Start heap at {0}".format(HEAP_START))
        lines.append("val_copy {0} regH # Start Call Stack at {0}".format(
            CALL_STACK_START))
        for ic_instruction in self.ic_instructions:
            lines.extend(ic_instruction.get_tca_lines())
            if DEBUG_MODE:
                lines.append("debug_status")
        return "\n".join(lines) + "\n"

    def __str__(self):
        lines = [str(ic_instruction) for ic_instruction
                 in self.ic_instructions]
        return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print("Running IC")
    icp = Program()
    icp.add(command="add", arguments=["2", "3", "s4"],
            label="start_while", comment="Start")
    print(icp)
