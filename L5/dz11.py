while True:
    x = int(input('Введіть перше число: '))
    math_operation = input('Введіть операцію: ')
    y = int(input('Введіть друге число: '))

    if math_operation == '+':
        result = x + y
        print("Результат:", result)
    elif math_operation == '-':
        result = x - y
        print("Результат:", result)
    elif math_operation == '*':
        result = x * y
        print("Результат:", result)
    elif math_operation == '/':
        if y == 0:
            print("Ділення на 0 неможливе!")
        else:
            result = x / y
            print("Результат:", result)

    proceed = input("Бажаєте продовжити (yes/no)? ")
    if proceed != 'yes':
        break
