# Розділити один список на два списки

# Перший список
lst = [1, 2, 3, 4, 5, 6]
length = len(lst)
if length % 2 == 0:
    middle = length // 2
else:
    middle = (length // 2) + 1
first_half = lst[:middle]
second_half = lst[middle:]
result = [first_half, second_half]
print(result)

# Другий список
lst = [1, 2, 3]
length = len(lst)
if length % 2 == 0:
    middle = length // 2
else:
    middle = (length // 2) + 1
first_half = lst[:middle]
second_half = lst[middle:]
result = [first_half, second_half]
print(result)

# Третій список
lst = [1, 2, 3, 4, 5]
length = len(lst)
if length % 2 == 0:
    middle = length // 2
else:
    middle = (length // 2) + 1
first_half = lst[:middle]
second_half = lst[middle:]
result = [first_half, second_half]
print(result)

# Четвертий список
lst = [1]
length = len(lst)
if length % 2 == 0:
    middle = length // 2
else:
    middle = (length // 2) + 1
first_half = lst[:middle]
second_half = lst[middle:]
result = [first_half, second_half]
print(result)

# П’ятий список
lst = []
length = len(lst)
if length % 2 == 0:
    middle = length // 2
else:
    middle = (length // 2) + 1
first_half = lst[:middle]
second_half = lst[middle:]
result = [first_half, second_half]
print(result)


