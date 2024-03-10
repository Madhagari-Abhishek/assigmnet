def compound_interest(principal, rate, time):
    """
    Function to calculate compound interest.

    Args:
    principal (float): The principal amount.
    rate (float): The annual interest rate (in percentage).
    time (float): The time duration for which the interest is applied (in years).

    Returns:
    float: The compound interest.
    """
    # Convert rate to decimal
    rate = rate / 100

    # Calculate compound interest
    amount = principal * (1 + rate) ** time
    compound_interest = amount - principal

    return compound_interest

# Example usage
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in percentage): "))
time = float(input("Enter time duration (in years): "))

interest = compound_interest(principal, rate, time)
print("Compound interest:", round(interest, 2))
