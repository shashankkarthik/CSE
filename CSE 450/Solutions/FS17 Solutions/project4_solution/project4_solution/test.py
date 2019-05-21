#! /usr/bin/env python3
import unittest

class TestCase(unittest.TestCase):
    def test_1(self):
        from Project4.project import generate_bad_code_from_string
        from Project4.bad_interpreter import run_bad_code_from_string

        def test(input_, expected):
          bc = generate_bad_code_from_string(input_)
          print("Generated Bad Code:\n{}".format(bc))
          output = run_bad_code_from_string(bc)
          self.assertEqual(expected, output)

        input_ = """
        # Test some math needs %right to be correct (multiple assignments)
        val a = 6;
        val b = 7;
        a = b = 9;
        print(a, b);
        """
        expected_output = "99\n"
        test(input_, expected_output)

unittest.main()
