class Arquivo:
    def __enter__(self):
        print('Enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



arquivo = Arquivo()

with arquivo:
    pass