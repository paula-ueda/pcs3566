class Pilha: 
    def __init__(self):
        self.pilha = []
    def push(self, estado_origem, estado_retorno):
        self.pilha.append(
            {
                "estado_origem": estado_origem,
                "estado_retorno": estado_retorno
            }
        )
    def pop(self):
        last_item = self.pilha[-1]
        del(self.pilha[-1])
        return last_item

    def vazia(self):
        if self.pilha:
            return True
        else:
            return False