#4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат. Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
def func():
    def info(name):
        print ("Your name is: ", name)
        return name
    info (name = input("Enter your name: "))
    def info_2 (age):
        print("Your age is: ", age)
        return age
    info_2(age=input("How old are you?: "))
    def info_3 (city):
        print("You live in: ", city)
        return (city)
    info_3(city = input("Where do you live?: "))
func()