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
    elif is_identif(string):
        resposta.append(Token("identificador", string))
    elif is_number(string):
        resposta.append(Token("numero", string))
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
                    resposta.append(Token("string", "".join(word)))
                sinal = not sinal
                word = [c]
        if sinal:
            resposta.append(Token("".join(word), "".join(word)))
        else:
            word =  "".join(word)
            if is_number(word):
                resposta.append(Token("numero", word))
            elif word in reservadas:
                resposta.append(Token(word, word))
            else:
                resposta.append(Token("string",word))

    return resposta

def is_number(string):
    try:
        float(string)
        return True
    except:
        return False

def is_identif(string):
    identificador = re.match("[A-Za-z][0-9]", string)
    if identificador:
        if identificador == string:
            return True
        else:
            return False
    else:
        return False

def quebrar(linha):
    lista = re.compile("(\t)+|(\ )+").split(linha.strip())
    lista = list(filter(lambda a: a != None and a != " " and a != "\t", lista))
    return lista