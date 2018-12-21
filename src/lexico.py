import queue
from evento import Evento
from linha_tokens import Linha_tokens
from lexico_utils import *


def leitura(queue_leitura, queue_linha, queue_lista):
    response = None
    if not queue_leitura.empty():
        evento = queue_leitura.get()
        params = evento.get_params()
        if evento.metodo == None:
            params["filename"] = evento.arg
            novo_evento = Evento("abrir", **params)
            queue_leitura.put(novo_evento)
        elif evento.metodo == "abrir":
            file = open(evento.filename, "r")
            novo_evento = Evento("primeira", file=file, **params)
            queue_leitura.put(novo_evento)
        elif evento.metodo == "primeira":
            params["numero_linha"] = 1
            novo_evento = Evento("ler", **params)
            queue_leitura.put(novo_evento)
        elif evento.metodo == "ler":
            linha = evento.file.readline()
            
            if not linha:
                linha = None
                novo_evento = Evento("fim", **params)
                queue_leitura.put(novo_evento)
            else:
                params["linha"] = linha
                novo_evento = Evento(None, **params)
                queue_linha.put(novo_evento)

        elif evento.metodo == "proxima":
            if "texto_analisado" not in params:
                params["texto_analisado"] = []
            
            params["texto_analisado"].append(Linha_tokens(evento.numero_linha, evento.linha_analisada))
            params["linha_analisada"] = []
            params["linha"] = None
            params["numero_linha"] += 1
            novo_evento = Evento("ler", **params)
            queue_leitura.put(novo_evento)
        elif evento.metodo == "fim":
            response = evento.texto_analisado
        else:
            raise Exception ("Evento estranho")
    return queue_leitura, queue_linha, queue_lista, response


def analisa_linha(queue_leitura, queue_linha, queue_lista):
    if not queue_linha.empty():
        evento = queue_linha.get()
        params = evento.get_params()
        if evento.metodo == None:
            novo_evento = Evento("quebrar", **params)
            queue_linha.put(novo_evento)
        elif evento.metodo == "quebrar":
            params["linha"] = str(evento.linha)
            lista = quebrar(evento.linha)
            params["lista"] = lista
            novo_evento = Evento(None, **params)
            queue_lista.put(novo_evento)
        elif evento.metodo == "fim":
            novo_evento = Evento("proxima", **params)
            queue_leitura.put(novo_evento)
    return queue_leitura, queue_linha, queue_lista

def analisa_lista(queue_leitura, queue_linha, queue_lista):
    if not queue_lista.empty():
        evento = queue_lista.get()
        params = evento.get_params()
        if evento.metodo == None:
            params["linha_analisada"] = []
            params["linha"] = (evento.linha)
            novo_evento = Evento("primeira", **params)
            queue_lista.put(novo_evento)
        elif evento.metodo == "primeira":
            string = evento.lista[0]
            del(evento.lista[0])
            novo_evento = Evento("classificar", arg=string,**params)
            queue_lista.put(novo_evento)
        elif evento.metodo == "classificar":
            token = classificar(evento.arg)
            if "linha_analisada" not in params:
                params["linha_analisada"] = []
            params["linha_analisada"]+=(token)
            novo_evento = Evento("proxima", **params)
            queue_lista.put(novo_evento)
        elif evento.metodo == "proxima":
            if not evento.lista or len(evento.lista) == 0:
                novo_evento = Evento("fim",**params)
                queue_lista.put(novo_evento)
            else:
                string = evento.lista[0]
                del(evento.lista[0])
                novo_evento = Evento("classificar", arg=string,**params)
                queue_lista.put(novo_evento)
        elif evento.metodo == "fim":
            params["lista"] = None
            novo_evento = Evento("fim", **params)
            queue_linha.put(novo_evento)
        return queue_leitura, queue_linha, queue_lista

def analise_lexica():
    queue_leitura = queue.Queue()
    queue_linha = queue.Queue()
    queue_lista = queue.Queue()
    
    #path = input("Digite o endereço do arquivo: ")
    path = "/home/paula/paula/poli/doing/compiladores/projeto/programa.bas"
    novo_evento = Evento(None, arg=path)
    queue_leitura.put(novo_evento)
    while (True):
        if not queue_lista.empty():
            queue_leitura, queue_linha, queue_lista = analisa_lista(queue_leitura, queue_linha, queue_lista)
        elif not queue_linha.empty():
            queue_leitura, queue_linha, queue_lista = analisa_linha(queue_leitura, queue_linha, queue_lista)
        elif not queue_leitura.empty():
            queue_leitura, queue_linha, queue_lista, response = leitura(queue_leitura, queue_linha, queue_lista)
        else:
            return response
    