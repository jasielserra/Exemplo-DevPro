_usuarios = {'jasielserra@gmail.com': 'Jasiel Serra'}

def procurar_usuario_no_banco(email: str) -> str:
    try:
        return _usuarios[email]
    except KeyError as e:
        print('Deu ruim no banco')
        raise e


def enviar_email_de_boas_vindas(email: str) -> None:
    try:
        usuario = procurar_usuario_no_banco(email)
    except KeyError:
        print('Não enviado o email porque usuário não foi encontrado')
    else:
        print(f'Enviando email para: {email}')
        print(f'Mensagem para {usuario}')


if __name__ == '__main__':
    enviar_email_de_boas_vindas('jasielserra@gmail.com')
    enviar_email_de_boas_vindas('pedroserra@gmail.com')