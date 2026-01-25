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
    return [initial_balance]


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
    return account[0]


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
    account[0] += amount


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
    account[0] -= amount


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
    return (id(account1) is id(account2)? True:False)


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
    account1 = create_account(initial_balance)
    account2 = account1
    return (account1, account2, True)


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
    deposit(account1, deposit_amount)
    return (get_balance(account1), get_balance(account2))


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
    new_account = create_account(old_account[0])
    return (id(old_account), id(new_account), !(are_same_account(old_account, new_account)))


def get_account_type(account):
    """
    Get the type of account object.
    
    Args:
        account: Account object
    
    Returns:
        Type of the account object
    """
    # TODO: Return type using type() function
    return type(account)


def verify_account_is_list(account):
    """
    Verify account is instance of list class.
    
    Args:
        account: Account object
    
    Returns:
        True if account is a list, False otherwise
    """
    # TODO: Use isinstance() to check if account is a list
    return isinstance(account, list)


def check_account_exists(account):
    """
    Check if account is None (doesn't exist).
    
    Args:
        account: Account reference that may be None
    
    Returns:
        True if account is None, False otherwise
    """
    # TODO: Use 'is None' to check
    return (account is None)


def demonstrate_dynamic_account_holder():
    """
    Show dynamic typing by reassigning account holder from int to string.
    
    Returns:
        Tuple (type_after_int, type_after_string) showing types after each assignment
    """
    # TODO: Assign holder = 12345 (account number), get type, 
    # reassign holder = "John Doe", get type, return both types
    holder = 12345
    type_after_int = type(holder)
    holder = "John Doe"
    type_after_string = type(holder)
    return (type_after_int, type_after_string)

def get_account_info(account):
    """
    Get complete account information.
    
    Args:
        account: Account object
    
    Returns:
        Tuple (account_id, account_type, account_balance)
    """
    # TODO: Return id(), type(), and balance of account
    return (id(account), type(account), account[0])

