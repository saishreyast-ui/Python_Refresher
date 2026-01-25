# Objective: Build a music festival planner to understand Python's built-in classes
# - Use tuples for immutable event details
# - Use lists for ordered schedules (mutable)
# - Use sets for unique artist rosters
# - Use frozensets for locked lineups
# - Use dicts for artist registries
# - Understand the += aliasing behavior


# =============================================================================
# SECTION 1: Tuples, Truthiness, and Parsing (bool, int, float, tuple, str)
# =============================================================================

def create_event_info(name, date, venue):
    """
    Create immutable event details as a tuple.
    
    Args:
        name: Name of the festival
        date: Date of the event
        venue: Venue location
    
    Returns:
        Tuple containing (name, date, venue)
    """
    # TODO: Create and return a tuple with the event details
    pass


def is_lineup_ready(performers):
    """
    Check if the lineup has any performers using truthiness.
    
    Args:
        performers: List of performer names
    
    Returns:
        True if there are performers, False if empty
    """
    # TODO: Use truthiness to check if performers list is non-empty
    pass


def parse_ticket_price(price_str):
    """
    Parse a ticket price from a string to a float.
    
    Args:
        price_str: Price as a string (e.g., "25" or "29.99")
    
    Returns:
        Price as a float
    """
    # TODO: Convert the string to a float
    pass


def parse_stage_number(stage_str, base=10):
    """
    Parse a stage number from a string in a given base.
    
    Args:
        stage_str: Stage number as string (e.g., "5", "101" for binary)
        base: The base to parse (default 10, could be 2 for binary)
    
    Returns:
        Stage number as integer
    """
    # TODO: Convert the string to an integer using the specified base
    pass


# =============================================================================
# SECTION 2: Lists and Sequence Operators
# =============================================================================

def create_schedule():
    """
    Create an empty performance schedule.
    
    Returns:
        Empty list to hold performers
    """
    # TODO: Return an empty list
    pass


def add_to_schedule(schedule, performer):
    """
    Add a performer to the end of the schedule.
    
    Args:
        schedule: The performance schedule list
        performer: Name of performer to add
    """
    # TODO: Add performer to the schedule list
    pass


def get_headliners(schedule, count):
    """
    Get the first N performers from the schedule (the headliners).
    
    Args:
        schedule: The performance schedule list
        count: Number of headliners to get
    
    Returns:
        List of first N performers
    """
    # TODO: Use slicing to get the first count performers
    pass


def get_closing_acts(schedule, count):
    """
    Get the last N performers from the schedule (closing acts).
    
    Args:
        schedule: The performance schedule list
        count: Number of closing acts to get
    
    Returns:
        List of last N performers
    """
    # TODO: Use negative slicing to get the last count performers
    pass


def is_performing(schedule, artist):
    """
    Check if an artist is in the schedule.
    
    Args:
        schedule: The performance schedule list
        artist: Name of artist to check
    
    Returns:
        True if artist is in schedule, False otherwise
    """
    # TODO: Check membership using the in operator
    pass


# =============================================================================
# SECTION 3: Sets and Set Operators
# =============================================================================

def create_artist_set(artist_list):
    """
    Create a set of unique artists from a list.
    
    Args:
        artist_list: List of artist names (may contain duplicates)
    
    Returns:
        Set of unique artist names
    """
    # TODO: Convert the list to a set
    pass


def get_all_performers(stage1_artists, stage2_artists):
    """
    Get all unique performers across both stages.
    
    Args:
        stage1_artists: Set of artists on stage 1
        stage2_artists: Set of artists on stage 2
    
    Returns:
        Set of all artists from both stages
    """
    # TODO: Return the union of both sets
    pass


def get_crossover_artists(stage1_artists, stage2_artists):
    """
    Find artists performing on both stages.
    
    Args:
        stage1_artists: Set of artists on stage 1
        stage2_artists: Set of artists on stage 2
    
    Returns:
        Set of artists appearing on both stages
    """
    # TODO: Return the intersection of both sets
    pass


