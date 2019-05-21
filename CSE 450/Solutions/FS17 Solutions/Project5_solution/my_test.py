#! /usr/bin/env python3
import unittest

class TestCase(unittest.TestCase):
    def test_1(self):
        from Project5.project import generate_bad_code_from_string
        from Project5.bad_interpreter import run_bad_code_from_string

        def test(input_, expected):
          bc = generate_bad_code_from_string(input_)
          print("Generated Bad Code:\n{}".format(bc))
          output = run_bad_code_from_string(bc)
          self.assertEqual(expected, output)

        test("""
# Access an array value.

string msg = "Did we generate proper output?";
print(msg[7], msg[18], msg[23], msg[2], '!');
        """, "Test Message!\n")


unittest.main()
