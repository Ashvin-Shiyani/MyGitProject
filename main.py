from validator import validate_input
from operations import calculate

def main():
    print("Simple Calculator (type 'quit' to exit)")

    while True:
        user_input = input("Enter expression (e.g., 5 + 3): ")

        if user_input.lower() == "quit":
            break

        valid, result = validate_input(user_input)

        if not valid:
            print("Invalid input:", result)
            continue

        a, op, b = result
        output = calculate(a, op, b)
        print("Result:", output)

if __name__ == "__main__":
    main()
