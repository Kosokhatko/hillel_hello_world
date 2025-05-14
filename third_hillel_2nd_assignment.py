# Перемістити елемент у списку

# Перший список
lst = [12, 3, 4, 10]
if len(lst) <= 1:
    result = lst
else:
    result = [lst[-1]] + lst[:-1]
print(result)

# Другий список
lst = [1]
if len(lst) <= 1:
    result = lst
else:
    result = [lst[-1]] + lst[:-1]
print(result)

# Третій список
lst = []
if len(lst) <= 1:
    result = lst
else:
    result = [lst[-1]] + lst[:-1]
print(result)

# Четвертий список
lst = [12, 3, 4, 10, 8]
if len(lst) <= 1:
    result = lst
else:
    result = [lst[-1]] + lst[:-1]
print(result)
