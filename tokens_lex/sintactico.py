import ply.yacc as yacc
import lexico

tokens = lexico.tokens

def p_sentencia(p):
	'''sentencia : assign
				 | for
				 | while
				 | if
				 | assign sentencia
				 | for sentencia
				 | while sentencia
				 | if sentencia'''

	if(len(p)==2):
		p[0] = ('SENTENCIA',p[1])
	if(len(p)==3):
		p[0] = ('SENTENCIA',p[1],p[2])


def p_assign(p):
	'''assign : NAME EQUALS expr
			  | NAME EQUALS list
			  | NAME EQUALS cad'''
	p[0] = (p[2],p[1],p[3])

"""
def p_assign(p):
	'''assign : NAME EQUALS expr
			  | NAME EQUALS list
			  | NAME EQUALS cad			  
			  | for
			  | while
			  | if
			  | NAME EQUALS expr assign
			  | NAME EQUALS list assign
			  | NAME EQUALS cad assign  
			  | for assign
			  | while assign
			  | if assign'''

	if(len(p)==4):
		p[0] = (p[2],p[1],p[3])
	if(len(p)==2):
		p[0] = (p[1])
"""

def p_expr(p):
	'''expr : expr PLUS term
			| expr MINUS term
			| term'''
	if(len(p)==4):
		p[0] = (p[2], p[1],p[3])
	if(len(p)==2):
		p[0] = (p[1])

def p_term(p):
	'''term : term TIMES factor
			| term DIVIDE factor
			| factor'''
	if(len(p)==4):
		p[0] = (p[2],p[1],p[3])
	if(len(p)==2):
		p[0] = (p[1])		

def p_list(p):
	'''list : LCORCHETE RCORCHETE
			| LCORCHETE element RCORCHETE
			| LCORCHETE element elements RCORCHETE'''
	"""
	if(len(p)==3):
		p[0] = ("")
	if(len(p)==4):
		p[0] = (p[2])
	if(len(p)==5):
		p[0] = (p[2],p[3])
	"""

def p_element(p):
	'''element : factor
			   | NAME
			   | list'''
	p[0] = (p[1])

def p_elements(p):
	'''elements : COMMA element
				| COMMA list
				| COMMA element elements'''
	if(len(p)==3):
		p[0] = (p[2])
	if(len(p)==4):
		p[0] = (p[2],p[3])

def p_factor(p):
	'''factor : NUMBER
			  | MINUS NUMBER
			  | NAME'''
	if(len(p)==3):
		p[0] = (p[1],p[2])
	if(len(p)==2):
		p[0] = (p[1])

def p_cad(p):
	'''cad : COMILLA NAME COMILLA
		   | COMILLAD NAME COMILLAD
		   | cad LCORCHETE index RCORCHETE'''
	"""
	if(len(p)==4):
		p[0] = (p[2])
	if(len(p)==5):
		p[0] = (p[1],p[3])
	"""

def p_index(p):
	'''index : factor
			 | factor DPOINT factor
			 | factor DPOINT factor DPOINT factor'''
	"""
	if(len(p)==2):
		p[0] = (p[1])
	if(len(p)==4):
		p[0] = (p[1],p[3])
	if(len(p)==6):
		p[0] = (p[1],p[3],p[5])
	"""

def p_while(p):
	'''while : WHILE LPAREN comparison RPAREN DPOINT sentencia
			 | WHILE comparison DPOINT sentencia
			 | WHILE LPAREN comparison comparisons RPAREN DPOINT sentencia
			 | WHILE comparison comparisons DPOINT sentencia'''
	if(len(p)==5):
		p[0] = (p[1],p[2],p[4])
	if(len(p)==6):
		p[0] = (p[1],p[2],p[3],p[5])
	if(len(p)==7):
		p[0] = (p[1],p[3],p[6])
	if(len(p)==8):
		p[0] = (p[1],p[3],p[4],p[7])

def p_comparisons(p):
	'''comparisons : AND comparison
				   | AND comparison comparisons
				   | OR comparison
				   | OR comparison comparisons'''
	if(len(p)==3):
		p[0] = (p[1],p[2])
	if(len(p)==4):
		p[0] = (p[1],p[2],p[3])

def p_bool(p):
	'''bool : TRUE
			| FALSE'''
	p[0] = (p[1])


def p_comparison(p):
    '''comparison : comp DEQUALS comp
                  | comp DIFFERENT comp
                  | comp HIGHER comp
                  | comp LESS comp
                  | comp HIGHEREQ  comp
                  | comp LESSEQ comp
                  | bool'''
    if(len(p)==4):
    	p[0] = (p[2],p[1],p[3])
    if(len(p)==2):
    	p[0] = (p[1])

def p_comp(p):
	'''comp : expr
			| element'''
	p[0] = (p[1])

def p_for(p):
	'''for : FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign
		   | FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign
		   | FOR NAME IN NAME DPOINT assign'''
	if(len(p)==9):
		p[0] = (p[2],p[3],p[4])
	if(len(p)==6):
		p[0] = (p[2],p[4])

def p_r_values(p):
	'''r_values : r_value COMMA r_value
				| r_value COMMA r_value COMMA r_value'''
	if(len(p)==4):
		p[0] = (p[1],p[2])
	if(len(p)==6):
		p[0] = (p[1],p[3],p[4])

def p_r_value(p):
	'''r_value : factor
			   | LEN LPAREN NAME RPAREN'''
	if(len(p)==2):
		p[0] = (p[1])
	if(len(p)==5):
		p[0] = (p[1],p[3])

def p_if(p):
    '''if : IF LPAREN comparison RPAREN DPOINT sentencia
    	  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia
    	  | IF comparison DPOINT sentencia
    	  | IF comparison comparisons DPOINT sentencia
          | IF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia
          | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia
          | IF comparison DPOINT sentencia ELSE DPOINT sentencia
          | IF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia
          | IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia
          | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia
		  | IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia ELSE DPOINT sentencia
		  | IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia'''	

def p_error(p):
    if p:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(p.type),str(p.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(p)
        print(resultado)

yacc.yacc()


def ejecutar_yacc(s):
 	result = yacc.parse(s)
 	print(result)
 	print(type(result))    

"""
while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = yacc.parse(s)
    print(result)
    print(type(result))    
    #print(result.__str__())
"""