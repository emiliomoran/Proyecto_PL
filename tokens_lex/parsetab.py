
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS BREAK COMILLA COMILLAD COMMA DEF DEQUALS DIC DIFFERENT DIVIDE DIVIDEINT DPOINT ELIF ELSE EQUALS EXPONENT FALSE FOR FROM HIGHER HIGHEREQ IF IMPORT IN IS LCORCHETE LEN LESS LESSEQ LIST LPAREN MINUS MODULE NAME NONE NOT NUMBER OR PLUS PRINT RANGE RCORCHETE RETURN RPAREN SET THEN TIMES TRUE TUPLE WHILEsentencia : assign\n\t\t\t\t | for\n\t\t\t\t | while\n\t\t\t\t | if\n\t\t\t\t | assign sentencia\n\t\t\t\t | for sentencia\n\t\t\t\t | while sentencia\n\t\t\t\t | if sentenciaassign : NAME EQUALS expr\n\t\t\t  | NAME EQUALS list\n\t\t\t  | NAME EQUALS cadexpr : expr PLUS term\n\t\t\t| expr MINUS term\n\t\t\t| termterm : term TIMES factor\n\t\t\t| term DIVIDE factor\n\t\t\t| factorlist : LCORCHETE RCORCHETE\n\t\t\t| LCORCHETE element RCORCHETE\n\t\t\t| LCORCHETE element elements RCORCHETEelement : factor\n\t\t\t   | NAME\n\t\t\t   | listelements : COMMA element\n\t\t\t\t| COMMA list\n\t\t\t\t| COMMA element elementsfactor : NUMBER\n\t\t\t  | MINUS NUMBER\n\t\t\t  | NAMEcad : COMILLA NAME COMILLA\n\t\t   | COMILLAD NAME COMILLAD\n\t\t   | cad LCORCHETE index RCORCHETEindex : factor\n\t\t\t | factor DPOINT factor\n\t\t\t | factor DPOINT factor DPOINT factorwhile : WHILE LPAREN comparison RPAREN DPOINT sentencia\n\t\t\t | WHILE comparison DPOINT sentencia\n\t\t\t | WHILE LPAREN comparison comparisons RPAREN DPOINT sentencia\n\t\t\t | WHILE comparison comparisons DPOINT sentenciacomparisons : AND comparison\n\t\t\t\t   | AND comparison comparisons\n\t\t\t\t   | OR comparison\n\t\t\t\t   | OR comparison comparisonsbool : TRUE\n\t\t\t| FALSEcomparison : comp DEQUALS comp\n                  | comp DIFFERENT comp\n                  | comp HIGHER comp\n                  | comp LESS comp\n                  | comp HIGHEREQ  comp\n                  | comp LESSEQ comp\n                  | boolcomp : expr\n\t\t\t| element\n\t\t\t| boolfor : FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign\n\t\t   | FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign\n\t\t   | FOR NAME IN NAME DPOINT assignr_values : r_value COMMA r_value\n\t\t\t\t| r_value COMMA r_value COMMA r_valuer_value : factor\n\t\t\t   | LEN LPAREN NAME RPARENif : IF LPAREN comparison RPAREN DPOINT sentencia\n    \t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia\n    \t  | IF comparison DPOINT sentencia\n    \t  | IF comparison comparisons DPOINT sentencia\n    \t  | IF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia\n    \t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia\n    \t  | IF comparison DPOINT sentencia ELSE DPOINT sentencia\n    \t  | IF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia\n    \t  | IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia\n    \t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia\n    \t  | IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia ELSE DPOINT sentencia\n    \t  | IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia'
    
