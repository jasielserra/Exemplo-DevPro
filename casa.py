"""
Forma de implementação de uma lista como atributo de classe que recebe um tipo especifico.
Aqui temos uma classe Casa e uma classe Eletrodoméstico. Dentro dessa casa tenho uma lista  de
eletrodomésticos. Quando utilizar a classe Casa vou pegar os eletrodomésticos e quero que cada
eletrodoméstico execute uma operaçção comum, por exemplo, chamo o método ligar eletrodoméstico.
Colocar os tipos que são esperados em cada entrada/saida. Isso não seria mais eficiente?
"""
from typing import List


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

class Aspirador(Eletrodomestico):
    def ligar(self):
        """
        Este método liga um aspirador retorna uma string
        :return:
        """
        return 'Ligando Aspirador'

class Casa:
    def __init__(self):
        self._eletrodomesticos: List[Eletrodomestico] = []

    def adicionar_eletrodomesticos(self, eletrodomestico: Eletrodomestico):
        self._eletrodomesticos.append(eletrodomestico)

    def ligar_todos_eletrodomesticos(self) -> str:
        return ' => '.join(eletro.ligar() for eletro in self._eletrodomesticos)

if __name__ == '__main__':
    liquidificador = Liquidificador()
    resultado_liquidificador_ligado = Liquidificador().ligar()

    casa = Casa()

    casa.adicionar_eletrodomesticos(liquidificador)
    casa.adicionar_eletrodomesticos(Aspirador())
    print(casa.ligar_todos_eletrodomesticos())