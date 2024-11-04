""" Create a Account class with methods"""

class Account:
    """Creating an Account class with methods"""
    def __init__(self, balance, interest_rate):
        self.balance = balance
        self.interest_rate = interest_rate

    # This method sets the balance of the account.
    def set_balance(self, balance):
        """Sets the balance for the for the account"""
        self.balance = balance

    # The method sets the interest gained for the account.
    def set_interest(self, interest_rate):
        """Sets the interest gained for the the account"""
        self.interest = interest_rate
    
    # This method calculates interest earned over a number of months.
    def calculate_intest(self, months):
        """Calculates interest earned over a specified number of months"""
        return self.balance * (self.interest_rate / 100) * (months / 12)
    
    # This method updates the balance after adding the interest earned.
    def update_balance(self, months):
        """Updates the balance after a specified number of months"""
        interest_earned = self.calculate_interest(months)
        self.balance += interest_earned
        return self.balance    
