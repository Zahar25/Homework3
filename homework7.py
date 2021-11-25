#7. Калькулятор
while True:
    s = input("Enter operation (+, -, , /): ")
    if s == '0':
        break
    if s in ('+', '-', '', '/'):
        x = float(input("First number = "))
        y = float(input("Second number = "))
        if s == '+':
            print("%.2f" % (x + y))
        elif s == '-':
            print("%.2f" % (x - y))
        elif s == '*':
            print("%.2f" % (x * y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x / y))
            else:
                print(False)
    else:
        print("Wrong")