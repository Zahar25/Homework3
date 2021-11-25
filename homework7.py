#7. Калькулятор
def calc (a, b, c):
    if c == "+":
        return a + b
    elif c == "-":
        return a - b
    elif c == "*":
        return a * b
    elif c == "/":
        return a / b
    else:
        return "Unexpected operation! "
result = calc(int(input("First number: ")), int(input("Second number: ")), (input("Enter operation: ")))
print ("Result", result)