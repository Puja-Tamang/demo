import art
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

# Operation dictionary
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}

# Calculator function
def calculator():
    print(art.logo)
    num1 = int(input("Type the first number: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_choice = input("Pick an operation from the line above: ")
        num2 = int(input("Type the next number: "))
        function = operations[operation_choice]
        answer = function(num1, num2)

        print(f"{num1} {operation_choice} {num2} = {answer}")

        choice = input(f"Type 'y' to continue with {answer}, or 'n' to start a new calculation: ").lower()
        if choice == 'y':
            num1 = answer
        else:
            should_continue = False
            print("\n" * 3)
            calculator()  # start fresh

# Start the calculator
calculator()
