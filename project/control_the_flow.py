# Objective: Build number crunching utilities to master Python's control flow and operators
# - Use logical operators (not, and, or) with short-circuit evaluation
# - Use equality (==, !=) and identity (is, is not) operators appropriately
# - Use comparison operators and chained comparisons
# - Use arithmetic operators including integer division and modulo
# - Use conditionals (if/elif/else) to classify and categorize numbers
# - Use for loops to iterate through ranges and sequences
# - Use while loops for condition-based iteration
# - Use break to exit loops early and continue to skip iterations
# - Use list, set, and dict comprehensions to create collections concisely


# =============================================================================
# SECTION 1: Logical Operators (not, and, or)
# =============================================================================

def negate(value):
    """
    Return the logical negation of a value.
    
    Args:
        value: Any value that can be evaluated as boolean
    
    Returns:
        True if value is falsy, False if value is truthy
    """
    pass


def both_true(a, b):
    """
    Check if both values are truthy.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if both a and b are truthy, False otherwise
    """
    pass


def either_true(a, b):
    """
    Check if at least one value is truthy.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if a or b (or both) are truthy, False otherwise
    """
    pass


def is_empty(container):
    """
    Check if a container (list, string, dict, etc.) is empty.
    
    Args:
        container: A container to check
    
    Returns:
        True if empty, False if it has elements
    """
    pass


def first_truthy(a, b, default):
    """
    Return the first truthy value among a and b, or default if both are falsy.
    This demonstrates short-circuit evaluation of 'or'.
    
    Args:
        a: First value to check
        b: Second value to check
        default: Default value if both are falsy
    
    Returns:
        First truthy value, or default
    """
    pass


# =============================================================================
# SECTION 2: Equality and Identity Operators
# =============================================================================

def are_same_object(a, b):
    """
    Check if a and b refer to the exact same object in memory.
    
    Args:
        a: First object
        b: Second object
    
    Returns:
        True if same object (same id), False otherwise
    """
    pass


def are_different_objects(a, b):
    """
    Check if a and b are different objects in memory.
    
    Args:
        a: First object
        b: Second object
    
    Returns:
        True if different objects, False if same object
    """
    pass


def are_equal(a, b):
    """
    Check if a and b have equal values.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if values are equal, False otherwise
    """
    pass


def are_not_equal(a, b):
    """
    Check if a and b have different values.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if values are different, False otherwise
    """
    pass


# =============================================================================
# SECTION 3: Comparison Operators
# =============================================================================

def compare_values(a, b):
    """
    Compare two values and return their relationship.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        "less" if a < b, "equal" if a == b, "greater" if a > b
    """
    pass


def is_in_range(value, low, high):
    """
    Check if value is within the range [low, high] inclusive.
    Use chained comparison for elegance.
    
    Args:
        value: Value to check
        low: Lower bound (inclusive)
        high: Upper bound (inclusive)
    
    Returns:
        True if low <= value <= high, False otherwise
    """
    pass


def find_max_of_three(a, b, c):
    """
    Find the maximum of three values.
    
    Args:
        a: First value
        b: Second value
        c: Third value
    
    Returns:
        The largest value
    """
    pass


def clamp(value, minimum, maximum):
    """
    Clamp a value to be within [minimum, maximum] range.
    
    Args:
        value: Value to clamp
        minimum: Minimum allowed value
        maximum: Maximum allowed value
    
    Returns:
        value if in range, minimum if too low, maximum if too high
    """
    pass


# =============================================================================
# SECTION 4: Arithmetic Operators
# =============================================================================

def integer_divide(a, b):
    """
    Perform integer (floor) division.
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Floor of a divided by b
    """
    pass


def get_remainder(a, b):
    """
    Get the remainder of division (modulo).
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Remainder of a divided by b
    """
    pass


def divmod_result(a, b):
    """
    Return both quotient and remainder of division.
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Tuple (quotient, remainder) using integer division
    """
    pass


def is_divisible(a, b):
    """
    Check if a is evenly divisible by b.
    
    Args:
        a: Number to check
        b: Potential divisor
    
    Returns:
        True if a is divisible by b, False otherwise
    """
    pass


# =============================================================================
# SECTION 5: Conditionals (if/elif/else)
# =============================================================================

def classify_number(n):
    """
    Classify a number as positive, negative, or zero.
    
    Args:
        n: A number to classify
    
    Returns:
        "positive", "negative", or "zero"
    """
    pass


def get_number_type(n):
    """
    Determine if a number is even or odd.
    
    Args:
        n: An integer
    
    Returns:
        "even" or "odd"
    """
    pass


