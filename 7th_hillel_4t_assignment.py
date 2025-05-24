def common_elements():
    multiples_of_3 = set(range(0, 100, 3))
    multiples_of_5 = set(range(0, 100, 5))
    return multiples_of_3 & multiples_of_5

assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print("ОК")
