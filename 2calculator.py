def add(n1, n2):
    return n1 + n2


def divide(n1, n2):
    if n2 == 0:
        return "num2 mustn't be 0 "
    else:
        return n1 / n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


function_dict = \
    {
        "+": add,
        "-": subtract,
        "/": divide,
        "*": multiply
    }
control = True


def calculator():
    global control
    num1 = float(input("What's the first number?"))
    for i in function_dict.keys():
        print(i)
    while control:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the next number?"))
        calculation_function = function_dict[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        response = input(
            f"Type 'y' to continue calculating with {answer} ,type 'n' to exit or  to enter a new operation press o:")
        if response == "y":
            num1 = answer
        elif response == "o":
            calculator()
        else:
            print("program is finishing...")
            control = False


calculator()
