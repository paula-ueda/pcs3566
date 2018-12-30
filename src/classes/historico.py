class Historico():
    def __init__(self):
        self.lista = []

    def coloca(self, estado_origem, transicao_index):
        self.lista.append(
            {
                "estado_origem": estado_origem,
                "transicao_index": transicao_index
            }
        )
    
    def tira():
        if self.lista:
            acontecimento = self.lista[-1]
            del(self.lista[-1])
            return acontecimento
        else:
            return None