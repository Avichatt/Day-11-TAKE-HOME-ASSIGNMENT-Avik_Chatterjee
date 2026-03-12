import logging

# Part A — Error Handling Refactor (Example Programs)

"""
Program 1 — Safe Age Calculator
Exception caught: ValueError
Recovery: User asked to enter age again.
User message: "Invalid input. Please enter a valid age."
Internal logging: Error stored in errors.log
"""

def safe_age_calculator():
    logging.basicConfig(filename="errors.log", level=logging.ERROR)
    
    while True:
        try:
            # Note: input() will hang in non-interactive environments
            age_str = input("Enter your age: ")
            age = int(age_str)

            if age < 0 or age > 150:
                raise ValueError("Age must be between 0 and 150")

        except ValueError as e:
            print("Invalid input. Please enter a valid age.")
            logging.error(f"Age input error: {e}")

        else:
            print(f"In 10 years you will be {age + 10}")
            break

        finally:
            print("Age input attempt completed.")

"""
Program 2 — Safe Division Calculator
Exceptions caught: ValueError, ZeroDivisionError
Recovery: User informed of invalid number or zero division.
User message: "Please enter valid numbers"
Internal logging: Division errors written to errors.log
"""

def safe_division_calculator():
    logging.basicConfig(filename="errors.log", level=logging.ERROR)

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")

    except ValueError:
        print("Please enter valid numbers.")
        logging.error("User entered invalid numeric value")

    except ZeroDivisionError as e:
        print(e)
        logging.error(f"Division error: {e}")

    else:
        result = num1 / num2
        print("Result:", result)

    finally:
        print("Division operation finished.")

"""
Program 3 — List Index Access
Exceptions caught: ValueError, IndexError
Recovery: User informed index is invalid.
User message: "Index out of range"
"""

def list_index_access():
    numbers = [10, 20, 30, 40]

    try:
        index = int(input("Enter index: "))

        if index < 0:
            raise ValueError("Index cannot be negative")

    except ValueError as e:
        print("Invalid index:", e)

    except IndexError:
        print("Index out of range.")

    else:
        print("Value:", numbers[index])

    finally:
        print("Index operation complete.")

if __name__ == "__main__":
    print("Part A PM loaded. Functions: safe_age_calculator, safe_division_calculator, list_index_access")
