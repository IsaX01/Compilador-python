import re

#Tupla que contiene los caracteres que reconocera el analizador lexico
TOKEN_TYPES = [
    #Se utiliza el simbolo \ en algunos para que no reconozca el mismo caracter un sin numero de veces
    #Esto se rige por el Lenguaje de expresiones regulares
    ('NUMBER',    r'\d+'),
    ('PLUS',      r'\+'),
    ('MINUS',     r'-'),
    ('TIMES',     r'\*'),
    ('DIVIDE',    r'/'),
    ('LPAREN',    r'\('),
    ('RPAREN',    r'\)'),
]

#Funcion que retornara a que tipo de caracter pertenece
def generate_tokens(expression):
    tokens = []
    #Evaluamos que mientras la expresion sea un token valido haga un match a la que pertenece y la devuelva como expresion
    while expression:
        for token_type, pattern in TOKEN_TYPES:
            match = re.match(pattern, expression)
            if match:
                token = match.group()
                tokens.append((token_type, token))
                expression = expression[len(token):]
                break
    return tokens


expression = input('Digite la exprecion que desea analizar su lexico Ej: 2 + 3 * 4 ')
tokens = generate_tokens(expression)
for token_type, token in tokens:
    print(token_type, token)