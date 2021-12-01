from collections import Counter


def contar_letras(s: str):
    '''
    >>> contar_letras('renzo')
    {'r': 1, 'e': 1, 'n': 1, 'z': 1, 'o': 1}
    >>> contar_letras('Rrenzo')
    {'R': 1, 'r': 1, 'e': 1, 'n': 1, 'z': 1, 'o': 1}
    >>> contar_letras('banana')
    {'b': 1, 'a': 3, 'n': 2}

    :param s:
    :return:
    '''

    return dict(Counter(s))
