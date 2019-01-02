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
            return False
        else:
            return True
    
    def mostra(self):
        print("\nPILHA:")
        for item in self.pilha:
            if item != {"estado_origem": None, "estado_retorno": None}:
                print(
                    f"Origem: {item['estado_origem'].stringfy()} | "
                    f"Retorno: {item['estado_retorno'].stringfy()}"
                )
            else:
                print(
                    f"Origem: None | "
                    f"Retorno: None"
                )