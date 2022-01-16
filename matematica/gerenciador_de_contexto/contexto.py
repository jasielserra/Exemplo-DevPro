'''
Gerenciador de contexto é um objeto que possui o metodo __enter__
e __exit__.
'''
from contextlib import contextmanager
from typing import Callable


def contextmanager(chamavel: Callable):
    gerador = chamavel()

    class GerenciadorDeContexto:
        def __enter__(self):
            return next(gerador)

        def __exit__(self, exc_type, exc_val, exc_tb):
            print('Saída')

    return GerenciadorDeContexto


@contextmanager
def Arquivo():
    print(f'Enter: ')
    yield 'foo'
    print('Saída')



with Arquivo() as arquivo: # Contruindo um objeto do tipo arquivo chamando o metodo __enter__ e retornando.
    #raise Exception
    print(arquivo)
    print(id(arquivo))