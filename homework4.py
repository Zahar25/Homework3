#4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
def func():
    def info(name, age, city):
        print ("Your name is: ", name)
        print("Your age is: ", age)
        print("You live in: ", city)
        return name
        return age
        return city
    info(name = input(), age=input(), city = input())
func()