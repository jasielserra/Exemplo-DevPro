def contar_caracteres(s):
    """
    Função que conta os carecteres de uma string

    Ex:
    >>> contar_caracteres('jasiel')
    {'a': 1, 'e': 1, 'i': 1, 'j': 1, 'l': 1, 's': 1}
    >>> contar_caracteres('banana')
    {'a': 3, 'b': 1, 'n': 2}

    :param s: string a ser contada

    """
    resultado = {}

    for caracter in s:
        contagem = resultado.get(caracter, 0)
        contagem += 1
        resultado[caracter] = contagem

    return resultado

if __name__ == '__main__':
    print(contar_caracteres('jasiel'))
    print()
    print(contar_caracteres('banana'))