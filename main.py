import logo

print(logo.logo)


# calculator


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide,
              }

should_continue = True

while should_continue is True:
    num1 = int(input("Whats your first number?"))
    for symbol in operations:
        print(symbol)
    operation_symbol = input("pick an operation from the line above")
    num2 = int(input("Whats your second number?"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)

    print(f"total {num1} {operation_symbol} {num2} = {answer}")
    warning = input("do you wanna go again? yes or no").lower()

    if warning == "no":
        should_continue = False
        print("have a nice day")