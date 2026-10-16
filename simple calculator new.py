def calculate(num1, operator, num2):
    """Perform calculation based on the operator."""

    if operator == "+":
        return num1 + num2

    elif operator == "-":
        return num1 - num2

    elif operator == "*":
        return num1 * num2

    elif operator == "/":
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2

    else:
        return "Error: Invalid operator!"


def simple_calculator():
    print("===== SIMPLE CALCULATOR =====")

    while True:
        print("\nMenu:")
        print("1. Calculate")
        print("2. Clear")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            try:
                num1 = float(input("Enter first number: "))
                operator = input("Enter operator (+, -, *, /): ")
                num2 = float(input("Enter second number: "))

                if operator not in ["+", "-", "*", "/"]:
                    print("Invalid operator!")
                    continue

                result = calculate(num1, operator, num2)
                print("Result:", result)

            except ValueError:
                print("Invalid input! Please enter valid numbers.")

        elif choice == "2":
            print("Calculator cleared!")

        elif choice == "3":
            print("Thank you for using the calculator!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


# Start the calculator
simple_calculator()