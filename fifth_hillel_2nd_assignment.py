while True:
    num1 = float(input("Перше число: "))
    operation = input("Операція (+, -, *, /): ")
    num2 = float(input("Друге число: "))

    match operation:
        case '+':
            result = num1 + num2
            print(f"Результат: {num1} + {num2} = {result}")
        case '-':
            result = num1 - num2
            print(f"Результат: {num1} - {num2} = {result}")
        case '*':
            result = num1 * num2
            print(f"Результат: {num1} * {num2} = {result}")
        case '/':
            if num2 == 0:
                print("Помилка: Ділення на 0 неможливе!")
            else:
                result = num1 / num2
                print(f"Результат: {num1} / {num2} = {result}")
        case _:
            print("Помилка: невідома операція!")

    answer = input("Ще одне обчислення? (yes/y для продовження): ").lower()
    if answer not in ('yes', 'y'):
        print("Роботу калькулятора завершено.")
        break



