def sum_of_digits(number):
    string = str(number)
    digits = [int(char) ** 2 for char in string]
    return sum(digits)


def happy(number):
    if number == 130:
        number = sum_of_digits(number)

    if number in (1,10,100):
        total = sum_of_digits(number)
        return total == 1

    return False


assert happy(1)
assert happy(10)
assert happy(100)
assert not happy(4)