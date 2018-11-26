import ply.yacc as yacc
import lexico

tokens = lexico.tokens

def p_assign(p):
	'''assign : NAME EQUALS expr
			  | NAME EQUALS list
			  | NAME EQUALS cad
			  | while
			  | for'''

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
			  | MINUS NUMBER
			  | NAME'''

def p_cad(p):
	'''cad : COMILLA NAME COMILLA
		   | COMILLAD NAME COMILLAD
		   | cad LCORCHETE index RCORCHETE'''

def p_index(p):
	'''index : factor
			 | factor DPOINT factor
			 | factor DPOINT factor DPOINT factor'''

def p_while(p):
	'''while : WHILE LPAREN comparison RPAREN DPOINT
			 | WHILE LPAREN comparison comparisons RPAREN DPOINT'''

def p_comparisons(p):
	'''comparisons : AND comparison
				   | AND comparison comparisons
				   | OR comparison
				   | OR comparison comparisons'''

def p_bool(p):
	'''bool : TRUE
			| FALSE'''

def p_comparison(p):
    '''comparison : comp DEQUALS comp
                  | comp DIFFERENT comp
                  | comp HIGHER comp
                  | comp LESS comp
                  | comp HIGHEREQ  comp
                  | comp LESSEQ comp
                  | bool'''

def p_comp(p):
	'''comp : expr
			| element'''

def p_for(p):
	'''for : FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT
		   | FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT
		   | FOR NAME IN NAME DPOINT'''

def p_r_values(p):
	'''r_values : r_value COMMA r_value
				| r_value COMMA r_value COMMA r_value'''

def p_r_value(p):
	'''r_value : factor'''

yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)