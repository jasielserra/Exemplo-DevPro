try:
    arquivo = open('a.txt', 'r', encoding='utf8')

    for linha in arquivo:
        raise Exception()
        print(linha)
    print('Fechado')
finally:
    arquivo.close()