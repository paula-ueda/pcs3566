from tokens_lists import sinais, reservadas


class Token:
    def __init__(self, tipo, nome):
        if (
            tipo == "especial" or
            tipo in reservadas or
            tipo == "letra" or
            tipo == "digito"
        ):
            self.tipo = tipo
            self.nome = nome
        else:
            raise Exception(f"Valor de tipo ({tipo}) incorreto")