def assign_grade(score):
    """
    Assign a letter grade based on score.
    
    Score ranges:
        90-100: "A"
        80-89: "B"
        70-79: "C"
        60-69: "D"
        Below 60: "F"
    
    Args:
        score: Numeric score (0-100)
    
    Returns:
        Letter grade as string
    """
    pass


# =============================================================================
# SECTION 6: For Loops
# =============================================================================

def sum_of_range(n):
    """
    Calculate the sum of integers from 1 to n (inclusive).
    
    Args:
        n: Upper bound (positive integer)
    
    Returns:
        Sum of 1 + 2 + 3 + ... + n
    """
    pass


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in the text.
    Case-insensitive.
    
    Args:
        text: A string to analyze
    
    Returns:
        Count of vowels
    """
    pass


def find_factors(n):
    """
    Find all factors of n (numbers that divide n evenly).
    
    Args:
        n: A positive integer
    
    Returns:
        List of factors in ascending order
    """
    pass


# =============================================================================
# SECTION 7: While Loops
# =============================================================================

def countdown(start):
    """
    Create a countdown list from start down to 1.
    
    Args:
        start: Starting number (positive integer)
    
    Returns:
        List like [start, start-1, ..., 2, 1]
    """
    pass


def sum_until_negative(numbers):
    """
    Sum numbers from the list until a negative number is encountered.
    The negative number is NOT included in the sum.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Sum of numbers before the first negative (or sum of all if no negatives)
    """
    pass


def find_first_multiple(n, minimum):
    """
    Find the smallest multiple of n that is >= minimum.
    
    Args:
        n: The number to find multiples of
        minimum: The minimum value the multiple must be
    
    Returns:
        Smallest multiple of n that is >= minimum
    """
    pass


# =============================================================================
# SECTION 8: Break and Continue
# =============================================================================

def find_first_negative(numbers):
    """
    Find the first negative number in the list.
    
    Args:
        numbers: List of numbers
    
    Returns:
        First negative number, or None if no negatives exist
    """
    pass


def sum_positive_only(numbers):
    """
    Sum only the positive numbers in the list, skipping negatives and zero.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Sum of positive numbers only
    """
    pass


def is_prime(n):
    """
    Check if n is a prime number.
    A prime is only divisible by 1 and itself.
    
    Args:
        n: A positive integer >= 2
    
    Returns:
        True if prime, False otherwise
    """
    pass


def find_index_of(items, target):
    """
    Find the index of target in items list.
    
    Args:
        items: List to search
        target: Value to find
    
    Returns:
        Index of target, or -1 if not found
    """
    pass


# =============================================================================
# SECTION 9: List Comprehension
# =============================================================================

def squares_up_to(n):
    """
    Generate a list of squares from 1 to n.
    
    Args:
        n: Upper bound
    
    Returns:
        List [1, 4, 9, 16, ..., n*n]
    """
    pass


def filter_even(numbers):
    """
    Filter only the even numbers from the list.
    
    Args:
        numbers: List of integers
    
    Returns:
        List containing only even numbers (in original order)
    """
    pass


def get_word_lengths(words):
    """
    Get the length of each word in the list.
    
    Args:
        words: List of strings
    
    Returns:
        List of lengths corresponding to each word
    """
    pass


def filter_long_words(words, min_length):
    """
    Filter words that have at least min_length characters.
    
    Args:
        words: List of strings
        min_length: Minimum length threshold
    
    Returns:
        List of words with length >= min_length
    """
    pass


# =============================================================================
# SECTION 10: Set Comprehension
# =============================================================================

def unique_digits(number):
    """
    Get the unique digits in a number.
    
    Args:
        number: A non-negative integer
    
    Returns:
        Set of unique digits (as integers)
    """
    pass


def unique_first_letters(words):
    """
    Get unique first letters from a list of words.
    
    Args:
        words: List of non-empty strings
    
    Returns:
        Set of unique first characters (lowercase)
    """
    pass


# =============================================================================
# SECTION 11: Dict Comprehension
# =============================================================================

def number_to_square_map(n):
    """
    Create a mapping from numbers 1 to n to their squares.
    
    Args:
        n: Upper bound
    
    Returns:
        Dict like {1: 1, 2: 4, 3: 9, ...}
    """
    pass


def word_to_length_map(words):
    """
    Create a mapping from each word to its length.
    
    Args:
        words: List of strings
    
    Returns:
        Dict like {"hello": 5, "world": 5, ...}
    """
    pass


def char_frequency(text):
    """
    Count the frequency of each character in the text.
    
    Args:
        text: A string
    
    Returns:
        Dict mapping each character to its count
    """
    pass
