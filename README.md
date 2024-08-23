# ASDM Complex Calculator

**ASDM Complex Calculator** is an interactive Python program designed to perform addition, subtraction, division, and multiplication of numbers with a touch of personalization and user engagement.

## Features

- **User Authentication and Booting Sequence:** The program greets users with a personalized loading sequence, simulating a system boot-up process.
- **Comprehensive Error Handling:** Ensures only valid numeric inputs are accepted, preventing runtime errors.
- **Flexible Operation Input:** Supports multiple ways to specify operations, including keywords like "addition" or symbols like "+".
- **Basic Arithmetic:** Handles addition, subtraction, multiplication, and division with built-in checks (like division by zero).

# Update Log
## Python
-------------------------------------------------------------------------------------------------------------------------------------------------
- **23-8-24 - v1.0.4:** BIG CHANGE 
1. **`get_operation` Function**: Updated to recognize both symbols (`+`, `-`, `*`, `/`) and keywords (`add`, `subtract`, `multiply`, `divide`).
2. **Prompt Message**: Adjusted to include both symbols and keywords for operation input.
3. **Error Handling**: Added handling for invalid operations to guide users correctly.
4. **Operation Mapping**: Simplified operation mapping using a dictionary for easy extension and maintenance.
5. **Result Display**: Used `result.to_integral_value()` to check if the result can be an integer more efficiently.
6. **Speed**: Made the `load += random.randint(1, 20)` value to `(1, 30)`.
---------------------------------------------------------------------------------------------------------------------------------------------------
- **17-8-24 - v1.0.3:** Fixed floating-point precision error, Fixed decimal errors.
- **16-8-24 - v1.0.2:** Faster Booting speed, Changed input, Can detect inputs that are not possible, Allows decimal.
- **15-8-24 - v1.0.1:** Release Date.

## HTML
- **20-8-24 - v1.0.3:** Woohoo! Finally The HTML verson is out!

## Upcoming
- **Python-v1.0.5:** idk lol.
- **HTML:** Everytime changes after many new python versions is released.

Here are all the features changed in this version:



These changes enhance user interaction, increase flexibility in input handling, and improve overall code clarity.
