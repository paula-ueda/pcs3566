class Estado:
    def __init__(self, maquina, estado):
        self.maquina = maquina
        self.estado = estado
    
    def stringfy(self):
        return f"({self.maquina}, {self.estado})"