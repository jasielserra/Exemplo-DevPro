_usuarios = {'jasielserra@gmail.com': 'Jasiel Serra'}

class BancoDeDadosException(Exception):
    pass

class UsuarioNaoEncontrado(BancoDeDadosException):
    pass

class EmailInvalido(BancoDeDadosException):
    def __init__(self, msg_de_erro: str, email:str) -> None:
        super().__init__()
        self.email = email
        self.msg_de_erro = msg_de_erro


def procurar_usuario_no_banco(email: str) -> str:
    if '@' not in email:
        raise EmailInvalido('Email inválido, faltando caracter "@"', email)
    try:
        return _usuarios[email]
    except KeyError as e:
        print('Deu ruim no banco')
        raise UsuarioNaoEncontrado() from e


def enviar_email_de_boas_vindas(email: str) -> None:
    try:
        usuario = procurar_usuario_no_banco(email)
    except EmailInvalido as e:
        print(f'Informar usuária para corrigir email. Razão do erro: {e.msg_de_erro}')
    except UsuarioNaoEncontrado as e:
        print('Usuário não encontrado')
    else:
        print(f'Enviando email para: {email}')
        print(f'Mensagem para {usuario}')


if __name__ == '__main__':
    enviar_email_de_boas_vindas('jasielserra@gmail.com')
    enviar_email_de_boas_vindas('pedroserra')
    enviar_email_de_boas_vindas('carlospiton@hotmail.com')