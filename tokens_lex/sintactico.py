import ply.yacc as yacc
import lexico

tokens = lexico.tokens

def p_assign(p):
	'''assign : NAME EQUALS expr
			  | NAME EQUALS list
			  | NAME EQUALS cad'''


def p_expr(p):
	'''expr : expr PLUS term
			| expr MINUS term
			| term'''

def p_term(p):
	'''term : term TIMES factor
			| term DIVIDE factor
			| factor'''

def p_list(p):
	'''list : LCORCHETE RCORCHETE
			| LCORCHETE element RCORCHETE
			| LCORCHETE element elements RCORCHETE'''

def p_element(p):
	'''element : factor
			   | NAME
			   | list'''

def p_elements(p):
	'''elements : COMMA element
				| COMMA list
				| COMMA element elements'''

def p_factor(p):
	'''factor : NUMBER
			  | MINUS NUMBER'''

def p_cad(p):
	'''cad : COMILLA NAME COMILLA
		   | COMILLAD NAME COMILLAD
		   | cad LCORCHETE index RCORCHETE'''

def p_index(p):
	'''index : factor
			 | factor DPOINT factor
			 | factor DPOINT factor DPOINT factor'''

def p_for(p):
	'''elements: FOR NAME IN NAME
	| FOR NAME IN RANGE LPAREN NUMBER RPAREN
	| FOR NAME IN RANGE LPAREN LEN LPAREN NAME RPAREN RPAREN
	'''
yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)