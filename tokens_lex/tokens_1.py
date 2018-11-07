import ply.lex as lex

#Palabras reservadas
reservadas = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'elif' : 'ELIF',
   'while' : 'WHILE',
   'for' : 'FOR',
   'and' : 'AND',
   'or' : 'OR',
   'not' : 'NOT',
   'True': 'TRUE',
   'False': 'FALSE',
   'in': 'IN',
   'is': 'IS',
}

#Lista de tokens
tokens = ['NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN','DEQUALS','DIFFERENT','LESS','HIGHER','LESSEQ','HIGHEREQ','EXPONENT','DIVIDEINT','MODULE'] + list(reservadas.values())

#Definicion de tokens de caracteres simples
t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_DEQUALS = r'=='
t_DIFFERENT = r'!=|<>'
t_LESS = r'<'
t_HIGHER = r'>'
t_LESSEQ = r'<='
t_HIGHEREQ = r'>='
t_EXPONENT = r'\*\*'
t_DIVIDEINT = r'//'
t_MODULE = r'%'

#Para numeros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Para nombres de variables
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value, 'NAME')
    return t

#Para saltos de lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

#Para errores
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])

lexer = lex.lex()

#Pruebas
cadena1 = "3 + 4 * 10 + -20 *2"
cadena2 = "x = 3 * 4 + 5 * 6"
cadena3 = "for = 3 * 4 + 5 * 6"
cadena4 = "x == True"
cadena5 = "x <> 10"
cadena6 = "x and y"
cadena7 = "x**10"
cadena8 = "x//2"
cadena9 = "10%2"

#lexer.input(cadena1)
#lexer.input(cadena2)
#lexer.input(cadena3)
#lexer.input(cadena4)
lexer.input(cadena5)
#lexer.input(cadena6)
#lexer.input(cadena7)
#lexer.input(cadena8)
#lexer.input(cadena9)

while True:
    tok = lexer.token()
    if not tok: break
    print(tok)
    #Formato de la salida: LexRoken(type, value, lineno, lexpos)