# Python Palindrome Checker

A simple yet comprehensive Python function to check if a string is a palindrome, ignoring case and non-alphanumeric characters.

## Features

- ✅ Checks if a string is a palindrome
- ✅ Ignores case (case-insensitive)
- ✅ Ignores non-alphanumeric characters (spaces, punctuation, symbols)
- ✅ Handles empty strings (returns `True`)
- ✅ Handles single characters (returns `True`)
- ✅ Works with numbers and mixed alphanumeric strings
- ✅ Returns `False` for invalid input types (non-strings)
- ✅ Comprehensive unit test suite
- ✅ PEP8 compliant
- ✅ Well documented with examples

## Installation

No installation required! Just copy the `palindrome.py` file into your project.

## Usage

```python
from palindrome import is_palindrome

# Basic usage
print(is_palindrome("racecar"))           # True
print(is_palindrome("hello"))             # False

# Case insensitive
print(is_palindrome("RaceCar"))           # True

# Ignores punctuation and spaces
print(is_palindrome("A man, a plan, a canal: Panama"))  # True
print(is_palindrome("Was it a car or a cat I saw?"))    # True

# Works with numbers
print(is_palindrome("12321"))             # True
print(is_palindrome("1a2b3b2a1"))         # True

# Edge cases
print(is_palindrome(""))                  # True (empty string)
print(is_palindrome("a"))                 # True (single char)
print(is_palindrome("!@#$%"))             # True (only non-alphanumeric)

# Invalid inputs return False
print(is_palindrome(None))                # False
print(is_palindrome(123))                 # False
print(is_palindrome([]))                  # False
```

## Running the Tests

To run the unit test suite:

```bash
python -m unittest test_palindrome.py -v
```

Or simply:

```bash
python test_palindrome.py
```

## Examples

Here are some example palindromes that the function correctly identifies:

- "racecar"
- "A man, a plan, a canal: Panama"
- "No 'x' in Nixon"
- "Was it a car or a cat I saw?"
- "Madam, I'm Adam"
- "12321"
- "1a2b3b2a1"

## Implementation Details

The function works by:

1. **Input validation**: Returns `False` immediately for non-string inputs
2. **Cleaning**: Filters the input string to keep only alphanumeric characters and converts them to lowercase
3. **Comparison**: Checks if the cleaned string reads the same forwards and backwards using Python's slicing (`[::-1]`)

## Time and Space Complexity

- **Time Complexity**: O(n) where n is the length of the input string
- **Space Complexity**: O(n) for the cleaned string storage

## License

This project is open source and available under the MIT License.