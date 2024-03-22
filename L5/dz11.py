yes = "Y"
no = "no"
answer = input("Починаємо?")
while answer == yes:
    x = int(input('Введіть 1 число: '))
    math_operation = input('Введіть операції: ')
    y = int(input('Введіть 2 число: '))
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
    answer = input("Продовжити?")
else:
    print('End')