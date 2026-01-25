# Objective: Build a bank account manager to understand objects, aliases, and identity
# - Accounts are objects (represented as lists: [balance])
# - Joint accounts demonstrate aliases (two names for same account object)
# - Changes through one alias affect all aliases (deposits/withdrawals)
# - Use id() to verify if accounts are the same object


def create_account(initial_balance):
    """
    Create a bank account with initial balance.
    
    Args:
        initial_balance: Starting balance as integer
    
    Returns:
        Account object (list containing balance)
    
    Hint: Represent account as a list with one element (the balance).
          Lists are mutable objects - they can be modified after creation.
          Return a list like [initial_balance]
    """
    # TODO: Create and return a list containing the initial_balance
    pass


def get_balance(account):
    """
    Get current account balance.
    
    Args:
        account: Account object (list with balance)
    
    Returns:
        Current balance as integer
    
    Hint: Account is a list with balance as first element.
          Access first element using account[0]
    """
    # TODO: Return the balance from the account list
    pass


def deposit(account, amount):
    """
    Deposit money into account.
    
    Args:
        account: Account object (list with balance)
        amount: Amount to deposit
    
    Hint: Since lists are mutable, you can modify the balance directly.
          Set account[0] to current balance + amount.
          This modifies the original object - all aliases will see this change!
    """
    # TODO: Add amount to account balance (modify account[0])
    pass


def withdraw(account, amount):
    """
    Withdraw money from account.
    
    Args:
        account: Account object (list with balance)
        amount: Amount to withdraw
    
    Hint: Similar to deposit, but subtract amount from balance.
          Modify account[0] directly.
    """
    # TODO: Subtract amount from account balance (modify account[0])
    pass


def are_same_account(account1, account2):
    """
    Check if two account references point to the same account object.
    
    Args:
        account1: First account reference
        account2: Second account reference
    
    Returns:
        True if same account object, False otherwise
    """
    # TODO: Use id() to check if both references point to same object
    pass


def setup_joint_account(initial_balance):
    """
    Create joint account where two holders share the same account.
    
    Args:
        initial_balance: Starting balance
    
    Returns:
        Tuple (holder1_account, holder2_account, are_same) where both accounts
        are aliases (references to same object) and are_same is True
    """
    # TODO: Create one account, create alias, verify they're same using id()
    pass


def verify_joint_account_deposit(account1, account2, deposit_amount):
    """
    Deposit money via account1 and verify balance updated in account2.
    
    Args:
        account1: First account reference
        account2: Second account reference  
        deposit_amount: Amount to deposit
    
    Returns:
        Tuple (balance_via_account1, balance_via_account2) showing both balances after deposit
    """
    # TODO: Deposit via account1, return balances from both references
    pass


def close_and_open_new_account(old_account, new_balance):
    """
    Close old account and open new one (breaking alias).
    
    Args:
        old_account: Existing account
        new_balance: Balance for new account
    
    Returns:
        Tuple (old_id, new_id, are_different) where are_different is True
    """
    # TODO: Get old account id, create new account, get new id, verify different
    pass


def get_account_type(account):
    """
    Get the type of account object.
    
    Args:
        account: Account object
    
    Returns:
        Type of the account object
    """
    # TODO: Return type using type() function
    pass


def verify_account_is_list(account):
    """
    Verify account is instance of list class.
    
    Args:
        account: Account object
    
    Returns:
        True if account is a list, False otherwise
    """
    # TODO: Use isinstance() to check if account is a list
    pass


def check_account_exists(account):
    """
    Check if account is None (doesn't exist).
    
    Args:
        account: Account reference that may be None
    
    Returns:
        True if account is None, False otherwise
    """
    # TODO: Use 'is None' to check
    pass


def demonstrate_dynamic_account_holder():
    """
    Show dynamic typing by reassigning account holder from int to string.
    
    Returns:
        Tuple (type_after_int, type_after_string) showing types after each assignment
    """
    # TODO: Assign holder = 12345 (account number), get type, 
    # reassign holder = "John Doe", get type, return both types
    pass


def get_account_info(account):
    """
    Get complete account information.
    
    Args:
        account: Account object
    
    Returns:
        Tuple (account_id, account_type, account_balance)
    """
    # TODO: Return id(), type(), and balance of account
    pass

