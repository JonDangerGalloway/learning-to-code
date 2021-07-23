def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    num1 = float(input("\nWhat is the first number? "))
    for symbol in operations:
        print(symbol)
    another = True
    while another:
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        again = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ").lower()
        if again == "y":
            num1 = answer
        else:
            another = False
            calculator()

calculator()
