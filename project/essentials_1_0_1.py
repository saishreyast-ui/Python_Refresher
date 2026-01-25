# Objective: Build a movie ticket pricing system for a cinema
# - Child (under 13): $8
# - Adult (13-64): $12
# - Senior (65+): $10
# - Premium days (Friday/Saturday): add $3 surcharge


def calculate_base_price(age):
    """
    Calculate base ticket price based on age.
    
    Args:
        age: Customer's age in years
    
    Returns:
        Base ticket price as integer
    """
    # TODO: Fix the indentation errors below
    if age < 13:
    return 8
    elif age >= 65:
    return 10
    else:
    return 12


def is_premium_day(day):
    """
    Check if the day is a premium day (Friday or Saturday).
    
    Args:
        day: Day of week as string (e.g., "Friday", "Monday")
    
    Returns:
        True if premium day, False otherwise
    """
    # TODO: Fix the indentation errors below
    if day == "Friday" or day == "Saturday":
    return True
    else:
    return False


def calculate_total_price(age, day):
    """
    Calculate total ticket price including premium day surcharge.
    
    Args:
        age: Customer's age in years
        day: Day of week as string
    
    Returns:
        Total ticket price as integer
    """
    # TODO: Fix the indentation errors below
    base_price = calculate_base_price(age)
    if is_premium_day(day):
    return base_price + 3
    else:
    return base_price


def get_ticket_category(age):
    """
    Return the ticket category name based on age.
    
    Args:
        age: Customer's age in years
    
    Returns:
        Category as string: "Child", "Senior", or "Adult"
    """
    # TODO: Complete this function with correct indentation
    # Return "Child" if age < 13, "Senior" if age >= 65, "Adult" otherwise
    pass

