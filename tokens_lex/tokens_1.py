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


#Reglas de parsing
precedence = (
    ('left','PLUS','MINUS'),
    ('left','TIMES','DIVIDE'),
    ('right','UMINUS'),
    )

#Diccionario de nombres
names = { }

def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]


def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

# IF
def p_statement_if(t):
    '''statement : IF LPAREN comparison RPAREN statement
                    | IF LPAREN comparison RPAREN statement ELSE statement'''
    if t[3]:
        t[0] = t[5]
    else:
        if t[7] is not None:
            t[0] = t[7]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

# comparison
def p_comparison_binop(t):
    '''comparison : expression DEQUALS expression
                          | expression DIFFERENT expression
                          | expression HIGHER expression
                          | expression LESS expression
                          | expression HIGHEREQ  expression
                          | expression LESSEQ expression'''
    if t[2] == '==':
        t[0] = t[1] == t[3]
    elif t[2] == '!=':
        t[0] = t[1] != t[3]
    elif t[2] == '>':
        t[0] = t[1] > t[3]
    elif t[2] == '<':
        t[0] = t[1] < t[3]
    elif t[2] == '>=':
        t[0] = t[1] >= t[3]
    elif t[2] == '<=':
        t[0] = t[1] <= t[3]

import ply.yacc as yacc
parser = yacc.yacc()

#Pruebas
#cadena1 = "3 + 4 * 10 + -20 *2"
#cadena2 = "x = 3 * 4 + 5 * 6"
#cadena3 = "for = 3 * 4 + 5 * 6"
#cadena4 = "x == True"
#cadena5 = "x <> 10"
#cadena6 = "x and y"
#cadena7 = "x**10"
#cadena8 = "x//2"
#cadena9 = "10%2"

#lexer.input(cadena1)
#lexer.input(cadena2)
#lexer.input(cadena3)
#lexer.input(cadena4)
#lexer.input(cadena5)
#lexer.input(cadena6)
#lexer.input(cadena7)
#lexer.input(cadena8)
#lexer.input(cadena9)

#while True:
 #   tok = lexer.token()
  #  if not tok: break
   # print(tok)
    #Formato de la salida: LexRoken(type, value, lineno, lexpos)

while True:
    try:
        s = input('>> ')   # Use raw_input on Python 2
    except EOFError:
        break
    resultado=parser.parse(s)
    print(resultado)