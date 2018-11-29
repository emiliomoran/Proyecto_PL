import ply.yacc as yacc
import lexico

tokens = lexico.tokens
errors_list=[]
def p_sentencia(p): #definicion de sentencia/estructura de datos
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


def p_assign(p): #definicion de asignacion de variables
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

def p_list(p): #definicion de  lista
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

	p[0] = ('LISTA')

def p_element(p): #definicion numerica
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

def p_factor(p): #definicion numerica de valores
	'''factor : NUMBER
			  | MINUS NUMBER
			  | NAME'''
	if(len(p)==3):
		p[0] = (p[1],p[2])
	if(len(p)==2):
		p[0] = (p[1])

def p_cad(p): #definicion de cadena de caracteres
	'''cad : COMILLA str COMILLA
		   | COMILLAD str COMILLAD
		   | cad LCORCHETE index RCORCHETE'''
	p[0] = ('CADENA')

def p_str(p): #definicion de string
	'''str : NAME
		   | NAME str'''

def p_index(p): #definicion de indice
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

	p[0] = ('INDEX')

def p_while(p):#definicion de la estructura while
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

def p_comparisons(p): #definicion para anidar sentencias logicas
	'''comparisons : AND comparison
				   | AND comparison comparisons
				   | OR comparison
				   | OR comparison comparisons'''
	if(len(p)==3):
		p[0] = (p[1],p[2])
	if(len(p)==4):
		p[0] = (p[1],p[2],p[3])

def p_bool(p): #definicion de valores booleanos
	'''bool : TRUE
			| FALSE'''
	p[0] = (p[1])


def p_comparison(p): #definicion de las comparaciones que se realizan entre dos variables
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
			| element
			| bool'''
	p[0] = (p[1])

def p_for(p): #definicion del for en 3 formas conocidas
	'''for : FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign
		   | FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign
		   | FOR NAME IN NAME DPOINT assign'''
	if(len(p)==10):
		p[0] = (p[1],p[2],p[3],p[4],p[6],p[9])
	if(len(p)==7):
		p[0] = (p[1],p[2],p[3],p[4],p[6])

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

def p_if(p): #definicion de if en sus diversas formas
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
		  | IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia
		  | IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia
		  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia
		  | IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia
		  | IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia'''
	#cada uno de los tokens que vayan a fotmar el arbol tambien debe de definirselo abajo
	if(len(p)==5):
		p[0] = (p[1],p[2],p[4])
	if(len(p)==7):
		p[0] = (p[1],p[3],p[6])
	if(len(p)==8):
		p[0] = (p[1],p[3],p[4],p[7])
	if(len(p)==6):
		p[0] = (p[1],p[2],p[3],p[5])
	if(len(p)==10):
		p[0] = (p[1],p[3],p[6],p[7],p[9])
	if(len(p)==11):
		p[0] = (p[1],p[3],p[4],p[7],p[8],p[10])
	if(len(p)==8 and p[5]=="else"):
		p[0] = (p[1],p[2],p[4],p[5],p[7])
	if(len(p)==9):
		p[0] = (p[1],p[2],p[3],p[5],p[6],p[8])
	if(len(p)==16):
		p[0] = (p[1],p[3],p[6],p[7],p[9],p[12],p[13],p[15])
	if(len(p)==18):
		p[0] = (p[1],p[3],p[4],p[7],p[8],p[10],p[11],p[14],p[15],p[17])
	if(len(p)==12):
		p[0] = (p[1],p[2],p[4],p[5],p[6],p[8],p[9],p[11])
	if(len(p)==14):
		p[0] = (p[1],p[2],p[3],p[5],p[6],p[7],p[8],p[10],p[11],p[13])
	if(len(p)==13):
		p[0] = (p[1],p[3],p[6],p[7],p[9],p[12])
	if(len(p)==15):
		p[0] = (p[1],p[3],p[4],p[7],p[8],p[10],p[11],p[14])
	if(len(p) == 9 and p[5]=='elif'):
		p[0] = (p[1], p[2], p[4], p[5], p[6], p[8])
	if(len(p)==11 and p[6]=='elif'):
		p[0] = (p[1],p[2],p[3],p[5],p[6],p[7],p[8],p[10])
def p_error(p):		#funcion que se ejecuta en caso de generarse un error en la ejecucion de ejecutar_yacc(s)
    if p is not None:
        errors_list.append(p.type)
    else:
        print("No se ingreso nada")

yacc.yacc()

def ejecutar_yacc(s):		#funcion que realiza el arbol sintactico del programa
	result = yacc.parse(s)
	return result

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