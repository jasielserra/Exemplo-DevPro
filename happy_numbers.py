def sum_of_squares(number):
    digits = [int(char) ** 2 for char in str(number)]
    return sum(digits)


def happy(number):
    box = []
    n = number
    while n != 1 and n not in box:
        box.append(n)
        n = sum_of_squares(n)
    return n == 1


assert sum_of_squares(130) == 10
assert all(happy(n) for n in (1, 10, 100, 130, 97))
assert not all(happy(n) for n in (2, 3, 4, 5, 6, 7, 8, 9))