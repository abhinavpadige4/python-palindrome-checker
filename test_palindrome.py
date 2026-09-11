"""Unit tests for the palindrome checker function."""

import unittest
from palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    """Test cases for the is_palindrome function."""

    def test_simple_palindromes(self):
        """Test simple palindrome strings."""
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("level"))
        self.assertTrue(is_palindrome("madam"))

    def test_simple_non_palindromes(self):
        """Test simple non-palindrome strings."""
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("world"))
        self.assertFalse(is_palindrome("python"))

    def test_mixed_case_palindromes(self):
        """Test palindromes with mixed case."""
        self.assertTrue(is_palindrome("RaceCar"))
        self.assertTrue(is_palindrome("LeVeL"))
        self.assertTrue(is_palindrome("MaDaM"))

    def test_palindromes_with_punctuation(self):
        """Test palindromes containing punctuation."""
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(is_palindrome("No 'x' in Nixon"))
        self.assertTrue(is_palindrome("Madam, I'm Adam"))

    def test_palindromes_with_numbers(self):
        """Test palindromes containing numbers."""
        self.assertTrue(is_palindrome("12321"))
        self.assertTrue(is_palindrome("123454321"))
        self.assertTrue(is_palindrome("1a2b3b2a1"))

    def test_mixed_alphanumeric_palindromes(self):
        """Test mixed alphanumeric palindromes."""
        self.assertTrue(is_palindrome("A1b2B1a"))
        self.assertTrue(is_palindrome("1a2b3c3b2a1"))
        self.assertTrue(is_palindrome("a1b2c3c2b1a"))

    def test_empty_string(self):
        """Test empty string (should be palindrome)."""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """Test single character strings."""
        self.assertTrue(is_palindrome("a"))
        self.assertTrue(is_palindrome("A"))
        self.assertTrue(is_palindrome("1"))
        self.assertTrue(is_palindrome("@"))  # Non-alphanumeric becomes empty

    def test_only_non_alphanumeric(self):
        """Test strings with only non-alphanumeric characters."""
        self.assertTrue(is_palindrome("!@#$%^&*()"))
        self.assertTrue(is_palindrome("   \t\n  "))  # Whitespace
        self.assertTrue(is_palindrome(".,;:!?"))  # Punctuation

    def test_case_insensitive(self):
        """Test that function is case insensitive."""
        self.assertTrue(is_palindrome("Aa"))
        self.assertTrue(is_palindrome("AbBa"))
        self.assertFalse(is_palindrome("Ab"))

    def test_long_palindrome(self):
        """Test a longer palindrome string."""
        long_pal = "A man, a plan, a cat, a ham, a yak, a yam, a hat, a canal-Panama!"
        self.assertTrue(is_palindrome(long_pal))

    def test_invalid_input_types(self):
        """Test behavior with invalid input types."""
        # These should raise TypeError when passed to is_palindrome
        with self.assertRaises(AttributeError):
            is_palindrome(None)
        with self.assertRaises(TypeError):
            is_palindrome(123)
        with self.assertRaises(TypeError):
            is_palindrome([])


if __name__ == "__main__":
    unittest.main()