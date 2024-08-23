import time
import random
from decimal import Decimal, getcontext, InvalidOperation

# Set precision for decimal operations
getcontext().prec = 10_000  # High precision to handle large numbers accurately

def check_number(value):
    """
    Check if the input value can be converted to a Decimal.
    """
    try:
        Decimal(value)
        return True
    except (ValueError, InvalidOperation):
        print("Error: The value is not a valid number.")
        return False

def retry_input(prompt):
    """
    Continuously prompt the user until a valid Decimal number is entered.
    """
    while True:
        value = input(prompt)
        if check_number(value):
            return Decimal(value)  # Convert to Decimal for accurate calculations

def get_operation():
    """
    Prompt the user to enter a valid operation.
    """
    valid_operations = {
        "+": "+", 
        "-": "-", 
        "*": "*", 
        "/": "/", 
        "add": "+", 
        "subtract": "-", 
        "multiply": "*", 
        "divide": "/"
    }
    while True:
        operation = input("Operation (add, subtract, multiply, divide, +, -, *, /)= ").lower()
        if operation in valid_operations:
            return valid_operations[operation]
        print("Error: Invalid operation. Please enter one of the following: add, subtract, multiply, divide, +, -, *, /.")

def print_loading_animation(user):
    """
    Display a loading animation while initializing the application.
    """
    print(f"{user}/Activating.....")
    load = 0
    while load < 100:
        load += random.randint(1, 30)  # Increment load by a random amount
        load = min(load, 100)  # Ensure load doesn't exceed 100
        print(f"{load}%")
        time.sleep(random.uniform(0, 0.5))  # Random sleep time between 0 and 0.5 seconds

def perform_calculation(one, two, operation):
    """
    Perform the calculation based on the operation provided.
    """
    if operation == "+":
        return one + two
    elif operation == "-":
        return one - two
    elif operation == "*":
        return one * two
    elif operation == "/":
        if two == 0:
            return "Error: Division by zero is not allowed."
        return one / two

def display_result(result):
    """
    Display the result, converting to integer if it's a whole number.
    """
    if isinstance(result, Decimal) and result == result.to_integral_value():
        result = int(result)  # Convert to an integer to remove the decimal
    print(f"Result: {result}")

def main():
    user = input("User= ")
    print_loading_animation(user)
    print("ASDM Complex has booted...")
    time.sleep(0.5)
    print(f"Welcome {user}!")
    time.sleep(0.5)

    one = retry_input("Number 1: ")
    two = retry_input("Number 2: ")

    operation = get_operation()
    result = perform_calculation(one, two, operation)
    display_result(result)

if __name__ == "__main__":
    main()
