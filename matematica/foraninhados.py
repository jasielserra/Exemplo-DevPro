def imprimir_triangulo_de_numeros_crescentes(n: int):
    for linha in range(1, n + 1):
        for coluna in range(1, linha + 1):
            print(coluna, end= ' ')
        print('')

print("Triangulo")
imprimir_triangulo_de_numeros_crescentes(10)