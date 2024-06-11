def two_largest(array):
    sort = sorted(array)
    largest = sort[-1]
    second_largest = sort[-2]
    return [largest, second_largest]


def another_largest(array):
    for large in range(len(array)):
        array.sort()
        largest = array[large - 1]
        secondLargest = array[large - 2]
        return [largest, secondLargest]


if __name__ == '__main__':
    age_of_boys = [100, 2, 4, 7, 8, 9, 23, 45, 36, 66, 77]
    h = "jjj"

    # print(two_largest(age_of_boys))
    print(another_largest(age_of_boys))
# for name in range(len(age_of_boys)):
