from safe_tools import safe_number

def main():
    print("Enter numbers to add. Type 'quit' to stop.")
    total = 0

    while True:
        user_input = input("Number: ")
        if user_input.lower() == "quit":
            break

        value = safe_number(user_input)
        if value == "Not a number":
            print("That was not a valid number, try again.")
            continue

        total += value
        print(f"Running total: {total}")

    print(f"Final total: {total}")

if __name__ == "__main__":
    main()