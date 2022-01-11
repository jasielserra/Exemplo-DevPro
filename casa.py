"""
Forma de implementação de uma lista como atributo de classe que recebe um tipo especifico.
Aqui temos uma classe Casa e uma classe Eletrodoméstico. Dentro dessa casa tenho uma lista  de
eletrodomésticos. Quando utilizar a classe Casa vou pegar os eletrodomésticos e quero que cada
eletrodoméstico execute uma operaçção comum, por exemplo, chamo o método ligar eletrodoméstico.
Colocar os tipos que são esperados em cada entrada/saida. Isso não seria mais eficiente?
"""


class Eletrodomestico:
    def ligar(self):
        raise NotImplementedError()

class Liquidificador(Eletrodomestico):

    def ligar(self):
        """
        Este método liga um liquidificador retorna uma string
        :return: str
        """
        return 'Ligando liquidificador'

if __name__ == '__main__':
    resultado_liquidificador_ligado = Liquidificador().ligar()