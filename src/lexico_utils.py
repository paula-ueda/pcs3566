import re
from sinais import sinais
from reservadas import reservadas
from token_lexico import Token

def classificar(string):
    resposta = []
    if (
        string in sinais or
        string in reservadas
    ):
        resposta.append(Token(string, string))
    else:      
        sinal = None
        word = []
        tokens = []
        
        if string[0] in sinais:
            sinal = True
        else:
            sinal = False
            
        for c in string:
            if c in sinais and sinal:
                word.append(c)
            elif c not in sinais and not sinal:
                word.append(c)
            else:
                if sinal:
                    resposta.append(Token("".join(word), "".join(word)))
                else:
                    for char in word:
                        if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                            resposta.append(Token("digito", char))
                        else:
                            resposta.append(Token("letra", char))
                sinal = not sinal
                word = [c]
        if sinal:
            resposta.append(Token("".join(word), "".join(word)))
        else:
            for char in word:
                if char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    resposta.append(Token("digito", char))
                else:
                    resposta.append(Token("letra", char))

    return resposta

def quebrar(linha):
    lista = re.compile("(\t)+|(\ )+").split(linha.strip())
    lista = list(filter(lambda a: a != None and a != " " and a != "\t", lista))
    return lista