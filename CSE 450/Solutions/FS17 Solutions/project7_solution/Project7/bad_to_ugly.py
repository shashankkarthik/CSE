import re
import string
from . import symbol_table

DEBUG_MODE = True
HEAP_START = 10000
CALL_STACK_START = 20000

MATH_COMMANDS = {"add", "sub", "mult", "div",
                 "test_less", "test_gtr", "test_equ",
                 "test_nequ", "test_gte", "test_lte"}

def convert_bad_line_to_ugly_lines(bad_line):

    def get_parts_of_line(line):
        def check_for_space(args):
            for i, arg in enumerate(args):
                if arg == "'" and args[i + 1] == "'":
                    args[i] = "' '"
                    del args[i + 1]
                    return True
            return False

        def remove_comments(parts):
            found_index = None
            for i, part in enumerate(parts):
                if part[0] == '#':
                    found_index = i
                    break
            if found_index is not None:
                return parts[:i]
            return parts

        def break_colon_off(parts):
            for part in parts:
                if part[-1] == ":":
                    assert len(parts) == 1
                    return [part[:-1], ':']
            return parts
        parts = bad_line.split()
        parts = remove_comments(parts)
        while(check_for_space(parts)):
            pass
        parts = break_colon_off(parts)
        return parts

    def check_reg_str(reg_str):
        assert reg_str[:3] == "reg"
        assert reg_str[3] in "ABCDEFGH"
        assert len(reg_str) == 4

    def load_reg(reg, value_str):
        check_reg_str(reg)
        if (value_str[0] == 's' or value_str[0] == 'a') and (value_str[1:]).isdigit():
            return ["load {} {}".format(value_str[1:], reg)]
        else:
            return ["val_copy {} {}".format(value_str, reg)]

    def store_reg(reg, value_str):
        check_reg_str(reg)
        assert value_str[0] == 's' or value_str[0] == 'a'
        return ["store {} {}".format(reg, value_str[1:])]

    def initalize_array(address):
        lines = []
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
        return lines

    ugly_lines = []

    parts = get_parts_of_line(bad_line)
    if not parts:
        return ugly_lines
    if len(parts) == 1:
        assert parts[0] == "nop"
        return parts

    command, *args = parts

    if command[0] == "#":
        return ugly_lines
    if command == "val_copy":
        assert len(args) == 2
        source = args[0]
        dest = args[1]

        ugly_lines += load_reg("regA", source)
        ugly_lines.append("val_copy regA regB")
        ugly_lines += store_reg("regB", dest)
        return ugly_lines
    if command == "out_char":
        assert len(args) == 1
        ugly_lines += load_reg("regA", args[0])
        ugly_lines += ["out_char regA"]
        return ugly_lines
    if command == "out_val":
        assert len(args) == 1
        ugly_lines += load_reg("regA", args[0])
        ugly_lines += ["out_val regA"]
        return ugly_lines
    if command in MATH_COMMANDS:
        assert len(args) == 3
        ugly_lines += load_reg("regA", args[0])
        ugly_lines += load_reg("regB", args[1])
        ugly_lines += ["{} regA regB regC".format(command)]
        ugly_lines += store_reg("regC", args[2])
        return ugly_lines
    if args[0] == ":":
        assert len(args) == 1
        ugly_lines += [command + ":"]
        return ugly_lines
    if command == "jump":
        assert len(args) == 1
        ugly_lines += load_reg("regA", args[0])
        ugly_lines +=  ["jump regA"]
        return ugly_lines
    if command == "jump_if_0" or command == "jump_if_n0":
        assert len(args) == 2
        ugly_lines += load_reg("regA", args[0])
        ugly_lines += load_reg("regB", args[1])
        ugly_lines +=  [f"{command} regA regB"]
        return ugly_lines
    if command == "random":
        assert len(args) == 2
        ugly_lines += load_reg("regA", args[0])
        ugly_lines += [f"{command} regA regB"]
        ugly_lines += store_reg("regB", args[1])
        return ugly_lines
    if command == "ar_copy":
        assert len(args) == 2
        source_array_var = args[0]
        dest_array_var = args[1]
        assert source_array_var[0] == 'a'
        assert dest_array_var[0] == 'a'

        source_address = source_array_var[1:]
        dest_address = dest_array_var[1:]

        ugly_lines += initalize_array(source_address)

        copy_start_label, copy_start_line = symbol_table.declare_label(
            prefix="copy_start")
        copy_end_label, copy_end_line = symbol_table.declare_label(
            prefix="copy_end")
        source_ptr = "regA"
        ugly_lines.append("load {} {}".format(source_address, source_ptr))
        new_ptr = "regC"
        ugly_lines.append("load 0 {}".format(new_ptr))

        ugly_lines.append("store {} {}".format(new_ptr, dest_address))

        dest_ptr = "regB"
        ugly_lines.append("val_copy {} {}".format(new_ptr, dest_ptr))
        size = "regD"
        ugly_lines.append("load {} {}".format(source_ptr, size))
        end_ptr = "regE"
        ugly_lines.append("add {} 1 {}".format(new_ptr, end_ptr))
        ugly_lines.append("add {0} {1} {0}".format(end_ptr, size))
        ugly_lines.append("store {} 0".format(end_ptr))

        ugly_lines.append(copy_start_line)
        is_done = "regD"
        ugly_lines.append("test_equ {} {} {}".format(new_ptr, end_ptr, is_done))
        ugly_lines.append("jump_if_n0 {} {}".format(is_done, copy_end_label))
        ugly_lines.append("mem_copy {} {}".format(source_ptr, new_ptr))
        ugly_lines.append("add {0} 1 {0}".format(source_ptr))
        ugly_lines.append("add {0} 1 {0}".format(new_ptr))
        ugly_lines.append("jump {}".format(copy_start_label))
        ugly_lines.append(copy_end_line)
        return ugly_lines
    elif command == "ar_set_size":
        assert len(args) == 2
        array_var = args[0]
        assert array_var[0] == 'a'

        should_copy_label, should_copy_line = symbol_table.declare_label(
            prefix="should_copy")
        copy_start_label, copy_start_line = symbol_table.declare_label(
            prefix="resize_copy_start")
        copy_end_label, copy_end_line = symbol_table.declare_label(
            prefix="resize_copy_end")

        old_address = array_var[1:]

        ugly_lines += initalize_array(old_address)
        old_pointer = "regA"
        ugly_lines.append("load {} {}".format(old_address, old_pointer))
        new_size = "regB"
        ugly_lines += load_reg(new_size, args[1])

        old_size = "regC"
        ugly_lines.append("# Load old array size into {}".format(old_size))
        ugly_lines.append("load {} {}".format(old_pointer, old_size))

        is_bigger = "regD"
        ugly_lines.append("# {} = new_size > old_size?".format(is_bigger))
        ugly_lines.append("test_gtr {} {} {}".format(new_size,
                                                    old_size,
                                                    is_bigger))

        ugly_lines.append("# Jump to array copy if new size is bigger.")
        ugly_lines.append("jump_if_n0 {} {}".format(is_bigger,
                                                    should_copy_label))

        ugly_lines.append("# Otherwise, replace old size w/ new size.  Done.")
        ugly_lines.append("store {} {}".format(new_size, old_pointer))
        ugly_lines.append("# Skip copying contents.")
        ugly_lines.append("jump {}".format(copy_end_label))

        ugly_lines.append(should_copy_line)

        new_pointer = "regD"
        ugly_lines.append("# Set {} = free mem position".format(new_pointer))
        ugly_lines.append("load 0 {}".format(new_pointer))
        ugly_lines.append("# Set indirect pointer to new mem pos.")
        ugly_lines.append("store {} {}".format(new_pointer, old_address))

        ugly_lines.append("# Store new size at new array start")
        ugly_lines.append("store {} {}".format(new_size, new_pointer))

        new_free_memory = "regE"
        ugly_lines.append("# Set {} = first pos. in new array".format(
                          new_free_memory))
        ugly_lines.append("add {} 1 {}".format(new_pointer, new_free_memory))
        ugly_lines.append("# Add the size of the array to new free memory")
        ugly_lines.append("add {0} {1} {0}".format(new_free_memory, new_size))
        ugly_lines.append("# Set 0 (free memory) to the new value")
        ugly_lines.append("store {} 0".format(new_free_memory))

        ugly_lines.append("# Loop to copy old array pointer in {}".format(
                          old_pointer))
        ugly_lines.append("# To new array pointer in {}".format(new_pointer))
        ugly_lines.append("# Copy until old pointer ({}) is at end ({})".format(
                          old_pointer, old_size))

        end_index = "regE"
        ugly_lines.append("add {} {} {}".format(old_pointer,
                                                old_size,
                                                    end_index))
        ugly_lines.append(copy_start_line)

        ugly_lines.append("# Increment pointer for OLD array and NEW arrays")
        ugly_lines.append("add {0} 1 {0}".format(old_pointer))
        ugly_lines.append("add {0} 1 {0}".format(new_pointer))

        ugly_lines.append("# Check if we are done copying")

        is_done = "regF"
        ugly_lines.append("test_gtr {} {} {}".format(old_pointer,
                                                     end_index,
                                                     is_done))
        ugly_lines.append("jump_if_n0 {} {}".format(is_done, copy_end_label))

        ugly_lines.append("# Do the copy")
        ugly_lines.append("mem_copy {} {}".format(old_pointer, new_pointer))
        ugly_lines.append("jump {}".format(copy_start_label))
        ugly_lines.append(copy_end_line)
        return ugly_lines
    elif command == "ar_get_size":
        assert len(args) == 2
        array_var = args[0]
        assert array_var[0] == 'a'

        address = array_var[1:]
        ugly_lines += load_reg("regA", array_var)
        ugly_lines += ["load regA regB"]
        ugly_lines += store_reg("regB", args[1])
        return ugly_lines
    elif command == "ar_set_idx":
        assert len(args) == 3
        array_var, index_var, value_var = args
        assert array_var[0] == 'a'

        ugly_lines += load_reg("regA", array_var)
        ugly_lines += load_reg("regB", index_var)
        ugly_lines += load_reg("regC", value_var)

        ugly_lines += ["add regA 1 regD",
                       "add regD regB regD",
                       "store regC regD"]
        return ugly_lines
    elif command == "ar_get_idx":
        assert len(args) == 3
        array_var, index_var, value_var = args
        assert array_var[0] == 'a'

        ugly_lines += load_reg("regA", array_var)
        ugly_lines += load_reg("regB", index_var)

        ugly_lines += ["add regA 1 regD",
                       "add regD regB regD",
                       "load regD regC"]

        ugly_lines += store_reg("regC", value_var)
        return ugly_lines
    elif command == "push" or command == "ar_push":
        assert len(args) == 1
        value_var = args[0]
        ugly_lines += load_reg("regA", value_var)
        ugly_lines += ["store regA regH",
                       "add 1 regH regH"]
        return ugly_lines
    elif command == "pop" or command == "ar_pop":
        assert len(args) == 1
        dest_var = args[0]
        ugly_lines += ["sub regH 1 regH",
                       "load regH regA"]
        ugly_lines += store_reg("regA", dest_var)
        return ugly_lines

    raise NotImplementedError(f"Unknown command: {command}")

def convert_bad_str_to_ugly_str(bad_str):
    ugly_lines = [f"store {HEAP_START} 0 # Start heap at {HEAP_START}",
                  f"val_copy {CALL_STACK_START} regH # Start Call Stack at {CALL_STACK_START}"]
    for bad_line in bad_str.splitlines():
        ugly_lines.append("# " + bad_line)
        ugly_lines += convert_bad_line_to_ugly_lines(bad_line)
        ugly_lines.append("")
    return "\n".join(ugly_lines) + "\n"
