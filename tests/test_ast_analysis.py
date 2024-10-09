import unittest
from ast_analysis import analyze_file

class TestASTAnalysis(unittest.TestCase):
    def test_identifier_length_violation(self):
        result = analyze_file("tests/code_with_identifier_violation.py")
        self.assertTrue(result["identifier_length_violation"])

    def test_no_identifier_length_violation(self):
        result = analyze_file("tests/code_without_identifier_violation.py")
        self.assertFalse(result["identifier_length_violation"])

    def test_max_nesting_violation(self):
        result = analyze_file("tests/code_with_max_nesting.py")
        self.assertTrue(result["max_control_structure_nesting"] > 4)

    def test_no_max_nesting_violation(self):
        result = analyze_file("tests/code_without_max_nesting.py")
        self.assertTrue(result["max_control_structure_nesting"] <= 4)

if __name__ == "__main__":
    unittest.main()
