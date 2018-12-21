from sinais import sinais
from reservadas import reservadas


class Token:
    def __init__(self, tipo, nome):
        if (
            tipo in sinais or
            tipo in reservadas or
            tipo == "identificador" or
            tipo == "numero" or
            tipo == "string"
        ):
            self.tipo = tipo
            self.nome = nome
        else:
            raise Exception(f"Valor de tipo ({tipo}) incorreto")