def get_exclusive_to_stage(stage1_artists, stage2_artists):
    """
    Find artists performing only on stage 1.
    
    Args:
        stage1_artists: Set of artists on stage 1
        stage2_artists: Set of artists on stage 2
    
    Returns:
        Set of artists only on stage 1
    """
    # TODO: Return the difference (stage1 - stage2)
    pass


def is_subset_lineup(small_lineup, full_lineup):
    """
    Check if small_lineup is a subset of full_lineup.
    
    Args:
        small_lineup: Smaller set of artists
        full_lineup: Larger set of artists
    
    Returns:
        True if small_lineup is subset of full_lineup
    """
    # TODO: Check if small_lineup is a subset of full_lineup
    pass


def lock_lineup(artists):
    """
    Create an immutable frozen set from the artist set.
    
    Args:
        artists: Set of artist names
    
    Returns:
        Frozenset of artist names (immutable)
    """
    # TODO: Convert to frozenset
    pass


# =============================================================================
# SECTION 4: Dicts and Dict Operators
# =============================================================================

def create_artist_registry():
    """
    Create an empty artist registry (artist name -> stage mapping).
    
    Returns:
        Empty dictionary
    """
    # TODO: Return an empty dictionary
    pass


def register_artist(registry, name, stage):
    """
    Register an artist to a stage in the registry.
    
    Args:
        registry: The artist registry dictionary
        name: Artist name
        stage: Stage name/number
    """
    # TODO: Add or update the artist's stage in the registry
    pass


def get_artist_stage(registry, name):
    """
    Get the stage assigned to an artist.
    
    Args:
        registry: The artist registry dictionary
        name: Artist name
    
    Returns:
        Stage name/number for the artist
    """
    # TODO: Return the stage for the given artist
    pass


def is_registered(registry, name):
    """
    Check if an artist is registered.
    
    Args:
        registry: The artist registry dictionary
        name: Artist name to check
    
    Returns:
        True if artist is in registry, False otherwise
    """
    # TODO: Check if name is a key in the registry
    pass


def remove_artist(registry, name):
    """
    Remove an artist from the registry.
    
    Args:
        registry: The artist registry dictionary
        name: Artist name to remove
    """
    # TODO: Delete the artist from the registry
    pass


# =============================================================================
# SECTION 5: The += Aliasing Trap
# =============================================================================

def share_lineup_alias(original):
    """
    Return an alias to the original lineup (same object).
    
    Args:
        original: The original lineup list
    
    Returns:
        Reference to the same list object
    """
    # TODO: Return the original list (creating an alias)
    pass


def share_lineup_copy(original):
    """
    Return a shallow copy of the lineup (new object).
    
    Args:
        original: The original lineup list
    
    Returns:
        New list with same contents
    """
    # TODO: Return a copy of the list
    pass


def extend_with_concat(lineup, new_artists):
    """
    Extend lineup using + concatenation (creates new list).
    
    Args:
        lineup: The original lineup list
        new_artists: List of new artists to add
    
    Returns:
        New list containing all artists
    """
    # TODO: Use + to concatenate and return the result
    pass


def extend_with_plus_equals(lineup, new_artists):
    """
    Extend lineup using += (modifies in place).
    
    Args:
        lineup: The original lineup list
        new_artists: List of new artists to add
    
    Returns:
        The same list object (now extended)
    """
    # TODO: Use += to extend the lineup in place, then return it
    pass


def demonstrate_alias_trap():
    """
    Demonstrate the difference between + and += with aliased lists.
    
    Returns:
        Tuple (concat_breaks_alias, plus_equals_keeps_alias) where:
        - concat_breaks_alias: True if + created a new object
        - plus_equals_keeps_alias: True if += modified the original
    """
    # TODO: Create a list and an alias
    # Use + to extend and check if alias sees the change
    # Use += to extend and check if alias sees the change
    # Return tuple showing the behavior difference
    pass
