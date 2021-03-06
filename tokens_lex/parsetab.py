
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS BREAK COMILLA COMILLAD COMMA DEF DEQUALS DIC DIFFERENT DIVIDE DIVIDEINT DPOINT ELIF ELSE EQUALS EXPONENT FALSE FOR FROM HIGHER HIGHEREQ IF IMPORT IN IS LCORCHETE LEN LESS LESSEQ LIST LPAREN MINUS MODULE NAME NONE NOT NUMBER OR PLUS PRINT RANGE RCORCHETE RETURN RPAREN SET THEN TIMES TRUE TUPLE WHILEsentencia : assign\n\t| for\n\t| while\n\t| if\n\t| assign sentencia\n\t\t\t\t | for sentencia\n\t\t\t\t | while sentencia\n\t\t\t\t | if sentenciaassign : NAME EQUALS expr\n\t\t\t  | NAME EQUALS list\n\t\t\t  | NAME EQUALS cadexpr : expr PLUS term\n\t\t\t| expr MINUS term\n\t\t\t| termterm : term TIMES factor\n\t\t\t| term DIVIDE factor\n\t\t\t| factorlist : LCORCHETE RCORCHETE\n\t\t\t| LCORCHETE element RCORCHETE\n\t\t\t| LCORCHETE element elements RCORCHETEelement : factor\n\t\t\t   | NAME\n\t\t\t   | listelements : COMMA element\n\t\t\t\t| COMMA list\n\t\t\t\t| COMMA element elementsfactor : NUMBER\n\t\t\t  | MINUS NUMBER\n\t\t\t  | NAMEcad : COMILLA str COMILLA\n\t\t   | COMILLAD str COMILLAD\n\t\t   | cad LCORCHETE index RCORCHETEstr : NAME\n\t\t   | NAME strindex : factor\n\t\t\t | factor DPOINT factor\n\t\t\t | factor DPOINT factor DPOINT factorwhile : WHILE LPAREN comparison RPAREN DPOINT sentencia\n\t\t\t | WHILE comparison DPOINT sentencia\n\t\t\t | WHILE LPAREN comparison comparisons RPAREN DPOINT sentencia\n\t\t\t | WHILE comparison comparisons DPOINT sentenciacomparisons : AND comparison\n\t\t\t\t   | AND comparison comparisons\n\t\t\t\t   | OR comparison\n\t\t\t\t   | OR comparison comparisonsbool : TRUE\n\t\t\t| FALSEcomparison : comp DEQUALS comp\n\t\t\t\t  | comp DIFFERENT comp\n\t\t\t\t  | comp HIGHER comp\n\t\t\t\t  | comp LESS comp\n\t\t\t\t  | comp HIGHEREQ  comp\n\t\t\t\t  | comp LESSEQ comp\n\t\t\t\t  | boolcomp : expr\n\t\t\t| element\n\t\t\t| boolfor : FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign\n\t\t   | FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign\n\t\t   | FOR NAME IN NAME DPOINT assignr_values : r_value COMMA r_value\n\t\t\t\t| r_value COMMA r_value COMMA r_valuer_value : factor\n\t\t\t   | LEN LPAREN NAME RPARENif : IF LPAREN comparison RPAREN DPOINT sentencia\n\t\t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia\n\t\t  | IF comparison DPOINT sentencia\n\t\t  | IF comparison comparisons DPOINT sentencia\n\t\t  | IF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF comparison DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia\n\t\t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia\n\t\t  | IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia\n\t\t  | IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia'
    
