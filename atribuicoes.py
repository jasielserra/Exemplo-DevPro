row = 'Jasiel', 'Alagoinhas', 22.9, 43.1

def f(t):
    nome,*_ = t
    print(nome,_)

if __name__ == '__main__':
    f(row)
