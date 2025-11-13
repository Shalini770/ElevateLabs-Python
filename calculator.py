# calculator.py
# A simple command-line calculator using functions, loops, and conditionals.

# --- Function Definitions ---

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers, handling division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def display_menu():
    """Display the list of available operations."""
    print("\n===== Simple Calculator =====")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

# --- Main Program ---

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break

        # Check for valid operation choice
        if choice not in ('1', '2', '3', '4'):
            print("Invalid choice! Please enter a number from 1 to 5.")
            continue

        # Take input numbers
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Perform operation based on user choice
        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

# --- Program Entry Point ---

if __name__ == "__main__":
    main()
