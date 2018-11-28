
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND AS BREAK COMILLA COMILLAD COMMA DEF DEQUALS DIC DIFFERENT DIVIDE DIVIDEINT DPOINT ELIF ELSE EQUALS EXPONENT FALSE FOR FROM HIGHER HIGHEREQ IF IMPORT IN IS LCORCHETE LEN LESS LESSEQ LIST LPAREN MINUS MODULE NAME NONE NOT NUMBER OR PLUS PRINT RANGE RCORCHETE RETURN RPAREN SET THEN TIMES TRUE TUPLE WHILEsentencia : assign\n\t\t\t\t | for\n\t\t\t\t | while\n\t\t\t\t | if\n\t\t\t\t | assign sentencia\n\t\t\t\t | for sentencia\n\t\t\t\t | while sentencia\n\t\t\t\t | if sentenciaassign : NAME EQUALS expr\n\t\t\t  | NAME EQUALS list\n\t\t\t  | NAME EQUALS cadexpr : expr PLUS term\n\t\t\t| expr MINUS term\n\t\t\t| termterm : term TIMES factor\n\t\t\t| term DIVIDE factor\n\t\t\t| factorlist : LCORCHETE RCORCHETE\n\t\t\t| LCORCHETE element RCORCHETE\n\t\t\t| LCORCHETE element elements RCORCHETEelement : factor\n\t\t\t   | NAME\n\t\t\t   | listelements : COMMA element\n\t\t\t\t| COMMA list\n\t\t\t\t| COMMA element elementsfactor : NUMBER\n\t\t\t  | MINUS NUMBER\n\t\t\t  | NAMEcad : COMILLA NAME COMILLA\n\t\t   | COMILLAD NAME COMILLAD\n\t\t   | cad LCORCHETE index RCORCHETEindex : factor\n\t\t\t | factor DPOINT factor\n\t\t\t | factor DPOINT factor DPOINT factorwhile : WHILE LPAREN comparison RPAREN DPOINT sentencia\n\t\t\t | WHILE comparison DPOINT sentencia\n\t\t\t | WHILE LPAREN comparison comparisons RPAREN DPOINT sentencia\n\t\t\t | WHILE comparison comparisons DPOINT sentenciacomparisons : AND comparison\n\t\t\t\t   | AND comparison comparisons\n\t\t\t\t   | OR comparison\n\t\t\t\t   | OR comparison comparisonsbool : TRUE\n\t\t\t| FALSEcomparison : comp DEQUALS comp\n                  | comp DIFFERENT comp\n                  | comp HIGHER comp\n                  | comp LESS comp\n                  | comp HIGHEREQ  comp\n                  | comp LESSEQ comp\n                  | boolcomp : expr\n\t\t\t| elementfor : FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign\n\t\t   | FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign\n\t\t   | FOR NAME IN NAME DPOINT assignr_values : r_value COMMA r_value\n\t\t\t\t| r_value COMMA r_value COMMA r_valuer_value : factor\n\t\t\t   | LEN LPAREN NAME RPARENif : IF LPAREN comparison RPAREN DPOINT sentencia\n    \t  | IF LPAREN comparison comparisons RPAREN DPOINT sentencia\n    \t  | IF comparison DPOINT sentencia\n    \t  | IF comparison comparisons DPOINT sentencia\n          | IF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia\n          | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia\n          | IF comparison DPOINT sentencia ELSE DPOINT sentencia\n          | IF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia\n          | IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia\n          | IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia ELSE DPOINT sentencia\n\t\t  | IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia'
    
