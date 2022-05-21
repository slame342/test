num1 = float(input('введите первое число: '))
num2 = float(input('введите второе число: '))

what = input("выберите действие : (+,-,*,/)")

if what == "+":
    num = num1 + num2
if what == "-":
    num = num1 - num2
if what == "*":
    num = num1 * num2
if what == "/":
    if num2 != 0:
        num = num1 / num2
    else:
        print("Вы ввели 0 !")
        print("Введите другое число!")
print("результат : " + str(num))






