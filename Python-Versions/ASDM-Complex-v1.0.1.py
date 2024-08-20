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

user = input("User= ")
load = 0

print(user + "/Activating.....")
while load < 100:
    random_increment = random.randint(1, 10)  # Random increment between 1 and 10
    load += random_increment
    load = min(load, 100)  # Ensure load doesn't exceed 100
    random_sleep = random.uniform(0, 1)  # Random sleep time between 0 and 1 second
    time.sleep(random_sleep)
    print(str(load) + "%")

print("Recovering....")
time.sleep(2)
print("ASDM Complex has booted...")
time.sleep(1)
print("Welcome " + user + "!")
time.sleep(1)

one = retry_input("Number 1= ")
two = retry_input("Number 2= ")

operation = input("Operation= ")

if operation in ("+", "addition", "add"):
    result = one + two
    print(result)
elif operation in ("-", "subtract", "minus"):
    result = one - two
    print(result)
elif operation in ("*", "multiply"):
    result = one * two
    print(result)
elif operation in ("/", "divide"):
    if two == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = one / two
        print(result)
