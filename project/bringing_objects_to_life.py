# Objective: Build a coffee shop order system where customers can create and customize coffee orders
# - Create Coffee objects using a class (instantiation)
# - Add customizations using mutator methods (modify the order)
# - Get order details using accessor methods (read information)
# - Chain methods together for smooth customization



class Coffee:
    """
    A Coffee class representing a coffee order at a coffee shop.
    
    Base prices by size:
    - "small": $3.00
    - "medium": $4.00
    - "large": $5.00
    """
    
    def __init__(self, size, coffee_type):
        """
        Initialize a Coffee object.
        
        Args:
            size: Size of coffee ("small", "medium", or "large")
            coffee_type: Type of coffee (e.g., "latte", "cappuccino", "espresso")
        
        Hint: Store size and coffee_type as instance variables using self.
              Initialize empty lists for syrups and extras.
              Set base price based on size.
        """
        # TODO: Initialize instance variables
        # self.size = size
        # self.coffee_type = coffee_type
        # self.syrups = []  # List to store added syrups
        # self.milk_type = None  # No milk by default
        # self.has_whipped_cream = False
        # self.base_price = 3.0 if size == "small" else (4.0 if size == "medium" else 5.0)
        pass
    
    def add_syrup(self, syrup_flavor):
        """
        Add a syrup to the coffee (MUTATOR method - modifies the object).
        Each syrup adds $0.50 to the price.
        
        Args:
            syrup_flavor: Flavor of syrup to add (e.g., "vanilla", "caramel")
        
        Returns:
            self (to allow method chaining)
        
        Hint: Append syrup_flavor to self.syrups list, then return self
        """
        # TODO: Add syrup to the syrups list and return self
        pass
    
    def add_milk(self, milk_type):
        """
        Add milk to the coffee (MUTATOR method).
        Milk adds $0.50 to the price.
        
        Args:
            milk_type: Type of milk (e.g., "whole", "oat", "almond")
        
        Returns:
            self (to allow method chaining)
        
        Hint: Set self.milk_type to the milk_type, then return self
        """
        # TODO: Set milk type and return self
        pass
    
    def add_whipped_cream(self):
        """
        Add whipped cream to the coffee (MUTATOR method).
        Whipped cream adds $0.75 to the price.
        
        Returns:
            self (to allow method chaining)
        
        Hint: Set self.has_whipped_cream to True, then return self
        """
        # TODO: Add whipped cream and return self
        pass
    
    def get_price(self):
        """
        Calculate total price of the coffee (ACCESSOR method - doesn't modify).
        
        Returns:
            Total price as float
        
        Hint: Start with base_price, add $0.50 per syrup, $0.50 if milk added,
              $0.75 if whipped cream added
        """
        # TODO: Calculate and return total price
        pass
    
    def get_description(self):
        """
        Get full description of the coffee order (ACCESSOR method).
        
        Returns:
            Description string
        
        Hint: Build a string like "Large Latte with vanilla syrup, oat milk, whipped cream"
        """
        # TODO: Build and return description string
        pass
    
    def get_size(self):
        """
        Get the size of the coffee (ACCESSOR method).
        
        Returns:
            Size string
        """
        # TODO: Return the size
        pass
    
    def get_type(self):
        """
        Get the type of coffee (ACCESSOR method).
        
        Returns:
            Coffee type string
        """
        # TODO: Return the coffee type
        pass


def create_simple_coffee(size, coffee_type):
    """
    Create a basic coffee with no customizations.
    This demonstrates instantiation - creating an object from a class.
    
    Args:
        size: Size of coffee
        coffee_type: Type of coffee
    
    Returns:
        Coffee object
    
    Hint: Call Coffee class like a function: Coffee(size, coffee_type)
    """
    # TODO: Create and return a Coffee object
    pass


def create_customized_coffee(size, coffee_type, syrup, milk):
    """
    Create a coffee with syrup and milk customizations.
    
    Args:
        size: Size of coffee
        coffee_type: Type of coffee
        syrup: Syrup flavor to add
        milk: Milk type to add
    
    Returns:
        Customized Coffee object
    
    Hint: Create Coffee object, then call add_syrup() and add_milk() on it
    """
    # TODO: Create coffee and add customizations
    pass


def create_deluxe_coffee_with_chaining(size, coffee_type, syrup1, syrup2, milk):
    """
    Create a deluxe coffee using method chaining.
    Deluxe coffee should have whipped cream.
    
    Args:
        size: Size of coffee
        coffee_type: Type of coffee
        syrup1: First syrup flavor
        syrup2: Second syrup flavor
        milk: Milk type
    
    Returns:
        Deluxe Coffee object
    
    Hint: Chain methods: coffee.add_syrup(syrup1).add_syrup(syrup2).add_milk(milk).add_whipped_cream()
    """
    # TODO: Create coffee and chain customization methods
    pass


def compare_two_orders(coffee1, coffee2):
    """
    Compare prices of two coffee orders (using accessor methods).
    
    Args:
        coffee1: First Coffee object
        coffee2: Second Coffee object
    
    Returns:
        Tuple (price1, price2, more_expensive) where more_expensive is 1 if coffee1
        costs more, 2 if coffee2 costs more, or 0 if they cost the same
    
    Hint: Use get_price() accessor method on both objects to compare
    """
    # TODO: Get prices and compare them
    pass

