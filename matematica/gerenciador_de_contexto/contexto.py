class Arquivo:
    def __enter__(self):
        print(f'Enter: {id(self)}')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



arquivo = Arquivo()

with Arquivo() as arquivo:
    print(id(arquivo))