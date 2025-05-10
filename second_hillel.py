number: int = 13578

num_1 = number // 1000
num_2 = (number // 100) % 10
num_3 = (number // 10) % 10
num_4 = number % 10

print(num_1)
print(num_2)
print(num_4)
print(num_4)


print("\n")

# Виконуємо реверс
number: int = 37568

digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

reversed_number = digit5 * 10000 + digit4 * 1000 + digit3 * 100 + digit2 * 10 + digit1

print(reversed_number)