_lr_action_items = {'NAME':([0,2,3,4,5,7,8,9,10,11,12,13,14,16,24,29,30,31,33,34,35,36,37,38,39,40,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,61,63,70,71,81,82,83,84,85,87,90,91,94,95,96,97,98,100,103,106,109,110,111,112,113,118,119,121,122,123,126,129,131,132,135,136,137,138,140,141,143,145,146,150,153,154,155,157,159,160,162,165,167,169,171,175,177,178,179,181,183,184,],[6,6,6,6,6,15,27,27,-5,-6,-7,-8,33,27,-14,-27,27,27,-29,-9,-10,-11,64,65,-17,66,6,27,27,27,27,27,27,27,27,33,33,33,33,-28,-18,6,33,-37,6,-12,-13,-15,-16,-19,27,-65,6,-30,-31,6,33,6,-39,-20,6,27,-66,-32,33,-58,-36,6,-63,6,6,27,33,144,-38,-64,-69,6,6,33,6,6,6,27,-70,-56,33,-57,-67,6,27,6,-68,6,6,-73,6,6,-74,6,-71,6,-72,]),'FOR':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,70,71,81,82,83,84,85,90,91,94,95,98,100,103,106,110,111,113,118,119,121,122,123,132,135,136,137,138,145,150,153,155,157,159,162,165,167,169,171,175,177,178,179,181,183,184,],[7,7,7,7,7,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,7,-28,-18,7,-37,7,-12,-13,-15,-16,-19,-65,7,-30,-31,7,-39,-20,7,-66,-32,-58,-36,7,-63,7,7,-38,-64,-69,7,7,7,-70,-56,-57,-67,7,7,-68,7,7,-73,7,7,-74,7,-71,7,-72,]),'WHILE':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,70,71,81,82,83,84,85,90,91,94,95,98,100,103,106,110,111,113,118,119,121,122,123,132,135,136,137,138,145,150,153,155,157,159,162,165,167,169,171,175,177,178,179,181,183,184,],[8,8,8,8,8,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,8,-28,-18,8,-37,8,-12,-13,-15,-16,-19,-65,8,-30,-31,8,-39,-20,8,-66,-32,-58,-36,8,-63,8,8,-38,-64,-69,8,8,8,-70,-56,-57,-67,8,8,-68,8,8,-73,8,8,-74,8,-71,8,-72,]),'IF':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,70,71,81,82,83,84,85,90,91,94,95,98,100,103,106,110,111,113,118,119,121,122,123,132,135,136,137,138,145,150,153,155,157,159,162,165,167,169,171,175,177,178,179,181,183,184,],[9,9,9,9,9,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,9,-28,-18,9,-37,9,-12,-13,-15,-16,-19,-65,9,-30,-31,9,-39,-20,9,-66,-32,-58,-36,9,-63,9,9,-38,-64,-69,9,9,9,-70,-56,-57,-67,9,9,-68,9,9,-73,9,9,-74,9,-71,9,-72,]),'$end':([1,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,70,81,82,83,84,85,90,94,95,100,103,110,111,113,118,121,132,135,136,150,153,155,157,165,171,178,181,184,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-37,-12,-13,-15,-16,-19,-65,-30,-31,-39,-20,-66,-32,-58,-36,-63,-38,-64,-69,-70,-56,-57,-67,-68,-73,-74,-71,-72,]),'ELSE':([2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,70,81,82,83,84,85,90,94,95,100,103,110,111,113,118,121,132,135,136,149,150,153,155,157,165,168,171,173,178,180,181,184,],[-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-37,-12,-13,-15,-16,-19,108,-30,-31,-39,-20,125,-32,-58,-36,133,-38,147,-69,161,-70,-56,-57,-67,-68,172,-73,176,-74,182,-71,-72,]),'ELIF':([2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,70,81,82,83,84,85,90,94,95,100,103,110,111,113,118,121,132,135,136,150,153,155,157,165,171,178,181,184,],[-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-37,-12,-13,-15,-16,-19,109,-30,-31,-39,-20,126,-32,-58,-36,134,-38,148,-69,-70,-56,-57,-67,-68,-73,-74,-71,-72,]),'EQUALS':([6,],[14,]),'LPAREN':([8,9,67,117,134,148,],[16,31,97,131,146,160,]),'TRUE':([8,9,16,31,44,45,46,47,48,49,50,51,109,126,146,160,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'FALSE':([8,9,16,31,44,45,46,47,48,49,50,51,109,126,146,160,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'NUMBER':([8,9,14,16,25,30,31,44,45,46,47,48,49,50,51,52,53,54,55,63,87,97,109,112,126,129,140,146,154,160,],[29,29,29,29,56,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'MINUS':([8,9,14,16,20,24,26,27,29,30,31,33,34,39,44,45,46,47,48,49,50,51,52,53,54,55,56,63,81,82,83,84,87,97,109,112,126,129,140,146,154,160,],[25,25,25,25,53,-14,-17,-29,-27,25,25,-29,53,-17,25,25,25,25,25,25,25,25,25,25,25,25,-28,25,-12,-13,-15,-16,25,25,25,25,25,25,25,25,25,25,]),'LCORCHETE':([8,9,14,16,30,31,36,44,45,46,47,48,49,50,51,87,94,95,109,111,126,146,160,],[30,30,30,30,30,30,63,30,30,30,30,30,30,30,30,30,-30,-31,30,-32,30,30,30,]),'COMILLA':([14,64,],[37,94,]),'COMILLAD':([14,65,],[38,95,]),'IN':([15,],[40,]),'DPOINT':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,43,56,57,62,66,68,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,93,99,101,102,103,107,108,124,125,127,128,130,133,147,151,161,164,172,174,176,182,],[42,-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,61,-29,-17,71,-28,-18,91,96,98,-40,-42,-46,-55,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,106,112,119,-41,-43,-20,122,123,137,138,140,141,143,145,159,162,167,169,175,177,179,183,]),'AND':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,41,56,57,60,72,73,74,75,76,77,78,79,80,81,82,83,84,85,103,139,166,],[44,-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,44,-29,-17,44,-28,-18,44,44,44,-46,-55,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,-20,44,44,]),'OR':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,41,56,57,60,72,73,74,75,76,77,78,79,80,81,82,83,84,85,103,139,166,],[45,-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,45,-29,-17,45,-28,-18,45,45,45,-46,-55,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,-20,45,45,]),'DEQUALS':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,81,82,83,84,85,103,],[46,-55,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'DIFFERENT':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,81,82,83,84,85,103,],[47,-55,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'HIGHER':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,81,82,83,84,85,103,],[48,-55,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'LESS':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,81,82,83,84,85,103,],[49,-55,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'HIGHEREQ':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,81,82,83,84,85,103,],[50,-55,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'LESSEQ':([18,19,20,21,22,23,24,26,27,28,29,33,39,56,57,81,82,83,84,85,103,],[51,-55,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'RPAREN':([19,20,21,22,23,24,26,27,28,29,33,39,41,56,57,60,69,72,73,74,75,76,77,78,79,80,81,82,83,84,85,89,101,102,103,114,115,116,142,144,156,158,163,170,],[-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,68,-28,-18,88,99,-40,-42,-46,-55,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,107,-41,-43,-20,128,130,-61,-59,156,-62,164,-60,174,]),'PLUS':([20,24,26,27,29,33,34,39,56,81,82,83,84,],[52,-14,-17,-29,-27,-29,52,-17,-28,-12,-13,-15,-16,]),'TIMES':([24,26,27,29,33,39,56,81,82,83,84,],[54,-17,-29,-27,-29,-17,-28,54,54,-15,-16,]),'DIVIDE':([24,26,27,29,33,39,56,81,82,83,84,],[55,-17,-29,-27,-29,-17,-28,55,55,-15,-16,]),'RCORCHETE':([27,28,29,30,33,56,57,58,59,85,86,92,93,103,104,105,120,127,152,],[-22,-23,-27,57,-29,-28,-18,85,-21,-19,103,111,-33,-20,-24,-23,-26,-34,-35,]),'COMMA':([27,28,29,33,56,57,58,59,85,103,104,105,114,116,142,156,],[-22,-23,-27,-29,-28,-18,87,-21,-19,-20,87,-23,129,-61,154,-62,]),'RANGE':([40,],[67,]),'LEN':([97,129,154,],[117,117,117,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,2,3,4,5,42,61,71,91,98,106,119,122,123,137,138,145,159,162,167,169,175,177,179,183,],[1,10,11,12,13,70,90,100,110,118,121,132,135,136,149,150,157,165,168,171,173,178,180,181,184,]),'assign':([0,2,3,4,5,42,61,71,91,96,98,106,119,122,123,137,138,141,143,145,159,162,167,169,175,177,179,183,],[2,2,2,2,2,2,2,2,2,113,2,2,2,2,2,2,2,153,155,2,2,2,2,2,2,2,2,2,]),'for':([0,2,3,4,5,42,61,71,91,98,106,119,122,123,137,138,145,159,162,167,169,175,177,179,183,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'while':([0,2,3,4,5,42,61,71,91,98,106,119,122,123,137,138,145,159,162,167,169,175,177,179,183,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'if':([0,2,3,4,5,42,61,71,91,98,106,119,122,123,137,138,145,159,162,167,169,175,177,179,183,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'comparison':([8,9,16,31,44,45,109,126,146,160,],[17,32,41,60,72,73,124,139,158,166,]),'comp':([8,9,16,31,44,45,46,47,48,49,50,51,109,126,146,160,],[18,18,18,18,18,18,74,76,77,78,79,80,18,18,18,18,]),'bool':([8,9,16,31,44,45,46,47,48,49,50,51,109,126,146,160,],[19,19,19,19,19,19,75,75,75,75,75,75,19,19,19,19,]),'expr':([8,9,14,16,31,44,45,46,47,48,49,50,51,109,126,146,160,],[20,20,34,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'element':([8,9,16,30,31,44,45,46,47,48,49,50,51,87,109,126,146,160,],[21,21,21,58,21,21,21,21,21,21,21,21,21,104,21,21,21,21,]),'term':([8,9,14,16,31,44,45,46,47,48,49,50,51,52,53,109,126,146,160,],[24,24,24,24,24,24,24,24,24,24,24,24,24,81,82,24,24,24,24,]),'factor':([8,9,14,16,30,31,44,45,46,47,48,49,50,51,52,53,54,55,63,87,97,109,112,126,129,140,146,154,160,],[26,26,39,26,59,26,26,26,26,26,26,26,26,26,39,39,83,84,93,59,116,26,127,26,116,152,26,116,26,]),'list':([8,9,14,16,30,31,44,45,46,47,48,49,50,51,87,109,126,146,160,],[28,28,35,28,28,28,28,28,28,28,28,28,28,28,105,28,28,28,28,]),'cad':([14,],[36,]),'comparisons':([17,32,41,60,72,73,139,166,],[43,62,69,89,101,102,151,170,]),'elements':([58,104,],[86,120,]),'index':([63,],[92,]),'r_value':([97,129,154,],[114,142,163,]),'r_values':([97,],[115,]),}

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
  ('assign -> NAME EQUALS expr','assign',3,'p_assign','sintactico.py',23),
  ('assign -> NAME EQUALS list','assign',3,'p_assign','sintactico.py',24),
  ('assign -> NAME EQUALS cad','assign',3,'p_assign','sintactico.py',25),
  ('expr -> expr PLUS term','expr',3,'p_expr','sintactico.py',50),
  ('expr -> expr MINUS term','expr',3,'p_expr','sintactico.py',51),
  ('expr -> term','expr',1,'p_expr','sintactico.py',52),
  ('term -> term TIMES factor','term',3,'p_term','sintactico.py',59),
  ('term -> term DIVIDE factor','term',3,'p_term','sintactico.py',60),
  ('term -> factor','term',1,'p_term','sintactico.py',61),
  ('list -> LCORCHETE RCORCHETE','list',2,'p_list','sintactico.py',68),
  ('list -> LCORCHETE element RCORCHETE','list',3,'p_list','sintactico.py',69),
  ('list -> LCORCHETE element elements RCORCHETE','list',4,'p_list','sintactico.py',70),
  ('element -> factor','element',1,'p_element','sintactico.py',83),
  ('element -> NAME','element',1,'p_element','sintactico.py',84),
  ('element -> list','element',1,'p_element','sintactico.py',85),
  ('elements -> COMMA element','elements',2,'p_elements','sintactico.py',89),
  ('elements -> COMMA list','elements',2,'p_elements','sintactico.py',90),
  ('elements -> COMMA element elements','elements',3,'p_elements','sintactico.py',91),
  ('factor -> NUMBER','factor',1,'p_factor','sintactico.py',98),
  ('factor -> MINUS NUMBER','factor',2,'p_factor','sintactico.py',99),
  ('factor -> NAME','factor',1,'p_factor','sintactico.py',100),
  ('cad -> COMILLA NAME COMILLA','cad',3,'p_cad','sintactico.py',107),
  ('cad -> COMILLAD NAME COMILLAD','cad',3,'p_cad','sintactico.py',108),
  ('cad -> cad LCORCHETE index RCORCHETE','cad',4,'p_cad','sintactico.py',109),
  ('index -> factor','index',1,'p_index','sintactico.py',119),
  ('index -> factor DPOINT factor','index',3,'p_index','sintactico.py',120),
  ('index -> factor DPOINT factor DPOINT factor','index',5,'p_index','sintactico.py',121),
  ('while -> WHILE LPAREN comparison RPAREN DPOINT sentencia','while',6,'p_while','sintactico.py',134),
  ('while -> WHILE comparison DPOINT sentencia','while',4,'p_while','sintactico.py',135),
  ('while -> WHILE LPAREN comparison comparisons RPAREN DPOINT sentencia','while',7,'p_while','sintactico.py',136),
  ('while -> WHILE comparison comparisons DPOINT sentencia','while',5,'p_while','sintactico.py',137),
  ('comparisons -> AND comparison','comparisons',2,'p_comparisons','sintactico.py',148),
  ('comparisons -> AND comparison comparisons','comparisons',3,'p_comparisons','sintactico.py',149),
  ('comparisons -> OR comparison','comparisons',2,'p_comparisons','sintactico.py',150),
  ('comparisons -> OR comparison comparisons','comparisons',3,'p_comparisons','sintactico.py',151),
  ('bool -> TRUE','bool',1,'p_bool','sintactico.py',158),
  ('bool -> FALSE','bool',1,'p_bool','sintactico.py',159),
  ('comparison -> comp DEQUALS comp','comparison',3,'p_comparison','sintactico.py',164),
  ('comparison -> comp DIFFERENT comp','comparison',3,'p_comparison','sintactico.py',165),
  ('comparison -> comp HIGHER comp','comparison',3,'p_comparison','sintactico.py',166),
  ('comparison -> comp LESS comp','comparison',3,'p_comparison','sintactico.py',167),
  ('comparison -> comp HIGHEREQ comp','comparison',3,'p_comparison','sintactico.py',168),
  ('comparison -> comp LESSEQ comp','comparison',3,'p_comparison','sintactico.py',169),
  ('comparison -> bool','comparison',1,'p_comparison','sintactico.py',170),
  ('comp -> expr','comp',1,'p_comp','sintactico.py',177),
  ('comp -> element','comp',1,'p_comp','sintactico.py',178),
  ('comp -> bool','comp',1,'p_comp','sintactico.py',179),
  ('for -> FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign','for',9,'p_for','sintactico.py',183),
  ('for -> FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign','for',9,'p_for','sintactico.py',184),
  ('for -> FOR NAME IN NAME DPOINT assign','for',6,'p_for','sintactico.py',185),
  ('r_values -> r_value COMMA r_value','r_values',3,'p_r_values','sintactico.py',192),
  ('r_values -> r_value COMMA r_value COMMA r_value','r_values',5,'p_r_values','sintactico.py',193),
  ('r_value -> factor','r_value',1,'p_r_value','sintactico.py',200),
  ('r_value -> LEN LPAREN NAME RPAREN','r_value',4,'p_r_value','sintactico.py',201),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia','if',6,'p_if','sintactico.py',208),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia','if',7,'p_if','sintactico.py',209),
  ('if -> IF comparison DPOINT sentencia','if',4,'p_if','sintactico.py',210),
  ('if -> IF comparison comparisons DPOINT sentencia','if',5,'p_if','sintactico.py',211),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',9,'p_if','sintactico.py',212),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',10,'p_if','sintactico.py',213),
  ('if -> IF comparison DPOINT sentencia ELSE DPOINT sentencia','if',7,'p_if','sintactico.py',214),
  ('if -> IF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia','if',8,'p_if','sintactico.py',215),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',15,'p_if','sintactico.py',216),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',17,'p_if','sintactico.py',217),
  ('if -> IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia ELSE DPOINT sentencia','if',11,'p_if','sintactico.py',218),
  ('if -> IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia','if',13,'p_if','sintactico.py',219),
]
