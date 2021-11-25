#2.Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно)
start = int(input("Enter start year: "))
end = int(input("Enter end year: "))
if start <= end:
    leap_years = [str(x + start) for x in range(end-start) if x % 4 == 0 and x % 100 != 0]
    leap_years[-1] += "."
    print(f"Here is a list of leap years between {start} and {end}:\n{(','.join(leap_years))}")
else:
    print("Check your input years again!")