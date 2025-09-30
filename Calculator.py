import art_calculator.py
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
    should_accumulate = True
    print(art_calculator.logo)
    num1 = int(input("What's the first digit? "))
    while should_accumulate:
        for symbol in operations:
            print(symbol)
        symbol = input("Chose mathematical operator ")
        num2 = int(input("What's the second digit? "))
        answear = operations[symbol](num1,num2)
        print(f"{num1}{symbol}{num2} = {answear}")

        choice = input(f"Do you want to continue 'y' for yes, 'n' for no:".lower())
        if choice == "y":
            num1 = answear
        else:
            should_accumulate = False
            print("\n" * 25)
            calculator()

calculator()
