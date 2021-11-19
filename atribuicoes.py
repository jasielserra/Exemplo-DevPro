table = (('Jasiel', 'Alagoinhas', 22.9, 43.1),
         ('Vinícius', 'Santarém', 2.3, 54.7))



for row in table:
    nome, cidade, lat, long = row
    print(nome, cidade, lat, long)