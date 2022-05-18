def calc (number1, number2, operation):
    print(number1, number2, operation)
    if operation == "*":
        return number1 * number2
    if operation == "/":
        if number2 != 0:
            return number1 / number2

        else:
            print ("на ноль делить нельзя")
            return (print("введите другое число"))
    if operation == "//":
        if number2 != 0:
            return number1 // number2

        else:
            print ("на ноль делить нельзя")
            return (print("введите другое число"))
    if operation == "%":
        return number1 % number2

result = calc(15, 7, "%")
print(result)