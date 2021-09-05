class CirculoPerfeito:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def mostra_cor(self):
        return self.cor

    def trocar_cor(self, cor):
        self.cor = cor

circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()
circulo_segundo.trocar_cor('Amarelo')

print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)
print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
print(id(circulo_segundo), circulo_segundo.mostra_cor())
print(circulo_primeiro.cor, circulo_segundo.cor)

class Quadrado:
    def __init__(self, lado = 1):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

quadrado = Quadrado(4)
print(quadrado.lado, quadrado.calcular_area())