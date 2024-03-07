import unittest
from io import StringIO
import sys
import Day2_jenkins  # Import the module you want to test

class TestDay2Jenkins(unittest.TestCase):
    def test_output(self):
        captured_output = StringIO()          # Create StringIO object to capture output
        sys.stdout = captured_output          # Redirect stdout to the StringIO object
        Day2_jenkins.main()                   # Call the function from the module
        sys.stdout = sys.__stdout__           # Reset redirect
        self.assertEqual(captured_output.getvalue().strip(), "Hello their!, Welcome to Day2_Jenkins!!!")

if __name__ == '__main__':
    unittest.main()
