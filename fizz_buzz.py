
def fizz_buzz(n: int):
    '''
    >>> fizz_buzz(6)
    1
    fizz
    buzz
    fizz
    5
    fizzbuzz

    :param n:
    :return:
    '''

    for i in range(1,  n + 1):
        if i % 3 == 0 and i % 2 == 0:
            print('fizzbuzz')
        elif i % 2 == 0:
            print('fizz')
        elif i % 3 == 0:
            print('buzz')
        else:
            print(i) # 1 fizz 3 fizz 5 fizz