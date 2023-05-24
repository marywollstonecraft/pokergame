class Jogador(object):
    def __init__(self, nome=None):
            self.name = name
            self.chips = 0
            self.aposta = 0
            self.aposta_gap = 0
            self.cartas = []
            self.score = []
            self.desistir = False
            self.prosseguir = False
            self.all_in = False
            self.lista_atributos_assigned = []
            self.win = False 
    def __repr__(self):
        name = self.name
        return name