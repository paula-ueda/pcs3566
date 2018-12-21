class Evento:
    def __init__(self, metodo, arg=None, filename=None, file=None, linha=None,
                 numero_linha=None, lista=None, linha_analisada=[], texto_analisado=[]):
        self.metodo = metodo
        self.arg = arg
        self.filename = filename
        self.file = file
        self.linha = linha
        self.numero_linha = numero_linha
        self.lista = lista
        self.linha_analisada = linha_analisada
        self.texto_analisado = texto_analisado
    def get_params(self):
        params = {}
        if self.filename:
            params["filename"] = self.filename
            
        if self.file:
            params["file"] = self.file
            
        if self.linha:
            params["linha"] = self.linha
            
        if self.numero_linha is not None:
            params["numero_linha"] = self.numero_linha
        
        if self.lista:
            params["lista"] = self.lista
            
        if self.linha_analisada:
            params["linha_analisada"] = self.linha_analisada
            
        if self.texto_analisado:
            params["texto_analisado"] = self.texto_analisado
             
        return params