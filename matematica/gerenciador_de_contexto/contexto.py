class Arquivo:
    def __enter__(self):
        print('Enter')
        return self



arquivo = Arquivo()

with arquivo:
    pass