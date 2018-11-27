import ply.yacc as yacc
import lexico

tokens = lexico.tokens

def p_assign(p):
	'''assign : NAME EQUALS expr'''
	p[0] = ('ASSIGN',p[1],p[3])

def p_expr_plus(p):
	'''expr : expr PLUS term'''
	p[0] = ('+',p[1],p[3])

def p_term_mul(p):
	'''term : term TIMES factor'''
	p[0] = ('*',p[1],p[3])

def p_term_factor(p):
	'''term : factor'''
	p[0] = p[1]

def p_factor(p):
	'''factor : NUMBER'''
	p[0] = ('NUM',p[1])

yacc.yacc()

while 1:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    yacc.parse(s)