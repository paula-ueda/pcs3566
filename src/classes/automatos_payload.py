from transicao import *
from estado import *
payload = {
    "program": {
        "estados": [0, 1, 2, 3],
        "final": [3],
        "transicoes": {
            "0": [
                Transicao(
                    "entra_submaquina",
                    Estado("program", 0),
                    Estado("program", 1),
                    submaquina="bstatement"
                )
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("program", 1),
                    Estado("program", 1),
                    submaquina="bstatement"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("program", 1),
                    Estado("program", 2),
                    submaquina="int"
                )
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("program", 2),
                    Estado("program", 3),
                    token=(True, "END")
                )
            ],
            "3": [
                Transicao(
                    "sai_submaquina",
                    Estado("program", 3),
                    None
                ),
            ]
        }
    },
    "bstatement": {
        "estados": [0, 1, 2],
        "final": [2],
        "transicoes": {
            "0": [
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 0),
                    Estado("bstatement", 1),
                    submaquina="int"
                )
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="assign"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="read"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="data"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="print"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="goto"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="if"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="for"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="next"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="dim"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="def"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="gosub"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="return"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("bstatement", 1),
                    Estado("bstatement", 2),
                    submaquina="remark"
                ),
            ],
            "2": [
                Transicao(
                    "sai_submaquina",
                    Estado("bstatement", 2),
                    None
                ),
            ]
        }
    },
    "assign": {
        "estados": [0, 1, 2, 3, 4],
        "final": [4],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("assign", 0),
                    Estado("assign", 1),
                    token=(True, "LET")
                ),
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("assign", 1),
                    Estado("assign", 2),
                    submaquina="var"
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("assign", 2),
                    Estado("assign", 3),
                    token=(True, "=")
                ),
            ],
            "3": [
                Transicao(
                    "entra_submaquina",
                    Estado("assign", 3),
                    Estado("assign", 4),
                    submaquina="exp"
                ),
            ],
            "4": [
                Transicao(
                    "sai_submaquina",
                    Estado("assign", 4),
                    None
                ),
            ],
        }
    },
    "var": {
        "estados": [0, 1, 2, 3, 4],
        "final": [2],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("var", 0),
                    Estado("var", 1),
                    token=(False, "letra")
                ),
                Transicao(
                    "consome_token",
                    Estado("var", 0),
                    Estado("var", 2),
                    token=(False, "letra")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("var", 1),
                    Estado("var", 2),
                    token=(False, "digito")
                ),
                Transicao(
                    "consome_token",
                    Estado("var", 1),
                    Estado("var", 4),
                    token=(True, "(")
                ),
            ],
            "2": [
                Transicao(
                    "sai_submaquina",
                    Estado("var", 2),
                    None
                ),
            ],
            "3": [
                Transicao(
                    "consome_token",
                    Estado("var", 3),
                    Estado("var", 2),
                    token=(True, ")")
                ),
                Transicao(
                    "consome_token",
                    Estado("var", 3),
                    Estado("var", 4),
                    token=(True, ",")
                ),
            ],
            "4": [
                Transicao(
                    "entra_submaquina",
                    Estado("var", 4),
                    Estado("var", 3),
                    submaquina="exp"
                ),
            ],
        }
    },
    "exp": {
        "estados": [0, 1],
        "final": [1],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("exp", 0),
                    Estado("exp", 0),
                    token=(True, "+")
                ),
                Transicao(
                    "consome_token",
                    Estado("exp", 0),
                    Estado("exp", 0),
                    token=(True, "-")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("exp", 0),
                    Estado("exp", 1),
                    submaquina="eb"
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("exp", 1),
                    Estado("exp", 0),
                    token=(True, "+")
                ),
                Transicao(
                    "consome_token",
                    Estado("exp", 1),
                    Estado("exp", 0),
                    token=(True, "-")
                ),
                Transicao(
                    "consome_token",
                    Estado("exp", 1),
                    Estado("exp", 0),
                    token=(True, "*")
                ),
                Transicao(
                    "consome_token",
                    Estado("exp", 1),
                    Estado("exp", 0),
                    token=(True, "/")
                ),
                Transicao(
                    "consome_token",
                    Estado("exp", 1),
                    Estado("exp", 0),
                    token=(True, "^")
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("exp", 1),
                    None
                ),
            ],
        }
    },
    "eb": {
        "estados": [0, 1, 2, 3, 4, 5, 6, 7],
        "final": [3],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("eb", 0),
                    Estado("eb", 1),
                    token=(True, "(")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("eb", 0),
                    Estado("eb", 3),
                    submaquina="num"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("eb", 0),
                    Estado("eb", 3),
                    submaquina="var"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("eb", 0),
                    Estado("eb", 4),
                    submaquina="fn"
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("eb", 0),
                    Estado("eb", 5),
                    submaquina="predef"
                ),
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("eb", 1),
                    Estado("eb", 2),
                    submaquina="exp"
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("eb", 2),
                    Estado("eb", 3),
                    token=(True, ")")
                ),
            ],
            "3": [
                Transicao(
                    "sai_submaquina",
                    Estado("eb", 3),
                    None
                ),
            ],
            "4": [
                Transicao(
                    "consome_token",
                    Estado("eb", 4),
                    Estado("eb", 5),
                    token=(False, "letra")
                ),
            ],
            "5": [
                Transicao(
                    "consome_token",
                    Estado("eb", 0),
                    Estado("eb", 1),
                    token=(True, "(")
                ),
            ],
            "6": [
                Transicao(
                    "entra_submaquina",
                    Estado("eb", 6),
                    Estado("eb", 7),
                    submaquina="exp"
                ),
            ],
            "7": [
                Transicao(
                    "consome_token",
                    Estado("eb", 7),
                    Estado("eb", 3),
                    token=(True, ")")
                ),
            ],
        }
    },
    "predef": {
        "estados": [0, 1],
        "final": [1],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "SIN")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "COS")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "TAN")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "ATN")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "EXP")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "ABS")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "LOG")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "SQR")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "INT")
                ),
                Transicao(
                    "consome_token",
                    Estado("predef", 0),
                    Estado("predef", 1),
                    token=(True, "RND")
                ),
            ],
            "1": [
                Transicao(
                    "sai_submaquina",
                    Estado("predef", 1),
                    None
                ),
            ],
        }
    },
    "read": {
        "estados": [0, 1, 2, 3],
        "final": [3],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("read", 0),
                    Estado("read", 1),
                    token=(True, "READ")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("read", 1),
                    Estado("read", 2),
                    token=(True, ",")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("read", 1),
                    Estado("read", 3),
                    submaquina="var"
                ),
            ],
            "2": [
                Transicao(
                    "entra_submaquina",
                    Estado("read", 2),
                    Estado("read", 3),
                    submaquina="var"
                ),
            ],
            "3": [
                Transicao(
                    "sai_submaquina",
                    Estado("read", 3),
                    None
                ),
            ],
        }
    },
    "data": {
        "estados": [0, 1, 2, 3],
        "final": [3],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("data", 0),
                    Estado("data", 1),
                    token=(True, "DATA")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("data", 1),
                    Estado("data", 2),
                    token=(True, ",")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("data", 1),
                    Estado("data", 3),
                    submaquina="snum"
                ),
            ],
            "2": [
                Transicao(
                    "entra_submaquina",
                    Estado("data", 2),
                    Estado("data", 3),
                    submaquina="snum"
                ),
            ],
            "3": [
                Transicao(
                    "sai_submaquina",
                    Estado("data", 3),
                    None
                ),
            ],
        }
    },
    "print": {
        "estados": [0, 1, 2, 3, 4],
        "final": [1, 2, 3],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("print", 0),
                    Estado("print", 1),
                    token=(True, "PRINT")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("print", 1),
                    Estado("print", 2),
                    token=(True, ",")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("print", 1),
                    Estado("print", 3),
                    submaquina="pitem"
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("print", 1),
                    None
                ),
            ],
            "2": [
                Transicao(
                    "sai_submaquina",
                    Estado("print", 2),
                    None
                ),
            ],
            "3": [
                Transicao(
                    "consome_token",
                    Estado("print", 3),
                    Estado("print", 4),
                    token=(True, "-")
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("print", 3),
                    None
                ),
            ],
            "4": [
                Transicao(
                    "entra_submaquina",
                    Estado("print", 3),
                    Estado("print", 4),
                    submaquina="pitem"
                ),
            ]
        }
    },
    "pitem": {
        "estados": [0, 1, 2, 3, 4],
        "final": [4],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("pitem", 0),
                    Estado("pitem", 1),
                    token=(True, '"')
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("pitem", 0),
                    Estado("pitem", 4),
                    submaquina="exp"
                ),
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("pitem", 1),
                    Estado("pitem", 2),
                    submaquina="character"
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("pitem", 2),
                    Estado("pitem", 3),
                    token=(True, '"')
                ),
                Transicao(
                    "consome_token",
                    Estado("pitem", 2),
                    Estado("pitem", 4),
                    token=(True, '"')
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("pitem", 2),
                    Estado("pitem", 2),
                    submaquina="character"
                ),
            ],
            "3": [
                Transicao(
                    "entra_submaquina",
                    Estado("pitem", 3),
                    Estado("pitem", 4),
                    submaquina="exp"
                ),
            ],
            "4": [
                Transicao(
                    "sai_submaquina",
                    Estado("pitem", 4),
                    None
                ),
            ],
        }
    },
    "goto": {
        "estados": [0, 1, 2],
        "final": [2],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("goto", 0),
                    Estado("goto", 1),
                    token=(True, "GO TO")
                ),
                Transicao(
                    "consome_token",
                    Estado("goto", 0),
                    Estado("goto", 1),
                    token=(True, "GOTO")
                ),
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("goto", 1),
                    Estado("goto", 2),
                    submaquina="int"
                ),
            ],
            "2": [
                Transicao(
                    "sai_submaquina",
                    Estado("goto", 2),
                    None
                ),
            ],
        }
    },
    "if": {
        "estados": [0, 1, 2, 3, 4, 5, 6],
        "final": [6],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("if", 0),
                    Estado("if", 1),
                    token=(True, "IF")
                ),
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("if", 1),
                    Estado("if", 2),
                    submaquina="exp"
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("if", 2),
                    Estado("if", 3),
                    token=(True, ">=")
                ),
                Transicao(
                    "consome_token",
                    Estado("if", 2),
                    Estado("if", 3),
                    token=(True, ">")
                ),
                Transicao(
                    "consome_token",
                    Estado("if", 2),
                    Estado("if", 3),
                    token=(True, "<>")
                ),
                Transicao(
                    "consome_token",
                    Estado("if", 2),
                    Estado("if", 3),
                    token=(True, "<")
                ),
                Transicao(
                    "consome_token",
                    Estado("if", 2),
                    Estado("if", 3),
                    token=(True, "<=")
                ),
                Transicao(
                    "consome_token",
                    Estado("if", 2),
                    Estado("if", 3),
                    token=(True, "=")
                ),

            ],
            "3": [
                Transicao(
                    "entra_submaquina",
                    Estado("if", 3),
                    Estado("if", 4),
                    submaquina="exp"
                ),
            ],
            "4": [
                Transicao(
                    "consome_token",
                    Estado("if", 4),
                    Estado("if", 5),
                    token=(True, "THEN")
                ),
            ],
            "5": [
                Transicao(
                    "entra_submaquina",
                    Estado("if", 5),
                    Estado("if", 6),
                    submaquina="int"
                ),
            ],
            "6": [
                Transicao(
                    "sai_submaquina",
                    Estado("if", 6),
                    None
                ),
            ],
        }
    },
    "for": {
        "estados": [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        "final": [9],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("for", 0),
                    Estado("for", 1),
                    token=(True, "FOR")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("for", 1),
                    Estado("for", 2),
                    token=(False, "letra")
                ),
                Transicao(
                    "consome_token",
                    Estado("for", 1),
                    Estado("for", 3),
                    token=(False, "letra")
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("for", 2),
                    Estado("for", 3),
                    token=(False, "digito")
                ),            
            ],
            "3": [
                Transicao(
                    "consome_token",
                    Estado("for", 3),
                    Estado("for", 4),
                    token=(True, "=")
                ),
            ],
            "4": [
                Transicao(
                    "entra_submaquina",
                    Estado("for", 4),
                    Estado("for", 5),
                    submaquina="exp"
                ),
            ],
            "5": [
                Transicao(
                    "consome_token",
                    Estado("for", 5),
                    Estado("for", 6),
                    token=(True, "TO")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("for", 5),
                    Estado("for", 6),
                    submaquina="exp"
                ),
            ],
            "6": [
                Transicao(
                    "entra_submaquina",
                    Estado("for", 6),
                    Estado("for", 7),
                    submaquina="exp"
                ),
            ],
            "7": [
                Transicao(
                    "consome_token",
                    Estado("for", 7),
                    Estado("for", 8),
                    token=(True, "STEP")
                ),
            ],
            "8": [
                Transicao(
                    "entra_submaquina",
                    Estado("for", 8),
                    Estado("for", 9),
                    submaquina="exp"
                ),
            ],
            "9": [
                Transicao(
                    "sai_submaquina",
                    Estado("for", 9),
                    None
                ),
            ],
        }
    },
    "next": {
        "estados": [0, 1, 2, 3],
        "final": [3],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("next", 0),
                    Estado("next", 1),
                    token=(True, "NEXT")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("next", 1),
                    Estado("next", 2),
                    token=(False, "letra")
                ),
                Transicao(
                    "consome_token",
                    Estado("next", 1),
                    Estado("next", 3),
                    token=(False, "letra")
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("next", 2),
                    Estado("next", 3),
                    token=(False, "digito")
                ),
            ],
            "3": [
                Transicao(
                    "sai_submaquina",
                    Estado("next", 3),
                    None
                ),
            ]
        }
    },
    "dim": {
        "estados": [0, 1, 2, 3, 4, 5, 6],
        "final": [6],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("dim", 0),
                    Estado("dim", 1),
                    token=(True, "DIM")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("dim", 1),
                    Estado("dim", 2),
                    token=(False, "letra")
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("dim", 2),
                    Estado("dim", 3),
                    token=(True, "(")
                ),
            ],
            "3": [
                Transicao(
                    "entra_submaquina",
                    Estado("dim", 3),
                    Estado("dim", 4),
                    submaquina="int"
                ),
            ],
            "4": [
                Transicao(
                    "consome_token",
                    Estado("dim", 4),
                    Estado("dim", 5),
                    token=(True, ",")
                ),
                Transicao(
                    "consome_token",
                    Estado("dim", 4),
                    Estado("dim", 6),
                    token=(True, ")")
                ),

            ],
            "5": [
                Transicao(
                    "entra_submaquina",
                    Estado("dim", 5),
                    Estado("dim", 4),
                    submaquina="int"
                ),
            ],
            "6": [
                Transicao(
                    "consome_token",
                    Estado("dim", 6),
                    Estado("dim", 1),
                    token=(True, ",")
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("dim", 6),
                    None
                ),
            ],
        }
    },
    "def": {
        "estados": [0, 1, 2, 3, 4, 5, 6, 7, 8],
        "final": [8],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("def", 0),
                    Estado("def", 1),
                    token=(True, "DEF FN")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("def", 1),
                    Estado("def", 2),
                    token=(False, "letra")
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("def", 2),
                    Estado("def", 3),
                    token=(True, "(")
                ),
            ],
            "3": [
                Transicao(
                    "consome_token",
                    Estado("def", 3),
                    Estado("def", 4),
                    token=(False, "letra")
                ),
            ],
            "4": [
                Transicao(
                    "consome_token",
                    Estado("def", 4),
                    Estado("def", 5),
                    token=(False, "digito")
                ),
                Transicao(
                    "consome_token",
                    Estado("def", 4),
                    Estado("def", 6),
                    token=(True, ")")
                ),
            ],
            "5": [
                Transicao(
                    "consome_token",
                    Estado("def", 5),
                    Estado("def", 6),
                    token=(True, ")")
                ),
            ],
            "6": [
                Transicao(
                    "consome_token",
                    Estado("def", 6),
                    Estado("def", 7),
                    token=(True, "=")
                ),
            ],
            "7": [
                Transicao(
                    "entra_submaquina",
                    Estado("def", 7),
                    Estado("def", 8),
                    submaquina="exp"
                ),
            ],
            "8": [
                Transicao(
                    "sai_submaquina",
                    Estado("def", 8),
                    None
                ),
            ],
        }
    },
    "gosub": {
        "estados": [0, 1, 2],
        "final": [2],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("gosub", 0),
                    Estado("gosub", 1),
                    token=(True, "GOSUB")
                ),
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("gosub", 1),
                    Estado("gosub", 2),
                    submaquina="int"
                ),
            ],
            "2": [
                Transicao(
                    "sai_submaquina",
                    Estado("gosub", 2),
                    None
                ),
            ],
        }
    },
    "return": {
        "estados": [0, 1],
        "final": [1],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("return", 0),
                    Estado("return", 1),
                    token=(True, "RETURN")
                ),
            ],
            "1": [
                Transicao(
                    "sai_submaquina",
                    Estado("return", 1),
                    None
                ),
            ],
        }
    },
    "remark": {
        "estados": [0, 1],
        "final": [1],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("remark", 0),
                    Estado("remark", 1),
                    token=(True, "REM")
                ),
            ],
            "1": [
                Transicao(
                    "entra_submaquina",
                    Estado("remark", 1),
                    Estado("remark", 1),
                    submaquina="character"
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("remark", 1),
                    None
                ),
            ],
        }
    },
    "int": {
        "estados": [0, 1],
        "final": [1],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("int", 0),
                    Estado("int", 1),
                    token=(False, "digito")
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("int", 1),
                    Estado("int", 1),
                    token=(False, "digito")
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("int", 1),
                    None
                ),
            ],
        }
    },
    "num": {
        "estados": [0, 1, 2, 3, 4, 5, 6, 7],
        "final": [2, 5, 6],
        "transicoes": {
            "0": [
                Transicao(
                    "consome_token",
                    Estado("num", 0),
                    Estado("num", 7),
                    token=(True, ".")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("num", 0),
                    Estado("num", 1),
                    submaquina="int"
                ),
            ],
            "1": [
                Transicao(
                    "consome_token",
                    Estado("num", 1),
                    Estado("num", 2),
                    token=(True, ".")
                ),
            ],
            "2": [
                Transicao(
                    "consome_token",
                    Estado("num", 2),
                    Estado("num", 2),
                    token=(False, "digito")
                ),
                Transicao(
                    "consome_token",
                    Estado("num", 2),
                    Estado("num", 3),
                    token=(True, "E")
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("num", 2),
                    None
                ),
            ],
            "3": [
                Transicao(
                    "consome_token",
                    Estado("num", 3),
                    Estado("num", 4),
                    token=(True, "+")
                ),
                Transicao(
                    "consome_token",
                    Estado("num", 3),
                    Estado("num", 4),
                    token=(True, "-")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("num", 3),
                    Estado("num", 5),
                    submaquina="int"
                ),
            ],
            "4": [
                Transicao(
                    "entra_submaquina",
                    Estado("num", 4),
                    Estado("num", 5),
                    submaquina="int"
                ),
            ],
            "5": [
                Transicao(
                    "sai_submaquina",
                    Estado("num", 5),
                    None
                ),
            ],
            "6": [
                Transicao(
                    "consome_token",
                    Estado("num", 6),
                    Estado("num", 7),
                    token=(True, "E")
                ),
                Transicao(
                    "sai_submaquina",
                    Estado("num", 6),
                    None
                ),
            ],
            "7": [
                Transicao(
                    "entra_submaquina",
                    Estado("num", 7),
                    Estado("num", 6),
                    submaquina="int"
                ),            
            ],
        }
    },
    "snum": {
        "estados": [0, 1, 2],
        "final": [2],
        "transicoes": {
        "0": [
            Transicao(
                    "consome_token",
                    Estado("snum", 0),
                    Estado("snum", 1),
                    token=(True, "+")
                ),
                Transicao(
                    "consome_token",
                    Estado("snum", 0),
                    Estado("snum", 1),
                    token=(True, "-")
                ),
                Transicao(
                    "entra_submaquina",
                    Estado("snum", 0),
                    Estado("snum", 2),
                    submaquina="num"
                ),
        ],
        "1": [
            Transicao(
                    "entra_submaquina",
                    Estado("snum", 1),
                    Estado("snum", 2),
                    submaquina="num"
                ),
            
        ],
        "2": [
            Transicao(
                    "sai_submaquina",
                    Estado("snum", 2),
                    None
                ),
        ],
        }
    },
    "character": {
        "estados": [0, 1, 2],
        "final": [2],
        "transicoes": {
        "0": [
            Transicao(
                    "consome_token",
                    Estado("character", 0),
                    Estado("character", "letra"),
                    token=(False, "+")
                ),
                Transicao(
                    "consome_token",
                    Estado("character", 0),
                    Estado("character", 1),
                    token=(False, "digito")
                ),
        ],
        "1": [
            Transicao(
                    "sai_submaquina",
                    Estado("character", 1),
                    None
                ),
        ],
        }
    }
}