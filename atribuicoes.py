row = 'Jasiel', 'Alagoinhas', 22.9, 43.1

def f(t):
    nome,*meio, long = t
    print(nome, long, meio)

if __name__ == '__main__':
    f(row)
