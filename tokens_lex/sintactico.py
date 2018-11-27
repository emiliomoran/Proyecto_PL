import ply.yacc as yacc
import lexico

tokens = lexico.tokens

def p_assign(p):
	'''assign : NAME EQUALS expr
			  | NAME EQUALS list
			  | NAME EQUALS cad			  
			  | for
			  | while
			  | if'''
	if(len(p)==4):
		p[0] = (p[2],p[1],p[3])
	if(len(p)==2):
		p[0] = (p[1])

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
	if(len(p)==3):
		p[0] = ("")
	if(len(p)==4):
		p[0] = (p[2])
	if(len(p)==5):
		p[0] = (p[2],p[3])

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
	if(len(p)==4):
		p[0] = (p[2])
	if(len(p)==5):
		p[0] = (p[1],p[3])

def p_index(p):
	'''index : factor
			 | factor DPOINT factor
			 | factor DPOINT factor DPOINT factor'''
	if(len(p)==2):
		p[0] = (p[1])
	if(len(p)==4):
		p[0] = (p[1],p[3])
	if(len(p)==6):
		p[0] = (p[1],p[3],p[5])

def p_while(p):
	'''while : WHILE LPAREN comparison RPAREN DPOINT
			 | WHILE LPAREN comparison comparisons RPAREN DPOINT'''
	if(len(p)==6):
		p[0] = (p[1],p[3])
	if(len(p)==7):
		p[0] = (p[1],p[3],p[4])

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
	'''for : FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT
		   | FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT
		   | FOR NAME IN NAME DPOINT'''
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
    '''if : IF LPAREN comparison RPAREN DPOINT assign
    	  | IF LPAREN comparison comparisons RPAREN DPOINT assign
    	  | IF comparison DPOINT assign
    	  | IF comparison comparisons DPOINT assign
          | IF LPAREN comparison RPAREN DPOINT assign ELSE DPOINT assign
          | IF LPAREN comparison comparisons RPAREN DPOINT assign ELSE DPOINT assign
          | IF comparison DPOINT assign ELSE DPOINT assign
          | IF comparison comparisons DPOINT assign ELSE DPOINT assign
          | IF LPAREN comparison RPAREN DPOINT assign ELIF LPAREN comparison RPAREN DPOINT assign ELSE DPOINT assign
          | IF LPAREN comparison comparisons RPAREN DPOINT assign ELIF LPAREN comparison comparisons RPAREN DPOINT assign ELSE DPOINT assign
		  | IF comparison DPOINT assign ELIF comparison DPOINT assign ELSE DPOINT assign
		  | IF comparison comparisons DPOINT assign ELIF comparison comparisons DPOINT assign ELSE DPOINT assign'''

yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = yacc.parse(s)
    print(result)