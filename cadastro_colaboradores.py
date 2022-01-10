"""
Utilizando o conceito de dicionários, faça uma ficha de cadastro de 4 funcionários utilizando a seguinte estrutura:
Chave: Nome Dados: Idade, email, setor, salario
inclua os funcionários:

João Pereira, 25, joao.pereira@hurb.com, marketing, 1950
Maria Silva, 23, maria.silva@hurb.com, comercial, 2300
Pedro Peixoto, 32, pedro.peixoto@hurb.com, operacao, 2625
Luiza Almeida, 28, luiza.almeida@hurb.com, atendimento, 2120
Faça um programa que retorna o nome, email e setor de todos os funcionários com de 25 anos
"""
import unittest

class TesteColaboradores(unittest.TestCase):
    def test_filtragem_colaboradores(self) -> None:
        self.assertFalse(True)
     #   self.colaboradores = {
     #       'joao pereira': [25, 'joao.pereira@hurb.com', 'marketing', 1950],
     #       'Maria Silva' : [23, 'maria.silva@hurb.com', 'comercial', 2300],
     #       'Pedro Peixoto' : [32, 'pedro.peixoto@hurb.com', 'operacao', 2625],
     #       'Luiza Almeida' : [28, 'luiza.almeida@hurb.com', 'atendimento', 2120],
     #   }