class Transicao:
    def __init__(self, tipo, estado_inicial, estado_final, token=None, submaquina=None):
        self.tipo = tipo
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.token = token
        self.submaquina = submaquina