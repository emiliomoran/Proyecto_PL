import ply.yacc as yacc
import lexico

tokens = lexico.tokens

def p_assign(p):
	'''assign : NAME EQUALS expr'''

def p_expr(p):
	'''expr : expr PLUS term
			| expr MINUS term
			| term'''

def p_term(p):
	'''term : term TIMES factor
			| term DIVIDE factor
			| factor'''

def p_lista(p):
	'''assign : NAME EQUALS list'''

def p_list(p):
	'''list : LCORCHETE RCORCHETE
			| LCORCHETE elements RCORCHETE'''

def p_elements(p):
	'''elements : factor
			   | NAM '''

def p_factor(p):
	'''factor : NUMBER'''

yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)