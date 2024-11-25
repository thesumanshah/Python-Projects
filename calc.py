import calcart
print(calcart.logo)
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

values={"+":add,
        "-":subtract,
        "*":multiply,
        "/":divide,}

num1 = float(input("Enter first number: "))

continue_program=True
while continue_program:
    for key in values:
        print(key)
    operation = input("Enter operation: ")

    num2 = float(input("Enter second number: "))
    final=values[operation](num1, num2)
    print(f"{num1} + {num2} = {final}")
    cont=input("Do you want to continue? with the given result y or new calculation for n").lower()
    if cont=="y":
        num1=final
    else:
        continue_program=False