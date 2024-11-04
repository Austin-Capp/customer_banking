# Import the create_cd_account and create_savings_account functions
from Account import Account
from customer_banking import create_cd_account, create_savings_account 

# Define the main function
def main():
    """This function prompts the user to enter the savings and CD account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account
    savings_balance = float(input("Enter the initial savings account balance: "))
    savings_interest = float(input("Enter the annual interest rate for the savings account (as a percentage): "))
    savings_maturity = int(input("Enter the number of months for the savings account: "))

    # Call the create_savings_account function and pass the variables from the user
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months
    print(f"Interest earned on the savings account: ${savings_interest_earned:.2f}")
    print(f"Updated savings account balance after {savings_maturity} months: ${updated_savings_balance:.2f}\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account
    cd_balance = float(input("Enter the initial CD account balance: "))
    cd_interest = float(input("Enter the annual interest rate for the CD account (as a percentage): "))
    cd_maturity = int(input("Enter the number of months for the CD account: "))

    # Call the create_cd_account function and pass the variables from the user
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months
    print(f"Interest earned on the CD account: ${cd_interest_earned:.2f}")
    print(f"Updated CD account balance after {cd_maturity} months: ${updated_cd_balance:.2f}")

if __name__ == "__main__":
    # Call the main function
    main()
