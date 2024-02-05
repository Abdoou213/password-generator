import string
import sys
import unittest
from unittest.mock import patch
from io import StringIO
from src.generator import generate_password

class TestGeneratePasswordFunction(unittest.TestCase):

    def setUp(self):
        # Redirect stdout to capture print statements
        self.capturedOutput = StringIO()
        sys.stdout = self.capturedOutput

    def tearDown(self):
        # Reset stdout to its original state
        sys.stdout = sys.__stdout__

    @patch('builtins.input', side_effect=['15', 'n', 'n'])  # Default length, no digits, no special chars
    def test_default_length(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        password = output.split("Generated Password:")[-1].strip()
        self.assertTrue(15 <= len(password) <= 30)

    @patch('builtins.input', side_effect=['20', 'n', 'n'])  # Custom length, no digits, no special chars
    def test_custom_length(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        password = output.split("Generated Password:")[-1].strip()
        self.assertEqual(len(password), 20)

    @patch('builtins.input', side_effect=['15', 'y', 'n'])  # Include digits
    def test_include_digits(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        password = output.split("Generated Password:")[-1].strip()
        self.assertTrue(any(char.isdigit() for char in password))

    @patch('builtins.input', side_effect=['25', 'y', 'y'])# Include special chars
    def test_include_special_chars(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        password = output.split("Generated Password:")[-1].strip()
        self.assertTrue(any(char in string.punctuation for char in password))

    @patch('builtins.input', side_effect=['15', 'y', 'y'])  # Include digits and special chars
    def test_include_digits_and_special_chars(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        password = output.split("Generated Password:")[-1].strip()
        self.assertTrue(any(char.isdigit() for char in password) and any(char in string.punctuation for char in password))

    @patch('builtins.input', side_effect=['10', '15', 'n', 'n'])  # First invalid, then valid length
    def test_invalid_length(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        self.assertIn("Invalid input. Password length must be between 15 and 30.", output)

if __name__ == '__main__':
    unittest.main()
