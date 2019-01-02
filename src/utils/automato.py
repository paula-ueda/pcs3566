from classes import *
from tokens_lists import *
from automato import payload

class Automato:
    def __init__(self, lista_tokens):
        self.pilha = Pilha()
        self.lista_tokens = lista_tokens
        self.lista_lidos = []
        self.historico = Historico()
        self.estado = Estado("program", 0)
        self.transicao_index = 0

    def mostra(self):
        print("--------------------------------------------")
        self.pilha.mostra()
        self.mostra_tokens("lista_tokens")
        self.mostra_tokens("lista_lidos")
        self.historico.mostra()
        self.mostra_estado()
        self.mostra_transicao_index()


    def mostra_estado(self):
        print("\nESTADO")
        print(self.estado.stringfy())

    def mostra_transicao_index(self):
        print("\nTRANSICAO INDEX")
        print(self.transicao_index)    


    def mostra_tokens(self, nome_lista):
        if nome_lista == "lista_tokens":
            print("\nLISTA TOKENS")
            lista = self.lista_tokens
        elif nome_lista == "lista_lidos":
            print("\nLISTA DE TOKENS LIDOS")
            lista = self.lista_lidos

        for item in lista:
            print(f"Tipo: {item.tipo} | Nome: {item.nome}")

    def get_transicoes(self):
        return payload[self.estado.maquina]["transicoes"][str(self.estado.estado)]

    def aceitou(self):
        if self.lista_tokens:
            if self.pilha.vazia():
                return False
            else:
                return None
        else:
            if self.pilha.vazia():
                return False
            else:
                return True

    def transiciona(self):
        continua = True
        # verifica se há transicoes possiveis nesse estado
        transicoes = self.get_transicoes()
        if len(transicoes) > self.transicao_index:
            transicao = transicoes[self.transicao_index]
            if transicao.tipo == "consome_token":
                tipo, valor = transicao.token
                if tipo:
                    if valor == self.lista_tokens[0].nome:
                        # coloca no historico
                        self.historico.coloca(self.estado, self.transicao_index)
                        # consome token da lista de tokens e poe na lista de lidos
                        self.lista_lidos.append(self.lista_tokens.pop(0))
                        #  faz transicao
                        self.transicao_index = 0
                        self.estado = transicao.estado_final
                        
                    else:
                        # atualiza transicao_index
                        self.transicao_index += 1
                else:
                    if valor == self.lista_tokens[0].tipo:
                        # coloca no historico
                        self.historico.coloca(self.estado, self.transicao_index)
                        # consome token da lista de tokens e poe na lista de lidos
                        self.lista_lidos.append(self.lista_tokens.pop(0))
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
                self.historico.coloca(self.estado, self.transicao_index)
                # faz transicao
                # coloca no estado um novo estado no automato destino
                self.estado = Estado(transicao.submaquina, 0)
                # poe index = 0
                self.transicao_index = 0

            elif transicao.tipo == "sai_submaquina":
                # desempilha
                item_pilha = self.pilha.pop()
                # poe no historico
                self.historico.coloca(self.estado, self.transicao_index)
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
                # Recoloca token (se tiver) na lista
                # Ve tipo de transicao
                if self.get_transicoes()[item_historico["transicao_index"]].tipo == "consome_token":
                    # pop_back na lista_lidos e push front na lista de tojkens
                    self.lista_tokens.insert(0, self.lista_lidos.pop(-1))

            else:
                continua = False

        return continua
