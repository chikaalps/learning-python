import math


def side_a_side_b(side_a, side_b):
    multiply_sides = (side_a ** 2) + (side_b ** 2)
    return multiply_sides


def hypotenuse(side_a, side_b):
    side_1 = math.pow(side_a, 2)
    side_2 = math.pow(side_b, 2)
    sum_of_side = side_1 + side_2
    hypo = math.sqrt(sum_of_side)
    return hypo


def temperature_conversion():
    temp = float(input("please enter a tempreture to convert to"))
    choice = int(input("press 1 for conversion to kelvin and 2 for celsius"))
    if choice == 1:
        return "Your temp in kelvin is -->", temp + 273.15
    else:
        return "Your temp in celsius is -->", temp - 273.15


def sum_of_digits():
    a, b, c, d = input("please enter a four digit number").split(",  "
                                                                 
                                                                 "  ")
    sum_of = int(a) + int(b) + int(c) + int(d)
    return sum_of


if __name__ == '__main__':
    print(sum_of_digits())
    # print(temperature_conversion())
    # Multiply_sides = side_a_side_b(3, 4)
    # print(Multiply_sides)
    # print("The hypotenuse is ", hypotenuse(3, 4))
