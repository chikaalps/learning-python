name_of_boys = ["emeka", "john", "abel"]
# name_of_girls = ["emilia", "ada", "rose", "felicia"]
# name_of_boys.append(name_of_girls)
# print(name_of_boys)
even_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

name = [print(m.upper()) for m in name_of_boys]


even_numbers = [x for x in even_number if x % 2 == 0]
print(even_numbers)

odd_numbers = [x for x in even_number if x % 2 != 0]
print(odd_numbers)