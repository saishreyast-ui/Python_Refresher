# Objective: Build a collection processor toolkit to master Python functions
# - Define functions with proper signatures and return values
# - Use default parameter values for optional behavior
# - Use keyword arguments for clarity and flexibility
# - Understand mutable parameter behavior (in-place vs new object)
# - Pass functions as arguments (first-class functions)
# - Use Python's built-in functions: sorted, reversed, sum, len, max, min, all, any


# =============================================================================
# SECTION 1: Basic Function Definition and Return Values
# =============================================================================

def get_length(items):
    """
    Return the number of items in a collection.
    
    Args:
        items: Any iterable (list, tuple, string, etc.)
    
    Returns:
        Integer count of items
    """
    pass


def get_sum(numbers):
    """
    Return the sum of all numbers in the collection.
    
    Args:
        numbers: Collection of numbers
    
    Returns:
        Sum of all numbers
    """
    pass


def get_average(numbers):
    """
    Return the average (mean) of numbers in the collection.
    
    Args:
        numbers: Collection of numbers
    
    Returns:
        Average as a float, or None if collection is empty
    """
    pass


def get_extremes(numbers):
    """
    Return both the minimum and maximum values.
    
    Args:
        numbers: Collection of numbers
    
    Returns:
        Tuple (minimum, maximum)
    """
    pass


# =============================================================================
# SECTION 2: Default Parameter Values
# =============================================================================

def slice_items(items, start=0, end=None):
    """
    Return a slice of items from start to end.
    
    Args:
        items: Collection to slice
        start: Starting index (default 0)
        end: Ending index exclusive (default None means end of collection)
    
    Returns:
        Sliced portion of items as a list
    """
    pass


def repeat_items(items, times=2):
    """
    Repeat the items a specified number of times.
    
    Args:
        items: Collection to repeat
        times: Number of repetitions (default 2)
    
    Returns:
        New list with items repeated
    """
    pass


def pad_list(items, target_length, pad_value=0):
    """
    Pad a list to reach target length.
    
    Args:
        items: List to pad
        target_length: Desired length
        pad_value: Value to use for padding (default 0)
    
    Returns:
        New list padded to target_length (or original if already long enough)
    """
    pass


# =============================================================================
# SECTION 3: Keyword Arguments for Clarity
# =============================================================================

def create_record(name, value, category="default", active=True, priority=1):
    """
    Create a record dictionary with the given attributes.
    
    Args:
        name: Record name (required)
        value: Record value (required)
        category: Category string (default "default")
        active: Whether record is active (default True)
        priority: Priority level 1-5 (default 1)
    
    Returns:
        Dictionary with all attributes
    """
    pass


def format_number(number, decimals=2, prefix="", suffix="", use_thousands=False):
    """
    Format a number as a string with various options.
    
    Args:
        number: The number to format
        decimals: Decimal places (default 2)
        prefix: String to prepend (default "")
        suffix: String to append (default "")
        use_thousands: Whether to use thousand separators (default False)
    
    Returns:
        Formatted string
    """
    pass


def sort_records(records, key="name", reverse=False):
    """
    Sort a list of record dictionaries by a specified key.
    
    Args:
        records: List of dictionaries
        key: Dictionary key to sort by (default "name")
        reverse: Sort in descending order (default False)
    
    Returns:
        New sorted list
    """
    pass


# =============================================================================
# SECTION 4: Mutable Parameter Behavior
# =============================================================================

def append_item(items, value):
    """
    Append a value to the list IN-PLACE.
    This modifies the original list.
    
    Args:
        items: List to modify
        value: Value to append
    
    Returns:
        None (modification is in-place)
    """
    pass


def append_item_safe(items, value):
    """
    Append a value to a COPY of the list.
    Original list remains unchanged.
    
    Args:
        items: List to copy and extend
        value: Value to append
    
    Returns:
        New list with value appended
    """
    pass


def remove_negatives_inplace(numbers):
    """
    Remove all negative numbers from the list IN-PLACE.
    
    Args:
        numbers: List of numbers to modify
    
    Returns:
        None (modification is in-place)
    """
    pass


def remove_negatives_safe(numbers):
    """
    Return a new list with negative numbers removed.
    Original list remains unchanged.
    
    Args:
        numbers: List of numbers
    
    Returns:
        New list containing only non-negative numbers
    """
    pass


# =============================================================================
# SECTION 5: First-Class Functions (Passing Functions as Arguments)
# =============================================================================

def apply_to_all(items, func):
    """
    Apply a function to each item in the collection.
    
    Args:
        items: Collection of items
        func: Function to apply to each item
    
    Returns:
        New list with function applied to each item
    """
    pass


def filter_items(items, predicate):
    """
    Filter items using a predicate function.
    
    Args:
        items: Collection of items
        predicate: Function that returns True/False for each item
    
    Returns:
        New list containing only items where predicate returns True
    """
    pass


def reduce_items(items, func, initial):
    """
    Reduce a collection to a single value using a function.
    
    Args:
        items: Collection of items
        func: Function that takes (accumulator, item) and returns new accumulator
        initial: Initial value for the accumulator
    
    Returns:
        Final accumulated value
    """
    pass


def find_first(items, predicate):
    """
    Find the first item matching a predicate.
    
    Args:
        items: Collection of items
        predicate: Function that returns True/False for each item
    
    Returns:
        First item where predicate returns True, or None if not found
    """
    pass


def compose(func1, func2):
    """
    Create a new function that applies func2 then func1.
    Result: func1(func2(x))
    
    Args:
        func1: Outer function
        func2: Inner function
    
    Returns:
        New function that is the composition of func1 and func2
    """
    pass


# =============================================================================
# SECTION 6: Using Built-in Functions
# =============================================================================

def check_all_positive(numbers):
    """
    Check if ALL numbers in the collection are positive.
    
    Args:
        numbers: Collection of numbers
    
    Returns:
        True if all are positive, False otherwise
    """
    pass


def check_any_negative(numbers):
    """
    Check if ANY number in the collection is negative.
    
    Args:
        numbers: Collection of numbers
    
    Returns:
        True if at least one is negative, False otherwise
    """
    pass


def get_sorted_copy(items, reverse=False):
    """
    Return a sorted copy of items.
    
    Args:
        items: Collection to sort
        reverse: Sort in descending order (default False)
    
    Returns:
        New sorted list
    """
    pass


def get_reversed_copy(items):
    """
    Return a reversed copy of items.
    
    Args:
        items: Collection to reverse
    
    Returns:
        New list with items in reverse order
    """
    pass


def count_occurrences(items, target):
    """
    Count how many times target appears in items.
    
    Args:
        items: Collection to search
        target: Value to count
    
    Returns:
        Number of occurrences
    """
    pass
