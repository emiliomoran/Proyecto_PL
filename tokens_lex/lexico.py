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
  'return':'RETURN',
  'break':'BREAK',
  'as':'AS',
  'import':'IMPORT',
  'def':'DEF',
  'print':'PRINT',
  'none':'NONE',
  'list':'LIST',
  'tuple':'TUPLE',
  'dic':'DIC',
  'from':'FROM',
  'set':'SET',
  'range':'RANGE',
  'len':'LEN',
}

#Lista de tokens
tokens = ['NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE','EQUALS','LPAREN','RPAREN','DEQUALS','DIFFERENT','LESS','HIGHER','LESSEQ','HIGHEREQ','EXPONENT','DIVIDEINT','MODULE','LCORCHETE','RCORCHETE','COMMA','COMILLA','COMILLAD','DPOINT'] + list(reservadas.values())

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
t_LCORCHETE = r'\['
t_RCORCHETE = r'\]'
t_COMMA = r','
t_COMILLA = r'\''
t_COMILLAD = r'"'
t_DPOINT = r':'

#Definicion de tokens para numeros
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

#Definicion de tokens para nombres de variables
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

##PRUEBA LEX##

def mostrar_tokens(cadena):
    l=[]
    lexer.input(cadena)
    while True:
        tok = lexer.token()
        if not tok: break
        print(tok.type)
        l.append(tok.type)
    return l
    #Formato de la salida: LexRoken(type, value, lineno, lexpos)
