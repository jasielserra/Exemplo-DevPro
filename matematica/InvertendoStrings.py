nome = 'Jasiel de Cristo Serra'.upper()

nome_invertido_por_letras = ''.join(reversed(nome))

nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome com letras em maiúsculo: {nome}')
print(f'Nome com letras em maiúsculo invertido por letras: {nome_invertido_por_letras}')
print(f'Nome com letras em maisúculo invertido por palavras: {nome_invertido_por_palavras}')