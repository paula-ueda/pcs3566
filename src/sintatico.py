from utils import Automato
from classes import Token

def analise_sintatica(lista_linhas_token):
    lista_tokens = []
    lista_linha = []
    for linha in lista_linhas_token:
        for token in linha.tokens:
            lista_tokens.append(token)
            lista_linha.append(linha.numero)
        lista_tokens.append(Token("EOF", "EOF"))
    lista_tokens.pop(-1)

    automato = Automato(lista_tokens)
    continua = True
    contador = 0
    while(continua):
        print("--------------------------------------------")
        print(contador)
        automato.mostra()
        continua = automato.transiciona()
        aceito = automato.aceitou()
        if aceito is None:
            next = input()
            contador += 1
        else:
            break

    if aceito:
        print("Sequencia aceita")
    else:
        print("Sequencia não aceita")
    
    print(f"aceito: {aceito} | continua: {continua}")
    automato.mostra()