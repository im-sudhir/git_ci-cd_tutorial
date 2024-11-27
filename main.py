# main.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def modulus(a, b):
    """Return the modulus of two numbers."""
    if b == 0:
        return "Error: Modulus by zero is not allowed."
    return a % b

def main():
    print("Simple Arithmetic Operations")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    
    try:
        choice = int(input("Choose an operation (1-5): "))
        if choice < 1 or choice > 5:
            print("Invalid choice. Please select a number between 1 and 5.")
            return

        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))

        if choice == 1:
            print(f"Result: {add(a, b)}")
        elif choice == 2:
            print(f"Result: {subtract(a, b)}")
        elif choice == 3:
            print(f"Result: {multiply(a, b)}")
        elif choice == 4:
            print(f"Result: {divide(a, b)}")
        elif choice == 5:
            print(f"Result: {modulus(a, b)}")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    main()
