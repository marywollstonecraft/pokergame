import random

class Cartas(object):
    def __init__(self, valor, naipe):
        self.valor = valor
        self.naipe = naipe
        #self.showing = True
        
    def __repr__(self): # representação das cartas
        nome_valor = ""
        nome_naipe = ""
        if self.valor == 0:
            nome_valor = "Dois"
        elif self.valor == 1:
            nome_valor = "Três"
        elif self.valor == 2:
            nome_valor = "Quatro"
        elif self.valor == 3:
            nome_valor = "Cinco"
        elif self.valor == 4:
            nome_valor = "Seis"
        elif self.valor == 5:
            nome_valor = "Sete"
        elif self.valor == 6:
            nome_valor = "Oito"
        elif self.valor == 7:
            nome_valor = "Nove"
        elif self.valor == 8:
            nome_valor = "Dez"
        elif self.valor == 9:
            nome_valor = "Valete"
        elif self.valor == 10:
            nome_valor = "Rainha"
        elif self.valor == 11:
            nome_valor = "Rei"
        elif self.valor == 12:
            nome_valor = "Ás"
        if self.naipe == 0:
            nome_naipe = "Paus"
        elif self.naipe == 1:
            nome_naipe = "Ouro"
        elif self.naipe == 2:
            nome_naipe = "Copas"
        elif self.naipe == 3:
            nome_naipe = "Espadas"
        return nome_valor + " de " + nome_naipe


class Baralho(list):
    def __init__(self):
        super().__init__()
        naipes = list(range(4))
        valores = list(range(13))
        [[self.append(Cartas(i, j)) for j in naipes] for i in valores]
        
    def shuffle(self):
        random.shuffle(self)
        print("baralho embaralhado :)")

    def distribuir(self):
        print(self.pop(0))

deck = Baralho()