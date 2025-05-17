import random

length = random.randint(3, 10)
numbers = []
for i in range(length):
    numbers.append(random.randint(0, 10))

print("Початковий список:", numbers)

new_list = [numbers[0], numbers[2], numbers[-2]]

print("Новий список:", new_list)
