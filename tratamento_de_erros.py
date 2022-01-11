_usuarios = {'jasielserra@gmail.com': 'Jasiel Serra'}

def procurar_usuario_no_banco(email: str) -> str:
    return _usuarios[email]

if __name__ == '__main__':
    print(procurar_usuario_no_banco('jasielserra@gmail.com'))
    print(procurar_usuario_no_banco('pedroserra@gmail.com'))