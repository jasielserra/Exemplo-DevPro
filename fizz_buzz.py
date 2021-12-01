
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
        resultado = ''
        if i % 2 == 0:
           resultado = 'fizz'
        if i % 3 == 0:
            resultado += 'buzz'
        print(resultado if resultado !='' else i)