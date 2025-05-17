examples = [
    [0, 1, 7, 2, 4, 8],
    [1, 3, 5],
    [6],
    []
]

for numbers in examples:
    if len(numbers) == 0:
        result = 0
    else:
        sum_index = 0
        for i in range(0, len(numbers), 2):
            sum_index += numbers[i]
        result = sum_index * numbers[-1]

    print(f"{numbers} => {result}")
