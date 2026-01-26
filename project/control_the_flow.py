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
    return (not value)


def both_true(a, b):
    """
    Check if both values are truthy.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if both a and b are truthy, False otherwise
    """
    return bool(a and b)


def either_true(a, b):
    """
    Check if at least one value is truthy.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if a or b (or both) are truthy, False otherwise
    """
    return bool(a or b)


def is_empty(container):
    """
    Check if a container (list, string, dict, etc.) is empty.
    
    Args:
        container: A container to check
    
    Returns:
        True if empty, False if it has elements
    """
    return (not container)


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
    if a:
        return a
    elif b:
        return b
    else:
        return default


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
    return (id(a) == id(b))


def are_different_objects(a, b):
    """
    Check if a and b are different objects in memory.
    
    Args:
        a: First object
        b: Second object
    
    Returns:
        True if different objects, False if same object
    """
    return (id(a) != id(b))


def are_equal(a, b):
    """
    Check if a and b have equal values.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if values are equal, False otherwise
    """
    return a==b


def are_not_equal(a, b):
    """
    Check if a and b have different values.
    
    Args:
        a: First value
        b: Second value
    
    Returns:
        True if values are different, False otherwise
    """
    return a != b


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
    if a < b: return "less"
    elif a==b: return "equal"
    else: return "greater"


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
    if low <= value and value <= high: return True
    return False

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
    return (a if a>(b if b>c else c) else (b if b>c else c))


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
    if minimum <= value and value <= maximum: return value
    elif value <= minimum: return minimum
    else: return maximum


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
    return a//b


def get_remainder(a, b):
    """
    Get the remainder of division (modulo).
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Remainder of a divided by b
    """
    return a%b


def divmod_result(a, b):
    """
    Return both quotient and remainder of division.
    
    Args:
        a: Dividend
        b: Divisor
    
    Returns:
        Tuple (quotient, remainder) using integer division
    """
    return (a//b, a%b)


def is_divisible(a, b):
    """
    Check if a is evenly divisible by b.
    
    Args:
        a: Number to check
        b: Potential divisor
    
    Returns:
        True if a is divisible by b, False otherwise
    """
    return a%b==0


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
    if n > 0: return "positive"
    if n ==0: return "zero"
    return "negative"



def get_number_type(n):
    """
    Determine if a number is even or odd.
    
    Args:
        n: An integer
    
    Returns:
        "even" or "odd"
    """
    return ("even" if n%2==0 else "odd")


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
    if score < 60: return "F"
    elif score<70: return "D"
    elif score<80: return "C"
    elif score<90: return "B"
    return "A"



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
    return n*(n+1)/2


def count_vowels(text):
    """
    Count the number of vowels (a, e, i, o, u) in the text.
    Case-insensitive.
    
    Args:
        text: A string to analyze
    
    Returns:
        Count of vowels
    """
    count = 0
    for e in text.lower():
        if e in ['a','e','i','o','u']: count+=1
    return count


def find_factors(n):
    """
    Find all factors of n (numbers that divide n evenly).
    
    Args:
        n: A positive integer
    
    Returns:
        List of factors in ascending order
    """
    L = []
    for i in range(1, n//2 +1):
        if n%i==0: L += [i]
    L += [n]
    return L


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
    L = []
    while start:
        L += [start]
        start -= 1
    return L


def sum_until_negative(numbers):
    """
    Sum numbers from the list until a negative number is encountered.
    The negative number is NOT included in the sum.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Sum of numbers before the first negative (or sum of all if no negatives)
    """
    sum = 0
    i = 0
    while numbers[i]>=0 and i<len(numbers):
        sum += numbers[i]
        i += 1
    return sum


def find_first_multiple(n, minimum):
    """
    Find the smallest multiple of n that is >= minimum.
    
    Args:
        n: The number to find multiples of
        minimum: The minimum value the multiple must be
    
    Returns:
        Smallest multiple of n that is >= minimum
    """
    if minimum%n==0: return n
    return ((minimum//n + 1) * n)


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
    for x in numbers:
        if x < 0:
            return x
    return None


def sum_positive_only(numbers):
    """
    Sum only the positive numbers in the list, skipping negatives and zero.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Sum of positive numbers only
    """
    total = 0
    for x in numbers:
        if x <= 0: continue
        total += x
    return total


def is_prime(n):
    """
    Check if n is a prime number.
    A prime is only divisible by 1 and itself.
    
    Args:
        n: A positive integer >= 2
    
    Returns:
        True if prime, False otherwise
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_index_of(items, target):
    """
    Find the index of target in items list.
    
    Args:
        items: List to search
        target: Value to find
    
    Returns:
        Index of target, or -1 if not found
    """
    for i, x in enumerate(items):
        if x == target:
            return i
    return -1


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
    return [i*i for i in range(1, n+1)]


def filter_even(numbers):
    """
    Filter only the even numbers from the list.
    
    Args:
        numbers: List of integers
    
    Returns:
        List containing only even numbers (in original order)
    """
    return [x for x in numbers if x % 2 == 0]


def get_word_lengths(words):
    """
    Get the length of each word in the list.
    
    Args:
        words: List of strings
    
    Returns:
        List of lengths corresponding to each word
    """
    return [len(w) for w in words]


def filter_long_words(words, min_length):
    """
    Filter words that have at least min_length characters.
    
    Args:
        words: List of strings
        min_length: Minimum length threshold
    
    Returns:
        List of words with length >= min_length
    """
    return [w for w in words if len(w) >= min_length]


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
    return {int(d) for d in str(number)}


def unique_first_letters(words):
    """
    Get unique first letters from a list of words.
    
    Args:
        words: List of non-empty strings
    
    Returns:
        Set of unique first characters (lowercase)
    """
    return {w[0].lower() for w in words}


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
    return {i: i*i for i in range(1, n+1)}


def word_to_length_map(words):
    """
    Create a mapping from each word to its length.
    
    Args:
        words: List of strings
    
    Returns:
        Dict like {"hello": 5, "world": 5, ...}
    """
    return {w: len(w) for w in words}


def char_frequency(text):
    """
    Count the frequency of each character in the text.
    
    Args:
        text: A string
    
    Returns:
        Dict mapping each character to its count
    """
    return {c: text.count(c) for c in set(text)}
