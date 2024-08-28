import time
import random

def check_number(value):
    try:
        float(value)  # Try converting the value to a float
        return True
    except ValueError:
        print("Error: The value is not a valid number.")
        return False

def retry_input(prompt):
    while True:
        value = input(prompt)
        if check_number(value):
            return float(value)  # Convert to float to handle decimals

def get_operation():
    valid_operations = ["+", "-", "*", "/", "addition", "subtract", "multiply", "divide"]
    while True:
        operation = input("Operation= ").lower()
        if operation in valid_operations:
            return operation
        else:
            print("Error: Invalid operation. Please enter a valid operation (+, -, *, /, addition, subtract, multiply, divide).")

user = input("User= ")
load = 0

print(user + "/Activating.....")
while load < 100:
    random_increment = random.randint(1, 20)  # Random increment between 1 and 20
    load += random_increment
    load = min(load, 100)  # Ensure load doesn't exceed 100
    random_sleep = random.uniform(0, 0.5)  # Random sleep time between 0 and 0.5 seconds
    time.sleep(random_sleep)
    print(str(load) + "%")

print("ASDM Complex has booted...")
time.sleep(0.5)
print("Welcome " + user + "!")
time.sleep(0.5)

print ("Please enter the numbers below:")

one = retry_input("")
two = retry_input("")

operation = get_operation()

if operation in ("+", "addition", "add"):
    result = one + two
elif operation in ("-", "subtract", "minus"):
    result = one - two
elif operation in ("*", "multiply"):
    result = one * two
elif operation in ("/", "divide"):
    if two == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = one / two

print("Result:", result)
