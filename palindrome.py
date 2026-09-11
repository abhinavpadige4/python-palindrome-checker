"""Palindrome checker module.

Provides a function to check if a string is a palindrome,
ignoring case and non-alphanumeric characters.
"""


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome.

    A palindrome reads the same forwards and backwards when ignoring
    case and non-alphanumeric characters.

    Args:
        s: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
        Returns False for non-string inputs.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
        >>> is_palindrome("")
        True
        >>> is_palindrome("a")
        True
    """
    # Handle non-string inputs gracefully
    if not isinstance(s, str):
        return False
    
    # Filter to only alphanumeric characters and convert to lowercase
    cleaned = [char.lower() for char in s if char.isalnum()]

    # Check if the cleaned list reads the same forwards and backwards
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    # Quick demo when run directly
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        "a",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon",
        "hello",
        "12321",
        "12345",
    ]

    for test in test_cases:
        result = is_palindrome(test)
        print(f"is_palindrome({test!r}) = {result}")