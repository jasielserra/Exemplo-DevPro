'''
Gerenciador de contexto é um objeto que possui o metodo __enter__
e __exit__.
'''


class Arquivo:
    def __enter__(self):
        print(f'Enter: {id(self)}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Saida', exc_type, exc_val,exc_tb)





with Arquivo() as arquivo: # Contruindo um objeto do tipo arquivo chamando o metodo __enter__ e retornando.
    #raise Exception
    print(id(arquivo))