_lr_action_items = {'NAME':([0,2,3,4,5,7,8,9,10,11,12,13,14,16,24,29,30,31,33,34,35,36,37,38,39,40,42,44,45,46,47,48,49,50,51,52,53,54,55,56,57,61,63,70,71,80,81,82,83,84,86,89,90,93,94,95,96,97,99,102,105,108,109,110,111,112,117,118,120,121,122,125,128,130,131,134,135,136,137,139,140,142,144,145,149,152,153,154,156,158,159,161,164,166,168,170,174,176,177,178,180,182,183,],[6,6,6,6,6,15,27,27,-5,-6,-7,-8,33,27,-14,-27,27,27,-29,-9,-10,-11,64,65,-17,66,6,27,27,27,27,27,27,27,27,33,33,33,33,-28,-18,6,33,-37,6,-12,-13,-15,-16,-19,27,-64,6,-30,-31,6,33,6,-39,-20,6,27,-65,-32,33,-57,-36,6,-62,6,6,27,33,143,-38,-63,-68,6,6,33,6,6,6,27,-69,-55,33,-56,-66,6,27,6,-67,6,6,-72,6,6,-73,6,-70,6,-71,]),'FOR':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,70,71,80,81,82,83,84,89,90,93,94,97,99,102,105,109,110,112,117,118,120,121,122,131,134,135,136,137,144,149,152,154,156,158,161,164,166,168,170,174,176,177,178,180,182,183,],[7,7,7,7,7,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,7,-28,-18,7,-37,7,-12,-13,-15,-16,-19,-64,7,-30,-31,7,-39,-20,7,-65,-32,-57,-36,7,-62,7,7,-38,-63,-68,7,7,7,-69,-55,-56,-66,7,7,-67,7,7,-72,7,7,-73,7,-70,7,-71,]),'WHILE':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,70,71,80,81,82,83,84,89,90,93,94,97,99,102,105,109,110,112,117,118,120,121,122,131,134,135,136,137,144,149,152,154,156,158,161,164,166,168,170,174,176,177,178,180,182,183,],[8,8,8,8,8,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,8,-28,-18,8,-37,8,-12,-13,-15,-16,-19,-64,8,-30,-31,8,-39,-20,8,-65,-32,-57,-36,8,-62,8,8,-38,-63,-68,8,8,8,-69,-55,-56,-66,8,8,-67,8,8,-72,8,8,-73,8,-70,8,-71,]),'IF':([0,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,42,56,57,61,70,71,80,81,82,83,84,89,90,93,94,97,99,102,105,109,110,112,117,118,120,121,122,131,134,135,136,137,144,149,152,154,156,158,161,164,166,168,170,174,176,177,178,180,182,183,],[9,9,9,9,9,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,9,-28,-18,9,-37,9,-12,-13,-15,-16,-19,-64,9,-30,-31,9,-39,-20,9,-65,-32,-57,-36,9,-62,9,9,-38,-63,-68,9,9,9,-69,-55,-56,-66,9,9,-67,9,9,-72,9,9,-73,9,-70,9,-71,]),'$end':([1,2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,70,80,81,82,83,84,89,93,94,99,102,109,110,112,117,120,131,134,135,149,152,154,156,164,170,177,180,183,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-37,-12,-13,-15,-16,-19,-64,-30,-31,-39,-20,-65,-32,-57,-36,-62,-38,-63,-68,-69,-55,-56,-66,-67,-72,-73,-70,-71,]),'ELSE':([2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,70,80,81,82,83,84,89,93,94,99,102,109,110,112,117,120,131,134,135,148,149,152,154,156,164,167,170,172,177,179,180,183,],[-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-37,-12,-13,-15,-16,-19,107,-30,-31,-39,-20,124,-32,-57,-36,132,-38,146,-68,160,-69,-55,-56,-66,-67,171,-72,175,-73,181,-70,-71,]),'ELIF':([2,3,4,5,10,11,12,13,24,29,33,34,35,36,39,56,57,70,80,81,82,83,84,89,93,94,99,102,109,110,112,117,120,131,134,135,149,152,154,156,164,170,177,180,183,],[-1,-2,-3,-4,-5,-6,-7,-8,-14,-27,-29,-9,-10,-11,-17,-28,-18,-37,-12,-13,-15,-16,-19,108,-30,-31,-39,-20,125,-32,-57,-36,133,-38,147,-68,-69,-55,-56,-66,-67,-72,-73,-70,-71,]),'EQUALS':([6,],[14,]),'LPAREN':([8,9,67,116,133,147,],[16,31,96,130,145,159,]),'TRUE':([8,9,16,31,44,45,108,125,145,159,],[22,22,22,22,22,22,22,22,22,22,]),'FALSE':([8,9,16,31,44,45,108,125,145,159,],[23,23,23,23,23,23,23,23,23,23,]),'NUMBER':([8,9,14,16,25,30,31,44,45,46,47,48,49,50,51,52,53,54,55,63,86,96,108,111,125,128,139,145,153,159,],[29,29,29,29,56,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'MINUS':([8,9,14,16,20,24,26,27,29,30,31,33,34,39,44,45,46,47,48,49,50,51,52,53,54,55,56,63,80,81,82,83,86,96,108,111,125,128,139,145,153,159,],[25,25,25,25,53,-14,-17,-29,-27,25,25,-29,53,-17,25,25,25,25,25,25,25,25,25,25,25,25,-28,25,-12,-13,-15,-16,25,25,25,25,25,25,25,25,25,25,]),'LCORCHETE':([8,9,14,16,30,31,36,44,45,46,47,48,49,50,51,86,93,94,108,110,125,145,159,],[30,30,30,30,30,30,63,30,30,30,30,30,30,30,30,30,-30,-31,30,-32,30,30,30,]),'COMILLA':([14,64,],[37,93,]),'COMILLAD':([14,65,],[38,94,]),'IN':([15,],[40,]),'DPOINT':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,43,56,57,62,66,68,72,73,74,75,76,77,78,79,80,81,82,83,84,87,92,98,100,101,102,106,107,123,124,126,127,129,132,146,150,160,163,171,173,175,181,],[42,-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,61,-29,-17,71,-28,-18,90,95,97,-40,-42,-46,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,105,111,118,-41,-43,-20,121,122,136,137,139,140,142,144,158,161,166,168,174,176,178,182,]),'AND':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,41,56,57,60,72,73,74,75,76,77,78,79,80,81,82,83,84,102,138,165,],[44,-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,44,-29,-17,44,-28,-18,44,44,44,-46,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,-20,44,44,]),'OR':([17,19,20,21,22,23,24,26,27,28,29,32,33,39,41,56,57,60,72,73,74,75,76,77,78,79,80,81,82,83,84,102,138,165,],[45,-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,45,-29,-17,45,-28,-18,45,45,45,-46,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,-20,45,45,]),'DEQUALS':([18,20,21,24,26,27,28,29,33,39,56,57,80,81,82,83,84,102,],[46,-53,-54,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'DIFFERENT':([18,20,21,24,26,27,28,29,33,39,56,57,80,81,82,83,84,102,],[47,-53,-54,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'HIGHER':([18,20,21,24,26,27,28,29,33,39,56,57,80,81,82,83,84,102,],[48,-53,-54,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'LESS':([18,20,21,24,26,27,28,29,33,39,56,57,80,81,82,83,84,102,],[49,-53,-54,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'HIGHEREQ':([18,20,21,24,26,27,28,29,33,39,56,57,80,81,82,83,84,102,],[50,-53,-54,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'LESSEQ':([18,20,21,24,26,27,28,29,33,39,56,57,80,81,82,83,84,102,],[51,-53,-54,-14,-17,-22,-23,-27,-29,-17,-28,-18,-12,-13,-15,-16,-19,-20,]),'RPAREN':([19,20,21,22,23,24,26,27,28,29,33,39,41,56,57,60,69,72,73,74,75,76,77,78,79,80,81,82,83,84,88,100,101,102,113,114,115,141,143,155,157,162,169,],[-52,-53,-54,-44,-45,-14,-17,-22,-23,-27,-29,-17,68,-28,-18,87,98,-40,-42,-46,-47,-48,-49,-50,-51,-12,-13,-15,-16,-19,106,-41,-43,-20,127,129,-60,-58,155,-61,163,-59,173,]),'PLUS':([20,24,26,27,29,33,34,39,56,80,81,82,83,],[52,-14,-17,-29,-27,-29,52,-17,-28,-12,-13,-15,-16,]),'TIMES':([24,26,27,29,33,39,56,80,81,82,83,],[54,-17,-29,-27,-29,-17,-28,54,54,-15,-16,]),'DIVIDE':([24,26,27,29,33,39,56,80,81,82,83,],[55,-17,-29,-27,-29,-17,-28,55,55,-15,-16,]),'RCORCHETE':([27,28,29,30,33,56,57,58,59,84,85,91,92,102,103,104,119,126,151,],[-22,-23,-27,57,-29,-28,-18,84,-21,-19,102,110,-33,-20,-24,-23,-26,-34,-35,]),'COMMA':([27,28,29,33,56,57,58,59,84,102,103,104,113,115,141,155,],[-22,-23,-27,-29,-28,-18,86,-21,-19,-20,86,-23,128,-60,153,-61,]),'RANGE':([40,],[67,]),'LEN':([96,128,153,],[116,116,116,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'sentencia':([0,2,3,4,5,42,61,71,90,97,105,118,121,122,136,137,144,158,161,166,168,174,176,178,182,],[1,10,11,12,13,70,89,99,109,117,120,131,134,135,148,149,156,164,167,170,172,177,179,180,183,]),'assign':([0,2,3,4,5,42,61,71,90,95,97,105,118,121,122,136,137,140,142,144,158,161,166,168,174,176,178,182,],[2,2,2,2,2,2,2,2,2,112,2,2,2,2,2,2,2,152,154,2,2,2,2,2,2,2,2,2,]),'for':([0,2,3,4,5,42,61,71,90,97,105,118,121,122,136,137,144,158,161,166,168,174,176,178,182,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'while':([0,2,3,4,5,42,61,71,90,97,105,118,121,122,136,137,144,158,161,166,168,174,176,178,182,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'if':([0,2,3,4,5,42,61,71,90,97,105,118,121,122,136,137,144,158,161,166,168,174,176,178,182,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'comparison':([8,9,16,31,44,45,108,125,145,159,],[17,32,41,60,72,73,123,138,157,165,]),'comp':([8,9,16,31,44,45,46,47,48,49,50,51,108,125,145,159,],[18,18,18,18,18,18,74,75,76,77,78,79,18,18,18,18,]),'bool':([8,9,16,31,44,45,108,125,145,159,],[19,19,19,19,19,19,19,19,19,19,]),'expr':([8,9,14,16,31,44,45,46,47,48,49,50,51,108,125,145,159,],[20,20,34,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'element':([8,9,16,30,31,44,45,46,47,48,49,50,51,86,108,125,145,159,],[21,21,21,58,21,21,21,21,21,21,21,21,21,103,21,21,21,21,]),'term':([8,9,14,16,31,44,45,46,47,48,49,50,51,52,53,108,125,145,159,],[24,24,24,24,24,24,24,24,24,24,24,24,24,80,81,24,24,24,24,]),'factor':([8,9,14,16,30,31,44,45,46,47,48,49,50,51,52,53,54,55,63,86,96,108,111,125,128,139,145,153,159,],[26,26,39,26,59,26,26,26,26,26,26,26,26,26,39,39,82,83,92,59,115,26,126,26,115,151,26,115,26,]),'list':([8,9,14,16,30,31,44,45,46,47,48,49,50,51,86,108,125,145,159,],[28,28,35,28,28,28,28,28,28,28,28,28,28,28,104,28,28,28,28,]),'cad':([14,],[36,]),'comparisons':([17,32,41,60,72,73,138,165,],[43,62,69,88,100,101,150,169,]),'elements':([58,103,],[85,119,]),'index':([63,],[91,]),'r_value':([96,128,153,],[113,141,162,]),'r_values':([96,],[114,]),}

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
  ('element -> factor','element',1,'p_element','sintactico.py',81),
  ('element -> NAME','element',1,'p_element','sintactico.py',82),
  ('element -> list','element',1,'p_element','sintactico.py',83),
  ('elements -> COMMA element','elements',2,'p_elements','sintactico.py',87),
  ('elements -> COMMA list','elements',2,'p_elements','sintactico.py',88),
  ('elements -> COMMA element elements','elements',3,'p_elements','sintactico.py',89),
  ('factor -> NUMBER','factor',1,'p_factor','sintactico.py',96),
  ('factor -> MINUS NUMBER','factor',2,'p_factor','sintactico.py',97),
  ('factor -> NAME','factor',1,'p_factor','sintactico.py',98),
  ('cad -> COMILLA NAME COMILLA','cad',3,'p_cad','sintactico.py',105),
  ('cad -> COMILLAD NAME COMILLAD','cad',3,'p_cad','sintactico.py',106),
  ('cad -> cad LCORCHETE index RCORCHETE','cad',4,'p_cad','sintactico.py',107),
  ('index -> factor','index',1,'p_index','sintactico.py',116),
  ('index -> factor DPOINT factor','index',3,'p_index','sintactico.py',117),
  ('index -> factor DPOINT factor DPOINT factor','index',5,'p_index','sintactico.py',118),
  ('while -> WHILE LPAREN comparison RPAREN DPOINT sentencia','while',6,'p_while','sintactico.py',129),
  ('while -> WHILE comparison DPOINT sentencia','while',4,'p_while','sintactico.py',130),
  ('while -> WHILE LPAREN comparison comparisons RPAREN DPOINT sentencia','while',7,'p_while','sintactico.py',131),
  ('while -> WHILE comparison comparisons DPOINT sentencia','while',5,'p_while','sintactico.py',132),
  ('comparisons -> AND comparison','comparisons',2,'p_comparisons','sintactico.py',143),
  ('comparisons -> AND comparison comparisons','comparisons',3,'p_comparisons','sintactico.py',144),
  ('comparisons -> OR comparison','comparisons',2,'p_comparisons','sintactico.py',145),
  ('comparisons -> OR comparison comparisons','comparisons',3,'p_comparisons','sintactico.py',146),
  ('bool -> TRUE','bool',1,'p_bool','sintactico.py',153),
  ('bool -> FALSE','bool',1,'p_bool','sintactico.py',154),
  ('comparison -> comp DEQUALS comp','comparison',3,'p_comparison','sintactico.py',159),
  ('comparison -> comp DIFFERENT comp','comparison',3,'p_comparison','sintactico.py',160),
  ('comparison -> comp HIGHER comp','comparison',3,'p_comparison','sintactico.py',161),
  ('comparison -> comp LESS comp','comparison',3,'p_comparison','sintactico.py',162),
  ('comparison -> comp HIGHEREQ comp','comparison',3,'p_comparison','sintactico.py',163),
  ('comparison -> comp LESSEQ comp','comparison',3,'p_comparison','sintactico.py',164),
  ('comparison -> bool','comparison',1,'p_comparison','sintactico.py',165),
  ('comp -> expr','comp',1,'p_comp','sintactico.py',172),
  ('comp -> element','comp',1,'p_comp','sintactico.py',173),
  ('for -> FOR NAME IN RANGE LPAREN r_value RPAREN DPOINT assign','for',9,'p_for','sintactico.py',177),
  ('for -> FOR NAME IN RANGE LPAREN r_values RPAREN DPOINT assign','for',9,'p_for','sintactico.py',178),
  ('for -> FOR NAME IN NAME DPOINT assign','for',6,'p_for','sintactico.py',179),
  ('r_values -> r_value COMMA r_value','r_values',3,'p_r_values','sintactico.py',186),
  ('r_values -> r_value COMMA r_value COMMA r_value','r_values',5,'p_r_values','sintactico.py',187),
  ('r_value -> factor','r_value',1,'p_r_value','sintactico.py',194),
  ('r_value -> LEN LPAREN NAME RPAREN','r_value',4,'p_r_value','sintactico.py',195),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia','if',6,'p_if','sintactico.py',202),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia','if',7,'p_if','sintactico.py',203),
  ('if -> IF comparison DPOINT sentencia','if',4,'p_if','sintactico.py',204),
  ('if -> IF comparison comparisons DPOINT sentencia','if',5,'p_if','sintactico.py',205),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',9,'p_if','sintactico.py',206),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',10,'p_if','sintactico.py',207),
  ('if -> IF comparison DPOINT sentencia ELSE DPOINT sentencia','if',7,'p_if','sintactico.py',208),
  ('if -> IF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia','if',8,'p_if','sintactico.py',209),
  ('if -> IF LPAREN comparison RPAREN DPOINT sentencia ELIF LPAREN comparison RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',15,'p_if','sintactico.py',210),
  ('if -> IF LPAREN comparison comparisons RPAREN DPOINT sentencia ELIF LPAREN comparison comparisons RPAREN DPOINT sentencia ELSE DPOINT sentencia','if',17,'p_if','sintactico.py',211),
  ('if -> IF comparison DPOINT sentencia ELIF comparison DPOINT sentencia ELSE DPOINT sentencia','if',11,'p_if','sintactico.py',212),
  ('if -> IF comparison comparisons DPOINT sentencia ELIF comparison comparisons DPOINT sentencia ELSE DPOINT sentencia','if',13,'p_if','sintactico.py',213),
]
