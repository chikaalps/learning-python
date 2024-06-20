from functools import reduce


def add_drugs(a, b):
    return a + b


def add_two_numbers(x, y, z):
    sums = x + y + z
    return sums / 3


inventory_of_drugs = [40, 41, 44, 10, 21, 25, 26]
drugs_count = reduce(add_drugs, inventory_of_drugs)
print(drugs_count)

print("added", add_two_numbers(2, 4,8))
