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

def evaluate_expression(expression):
    """
    Evaluate a mathematical expression with high precision.
    """
    try:
        # Convert expression to Decimal
        expression = expression.replace('/', ' / ').replace('*', ' * ')
        result = eval(expression, {"__builtins__": None}, {"Decimal": Decimal, "math": __import__('math')})
        return Decimal(result)
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        return f"Error: {e}"

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

    expression = input("Enter your expression: ")  # Get the full mathematical expression from the user
    result = evaluate_expression(expression)
    display_result(result)

if __name__ == "__main__":
    main()