_lr_action_items = {'NAME':([0,2,3,4,5,7,8,9,10,11,12,13,14,16,24,29,30,31,33,34,35,36,37,38,39,40,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,61,63,65,71,72,82,83,84,85,86,88,91,92,95,97,98,99,100,102,105,108,111,112,113,114,115,120,121,123,124,125,128,131,133,134,137,138,139,140,142,143,145,147,148,151,152,155,156,157,159,161,162,164,167,169,170,171,173,175,177,179,180,181,182,183,185,186,],[6,6,6,6,6,15,27,27,-5,-6,-7,-8,33,27,-14,-27,27,27,-29,-9,-10,-11,65,65,-17,67,6,27,27,27,27,27,27,27,27,33,33,33,33,-28,-18,6,33,65,-39,6,-12,-13,-15,-16,-19,27,-67,6,-30,-31,6,33,6,-41,-20,6,27,-68,-32,33,-60,-38,6,-65,6,6,27,33,146,-40,-66,-71,6,6,33,6,6,6,27,-79,-72,-58,33,-59,-69,6,27,6,-70,6,-80,6,-75,-77,6,6,-76,6,-78,-73,6,-74,]),'FOR':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,71,72,82,83,84,85,86,91,92,95,97,100,102,105,108,112,113,115,120,121,123,124,125,134,137,138,139,140,147,151,152,155,157,159,161,164,167,169,170,171,173,175,177,179,180,181,182,183,185,186,],[7,7,7,7,7,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,7,-28,-18,7,-39,7,-12,-13,-15,-16,-19,-67,7,-30,-31,7,-41,-20,7,-68,-32,-60,-38,7,-65,7,7,-40,-66,-71,7,7,7,-79,-72,-58,-59,-69,7,7,-70,7,-80,7,-75,-77,7,7,-76,7,-78,-73,7,-74,]),'WHILE':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,71,72,82,83,84,85,86,91,92,95,97,100,102,105,108,112,113,115,120,121,123,124,125,134,137,138,139,140,147,151,152,155,157,159,161,164,167,169,170,171,173,175,177,179,180,181,182,183,185,186,],[8,8,8,8,8,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,8,-28,-18,8,-39,8,-12,-13,-15,-16,-19,-67,8,-30,-31,8,-41,-20,8,-68,-32,-60,-38,8,-65,8,8,-40,-66,-71,8,8,8,-79,-72,-58,-59,-69,8,8,-70,8,-80,8,-75,-77,8,8,-76,8,-78,-73,8,-74,]),'IF':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,71,72,82,83,84,85,86,91,92,95,97,100,102,105,108,112,113,115,120,121,123,124,125,134,137,138,139,140,147,151,152,155,157,159,161,164,167,169,170,171,173,175,177,179,180,181,182,183,185,186,],[9,9,9,9,9,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,9,-28,-18,9,-39,9,-12,-13,-15,-16,-19,-67,9,-30,-31,9,-41,-20,9,-68,-32,-60,-38,9,-65,9,9,-40,-66,-71,9,9,9,-79,-72,-58,-59,-69,9,9,-70,9,-80,9,-75,-77,9,9,-76,9,-78,-73,9,-74,]),'$end':([1,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,71,82,83,84,85,86,91,95,97,102,105,112,113,115,120,123,134,137,138,151,152,155,157,159,167,170,173,175,180,182,183,186,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-39,-12,-13,-15,-16,-19,-67,-30,-31,-41,-20,-68,-32,-60,-38,-65,-40,-66,-71,-79,-72,-58,-59,-69,-70,-80,-75,-77,-76,-78,-73,-74,]),'ELSE':([2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,71,82,83,84,85,86,91,95,97,102,105,112,113,115,120,123,134,137,138,151,152,155,157,159,167,170,173,175,180,182,183,186,],[-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-39,-12,-13,-15,-16,-19,110,-30,-31,-41,-20,127,-32,-60,-38,135,-40,149,-71,163,-72,-58,-59,-69,-70,174,-75,178,-76,184,-73,-74,]),'ELIF':([2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,71,82,83,84,85,86,91,95,97,102,105,112,113,115,120,123,134,137,138,151,152,155,157,159,167,170,173,175,180,182,183,186,],[-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-39,-12,-13,-15,-16,-19,111,-30,-31,-41,-20,128,-32,-60,-38,136,-40,150,-71,-79,-72,-58,-59,-69,-70,-80,-75,-77,-76,-78,-73,-74,]),'EQUALS':([6,],[14,]),'LPAREN':([8,9,68,119,136,150,],[16,31,99,133,148,162,]),'TRUE':([8,9,16,31,44,45,46,47,48,49,50,51,111,128,148,162,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'FALSE':([8,9,16,31,44,45,46,47,48,49,50,51,111,128,148,162,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'NUMBER':([8,9,14,16,25,30,31,44,45,46,47,48,49,50,51,52,53,54,55,63,88,99,111,114,128,131,142,148,156,162,],[29,29,29,29,56,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'MINUS':([8,9,14,16,20,24,26,27,29,30,31,33,34,39,44,45,46,47,48,49,50,51,52,53,54,55,56,63,82,83,84,85,88,99,111,114,128,131,142,148,156,162,],[25,25,25,25,53,-14,-17,-29,-27,25,25,-29,53,-17,25,25,25,25,25,25,25,25,25,25,25,25,-28,25,-12,-13,-15,-16,25,25,25,25,25,25,25,25,25,25,]),'LCORCHETE':([8,9,14,16,30,31,36,44,45,46,47,48,49,50,51,88,95,97,111,113,128,148,162,],[30,30,30,30,30,30,63,30,30,30,30,30,30,30,30,30,-30,-31,30,-32,30,30,30,]),'COMILLA':([14,64,65,96,],[37,95,-33,-34,]),'COMILLAD':([14,65,66,96,],[38,-33,97,-34,]),'IN':([15,],[40,]),'DPOINT':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,43,56,57,62,67,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,89,94,101,103,104,105,109,110,126,127,129,130,132,135,149,153,163,166,174,176,178,184,],[42,-54,-55,-56,-46,-47,-14,-17,-22,-23,-27,61,-29,-17,72,-28,-18,92,98,100,-42,-44,-48,-57,-49,-50,-51,-52,-53,-12,-13,-15,-16,-19,108,114,121,-43,-45,-20,124,125,139,140,142,143,145,147,161,164,169,171,177,179,181,185,]),'AND':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,41,56,57,60,73,74,75,76,77,78,79,80,81,82,83,84,85,86,105,141,168,],[44,-54,-55,-56,-46,-47,-14,-17,-22,-23,-27,44,-29,-17,44,-28,-18,44,44,44,-48,-57,-49,-50,-51,-52,-53,-12,-13,-15,-16,-19,-20,44,44,]),'OR':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,41,56,57,60,73,74,75,76,77,78,79,80,81,82,83,84,85,86,105,141,168,],[45,-54,-55,-56,-46,-47,-14,-17,-22,-23,-27,45,-29,-17,45,-28,-18,45,45,45,-48,-57,-49,-50,-51,-52,-53,-12,-13,-15,-16,-19,-20,45,45,]),'DEQUALS':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,82,83,84,85,86,105,],[46,-57,-55,-56,-46,-47,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'DIFFERENT':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,82,83,84,85,86,105,],[47,-57,-55,-56,-46,-47,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'HIGHER':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,82,83,84,85,86,105,],[48,-57,-55,-56,-46,-47,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'LESS':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,82,83,84,85,86,105,],[49,-57,-55,-56,-46,-47,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'HIGHEREQ':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,82,83,84,85,86,105,],[50,-57,-55,-56,-46,-47,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'LESSEQ':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,82,83,84,85,86,105,],[51,-57,-55,-56,-46,-47,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'RPAREN':([19,20,21,22,23,24,26,27,28,29,33,39,41,56,57,60,70,73,74,75,76,77,78,79,80,81,82,83,84,85,86,90,103,104,105,116,117,118,144,146,158,160,165,172,],[-54,-55,-56,-46,-47,-14,-17,-22,-23,-27,-29,-17,69,-28,-18,89,101,-42,-44,-48,-57,-49,-50,-51,-52,-53,-12,-13,-15,-16,-19,109,-43,-45,-20,130,132,-63,-61,158,-64,166,-62,176,]),'PLUS':([20,24,26,27,29,33,34,39,56,82,83,84,85,],[52,-14,-17,-29,-27,-29,52,-17,-28,-12,-13,-15,-16,]),'TIMES':([24,26,27,29,33,39,56,82,83,84,85,],[54,-17,-29,-27,-29,-17,-28,54,54,-15,-16,]),'DIVIDE':([24,26,27,29,33,39,56,82,83,84,85,],[55,-17,-29,-27,-29,-17,-28,55,55,-15,-16,]),'RCORCHETE':([27,28,29,30,33,56,57,58,59,86,87,93,94,105,106,107,122,129,154,],[-22,-23,-27,57,-29,-28,-18,86,-21,-19,105,113,-35,-20,-24,-23,-26,-36,-37,]),'COMMA':([27,28,29,33,56,57,58,59,86,105,106,107,116,118,144,158,],[-22,-23,-27,-29,-28,-18,88,-21,-19,-20,88,-23,131,-63,156,-64,]),'RANGE':([40,],[68,]),'LEN':([99,131,156,],[119,119,119,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,2,3,4,5,42,61,72,92,100,108,121,124,125,139,140,147,161,164,169,171,177,179,181,185,],[1,10,11,12,13,71,91,102,112,120,123,134,137,138,151,152,159,167,170,173,175,180,182,183,186,]),'assign':([0,2,3,4,5,42,61,72,92,98,100,108,121,124,125,139,140,143,145,147,161,164,169,171,177,179,181,185,],[2,2,2,2,2,2,2,2,2,115,2,2,2,2,2,2,2,155,157,2,2,2,2,2,2,2,2,2,]),'for':([0,2,3,4,5,42,61,72,92,100,108,121,124,125,139,140,147,161,164,169,171,177,179,181,185,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'while':([0,2,3,4,5,42,61,72,92,100,108,121,124,125,139,140,147,161,164,169,171,177,179,181,185,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'if':([0,2,3,4,5,42,61,72,92,100,108,121,124,125,139,140,147,161,164,169,171,177,179,181,185,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'comparison':([8,9,16,31,44,45,111,128,148,162,],[17,32,41,60,73,74,126,141,160,168,]),'comp':([8,9,16,31,44,45,46,47,48,49,50,51,111,128,148,162,],[18,18,18,18,18,18,75,77,78,79,80,81,18,18,18,18,]),'bool':([8,9,16,31,44,45,46,47,48,49,50,51,111,128,148,162,],[19,19,19,19,19,19,76,76,76,76,76,76,19,19,19,19,]),'expr':([8,9,14,16,31,44,45,46,47,48,49,50,51,111,128,148,162,],[20,20,34,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'element':([8,9,16,30,31,44,45,46,47,48,49,50,51,88,111,128,148,162,],[21,21,21,58,21,21,21,21,21,21,21,21,21,106,21,21,21,21,]),'term':([8,9,14,16,31,44,45,46,47,48,49,50,51,52,53,111,128,148,162,],[24,24,24,24,24,24,24,24,24,24,24,24,24,82,83,24,24,24,24,]),'factor':([8,9,14,16,30,31,44,45,46,47,48,49,50,51,52,53,54,55,63,88,99,111,114,128,131,142,148,156,162,],[26,26,39,26,59,26,26,26,26,26,26,26,26,26,39,39,84,85,94,59,118,26,129,26,118,154,26,118,26,]),'list':([8,9,14,16,30,31,44,45,46,47,48,49,50,51,88,111,128,148,162,],[28,28,35,28,28,28,28,28,28,28,28,28,28,28,107,28,28,28,28,]),'cad':([14,],[36,]),'comparisons':([17,32,41,60,73,74,141,168,],[43,62,70,90,103,104,153,172,]),'str':([37,38,65,],[64,66,96,]),'elements':([58,106,],[87,122,]),'index':([63,],[93,]),'r_value':([99,131,156,],[116,144,165,]),'r_values':([99,],[117,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> sentencia","S'",1,None,None,None),
  ('sentencia -> assign','sentencia',1,'p_sentencia','sintactico.py',7),
  ('sentencia -> for','sentencia',1,'p_sentencia','sintactico.py',8),
  ('sentencia -> while','sentencia',1,'p_sentencia','sintactico.py',9),
  ('sentencia -> if','sentencia',1,'p_sentencia','sintactico.py',10),
  ('sentencia -> assign sentencia','sentencia',2,'p_sentencia','sintactico.py',11),
  ('sentencia -> for sentencia','sentencia',2,'p_sentencia','sintactico.py',12),
  ('sentencia -> while sentencia','sentencia',2,'p_sentencia','sintactico.py',13),
  ('sentencia -> if sentencia','sentencia',2,'p_sentencia','sintactico.py',14),
  ('assign -> NAME EQUALS expr','assign',3,'p_assign','sintactico.py',22),
  ('assign -> NAME EQUALS list','assign',3,'p_assign','sintactico.py',23),
  ('assign -> NAME EQUALS cad','assign',3,'p_assign','sintactico.py',24),
  ('expr -> expr PLUS term','expr',3,'p_expr','sintactico.py',49),
  ('expr -> expr MINUS term','expr',3,'p_expr','sintactico.py',50),
  ('expr -> term','expr',1,'p_expr','sintactico.py',51),
  ('term -> term TIMES factor','term',3,'p_term','sintactico.py',58),
  ('term -> term DIVIDE factor','term',3,'p_term','sintactico.py',59),
  ('term -> factor','term',1,'p_term','sintactico.py',60),
  ('list -> LCORCHETE RCORCHETE','list',2,'p_list','sintactico.py',67),
  ('list -> LCORCHETE element RCORCHETE','list',3,'p_list','sintactico.py',68),
  ('list -> LCORCHETE element elements RCORCHETE','list',4,'p_list','sintactico.py',69),
  ('element -> factor','element',1,'p_element','sintactico.py',82),
  ('element -> NAME','element',1,'p_element','sintactico.py',83),
  ('element -> list','element',1,'p_element','sintactico.py',84),
  ('elements -> COMMA element','elements',2,'p_elements','sintactico.py',88),
  ('elements -> COMMA list','elements',2,'p_elements','sintactico.py',89),
  ('elements -> COMMA element elements','elements',3,'p_elements','sintactico.py',90),
  ('factor -> NUMBER','factor',1,'p_factor','sintactico.py',97),
  ('factor -> MINUS NUMBER','factor',2,'p_factor','sintactico.py',98),
  ('factor -> NAME','factor',1,'p_factor','sintactico.py',99),
  ('cad -> COMILLA str COMILLA','cad',3,'p_cad','sintactico.py',106),
  ('cad -> COMILLAD str COMILLAD','cad',3,'p_cad','sintactico.py',107),
  ('cad -> cad LCORCHETE index RCORCHETE','cad',4,'p_cad','sintactico.py',108),
  ('str -> NAME','str',1,'p_str','sintactico.py',112),
  ('str -> NAME str','str',2,'p_str','sintactico.py',113),
  ('index -> factor','index',1,'p_index','sintactico.py',116),
  ('index -> factor DPOINT factor','index',3,'p_index','sintactico.py',117),
  ('index -> factor DPOINT factor DPOINT factor','index',5,'p_index','sintactico.py',118),
  ('while -> WHILE LPAREN comparison RPAREN DPOINT sentencia','while',6,'p_while','sintactico.py',131),
  ('while -> WHILE comparison DPOINT sentencia','while',4,'p_while','sintactico.py',132),
  ('while -> WHILE LPAREN comparison comparisons RPAREN DPOINT sentencia','while',7,'p_while','sintactico.py',133),
  ('while -> WHILE comparison comparisons DPOINT sentencia','while',5,'p_while','sintactico.py',134),
  ('comparisons -> AND comparison','comparisons',2,'p_comparisons','sintactico.py',145),
  ('comparisons -> AND comparison comparisons','comparisons',3,'p_comparisons','sintactico.py',146),
  ('comparisons -> OR comparison','comparisons',2,'p_comparisons','sintactico.py',147),
  ('comparisons -> OR comparison comparisons','comparisons',3,'p_comparisons','sintactico.py',148),
  ('bool -> TRUE','bool',1,'p_bool','sintactico.py',155),
  ('bool -> FALSE','bool',1,'p_bool','sintactico.py',156),
  ('comparison -> comp DEQUALS comp','comparison',3,'p_comparison','sintactico.py',161),
  ('comparison -> comp DIFFERENT comp','comparison',3,'p_comparison','sintactico.py',162),
  ('comparison -> comp HIGHER comp','comparison',3,'p_comparison','sintactico.py',163),
  ('comparison -> comp LESS comp','comparison',3,'p_comparison','sintactico.py',164),
  ('comparison -> comp HIGHEREQ comp','comparison',3,'p_comparison','sintactico.py',165),
  ('comparison -> comp LESSEQ comp','comparison',3,'p_comparison','sintactico.py',166),
  ('comparison -> bool','comparison',1,'p_comparison','sintactico.py',167),
  ('comp -> expr','comp',1,'p_comp','sintactico.py',174),
  ('comp -> element','comp',1,'p_comp','sintactico.py',175),
  ('comp -> bool','comp',1,'p_comp','sintactico.py',176),
  ('for -> FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign','for',9,'p_for','sintactico.py',180),
  ('for -> FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign','for',9,'p_for','sintactico.py',181),
  ('for -> FOR NAME IN NAME DPOINT assign','for',6,'p_for','sintactico.py',182),
  ('r_values -> r_value COMMA r_value','r_values',3,'p_r_values','sintactico.py',189),
  ('r_values -> r_value COMMA r_value COMMA r_value','r_values',5,'p_r_values','sintactico.py',190),
  ('r_value -> factor','r_value',1,'p_r_value','sintactico.py',197),
  ('r_value -> LEN LPAREN NAME RPAREN','r_value',4,'p_r_value','sintactico.py',198),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia','if',6,'p_if','sintactico.py',205),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia','if',7,'p_if','sintactico.py',206),
  ('if -> IF comparison DPOINT sentencia','if',4,'p_if','sintactico.py',207),
  ('if -> IF comparison comparisons DPOINT sentencia','if',5,'p_if','sintactico.py',208),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',9,'p_if','sintactico.py',209),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',10,'p_if','sintactico.py',210),
  ('if -> IF comparison DPOINT sentencia ELSE DPOINT sentencia','if',7,'p_if','sintactico.py',211),
  ('if -> IF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia','if',8,'p_if','sintactico.py',212),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',15,'p_if','sintactico.py',213),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',17,'p_if','sintactico.py',214),
  ('if -> IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia ELSE DPOINT sentencia','if',11,'p_if','sintactico.py',215),
  ('if -> IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia','if',13,'p_if','sintactico.py',216),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia','if',12,'p_if','sintactico.py',217),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia','if',14,'p_if','sintactico.py',218),
  ('if -> IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia','if',8,'p_if','sintactico.py',219),
  ('if -> IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia','if',10,'p_if','sintactico.py',220),
]
