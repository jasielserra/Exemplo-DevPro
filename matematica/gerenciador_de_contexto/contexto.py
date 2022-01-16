'''
Gerenciador de contexto é um objeto que possui o metodo __enter__
e __exit__.
'''
from contextlib import contextmanager


@contextmanager
def Arquivo():
    print(f'Enter: ')
    return 'foo'
    print('Saída')



with Arquivo() as arquivo: # Contruindo um objeto do tipo arquivo chamando o metodo __enter__ e retornando.
    #raise Exception
    print(id(arquivo))