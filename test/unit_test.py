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

    @patch('builtins.input', side_effect=['15', 'n', 'n'])  # Min length, alphabetic characters only
    def test_min_length_alphabetic_only(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        password = output.split("Generated Password:")[-1].strip()
        self.assertEqual(len(password), 15)
        self.assertTrue(all(char.isalpha() for char in password), "Password should contain alphabetic characters only.")

    @patch('builtins.input', side_effect=['30', 'y', 'y'])  # Max length, include digits and special chars
    def test_max_length_including_digits_and_special_chars(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        password = output.split("Generated Password:")[-1].strip()
        self.assertEqual(len(password), 30)
        self.assertTrue(any(char.isdigit() for char in password) and any(char in string.punctuation for char in password), "Password should include digits and special characters.")

    @patch('builtins.input', side_effect=['', '15', 'n', 'n'])  # Empty input, then valid length
    def test_empty_input_then_valid_length(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        self.assertNotIn("Invalid input. Password length must be between 15 and 30.", output, "Empty input should be handled gracefully.")

    @patch('builtins.input', side_effect=['-1', '15', 'n', 'n'])  # Negative length input, then valid length
    def test_negative_length_input(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        self.assertIn("Invalid input. Password length must be between 15 and 30.", output, "Negative input should be considered invalid.")

    @patch('builtins.input', side_effect=['100', '15', 'n', 'n'])  # Large length input, then valid length
    def test_extremely_large_length_input(self, mock_input):
        generate_password()
        output = self.capturedOutput.getvalue().strip()
        self.assertIn("Invalid input. Password length must be between 15 and 30.", output, "Extremely large input should be considered invalid.")

if __name__ == '__main__':
    unittest.main()
