#2.Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку (границі включно)
first_year = int(input("Year from: "))
second_year = int(input("To: "))
for year in range(first_year, second_year + 1):
    if year % 400 == 0:
        print("%d leap year" %year)
    elif year % 100 == 0:
            print("%d not leap" %year)
    elif year % 4 == 0:
            print("%d leap year" %year)
    else:
        print("%d not leap" %year)