from automatos_payload import payload
from pilha import *
from estado import *
from historico import *



class Automato():
    def __init__(self, estado_atual, lista_tokens):
        self.pilha = Pilha()
        self.lista_tokens = lista_tokens
        self.lista_lidos = []
        self.historico = Historico()
        self.estado = Estado("program", 0)
        self.transicao_index = 0

    def set_estado(self, estado, transicao=0):
        self.numero_estado = estado.estado
        self.maquina = payload[estado.maquina]
        self.transicao = transicao

    def get_transicoes(self):
        return self.maquina["transicoes"][self.estado.estado]

    def aceitou(self):
        if lista_tokens:
            if self.pilha.vazia():
                return True
            else:
                return False
        else:
            if self.pilha.vazia():
                return False
            else:
                return None

    def transiciona(self):
        sucesso = True
        # verifica se há transicoes possiveis nesse estado
        transicoes = self.get_transicoes()
        if len(transicoes) > transicao_index:
            transicao = transicoes[transicao_index]
            if transicao.tipo == "consome_token":
                tipo, valor = transicao.token
                if tipo:
                    if valor == lista_tokens[0].nome:
                        # coloca no historico
                        self.historico.coloca(self.estado, transicao_index)
                        # consome token da lista de tokens e poe na lista de lidos
                        self.lista_lidos.append(self.lista_tokens.pop_front())
                        #  faz transicao
                        self.transicao_index = 0
                        self.estado = transicao.estado_final
                        
                    else:
                        # atualiza transicao_index
                        self.transicao_index += 1
                else:
                    if valor == lista_tokens[0].tipo:
                        # coloca no historico
                        self.historico.coloca(self.estado, transicao_index)
                        # consome token da lista de tokens e poe na lista de lidos
                        self.lista_lidos.append(self.lista_tokens.pop_front())
                        #  faz transicao
                        self.transicao_index = 0
                        self.estado = transicao.estado_final
                    else:
                        # atualiza transicao_index
                        self.transicao_index += 1


            elif transicao.tipo == "entra_submaquina":
                # coloca na pilha
                self.pilha.push(transicao.estado_inicial, transicao.estado_final)
                # coloca no historico
                self.historico.coloca(self.estado, transicao_index)
                # faz transicao
                # coloca no estado um novo estado no automato destino
                self.estado = Estado(transicao.submaquina, 0)
                # poe index = 0
                self.transicao_index = 0

            elif transicao.tipo == "sai_submaquina":
                # desempilha
                item_pilha = self.pilha.pop()
                # poe no historico
                self.historico.coloca(self.estado, transicao_index)
                # faz transicao
                # atualiza estado
                self.estado = item_pilha["estado_retorno"]
                # poe index
                self.transicao_index = 0
    
        else:
            # tira do historico
            item_historico = self.historico.tira()
            if item_historico:
                # volta para estado anterior
                self.estado = item_historico["estado_origem"]
                # atualiza index 
                self.transicao_index = item_historico["transicao_index"] + 1
            else:
                sucesso = False

        return sucesso
