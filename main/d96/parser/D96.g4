grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classUse*  EOF;

classUse
    :  CLASS IDENT (SINGCOLON IDENT)?    bodyclass 
    ;
bodyclass
    :  LP (attribute|methodClass|constructor|destructor)* RP
    ;
constructor
    : CONSTRUCTOR LB listParams RB blockStatement
    ;
destructor
    : DESTRUCTOR LB listParams RB blockStatement
    ;
attribute
    : (val|var) SEMI
    ;
var
    : VAR DOLLAR (COMMA DOLLAR)* SINGCOLON (typeNumber|arrayType) (EQUAL calculators)?
    ;
val 
    : VAL IDENT (COMMA IDENT)* SINGCOLON (typeNumber|arrayType) (EQUAL calculators)?
    ;
 
calculators
    : calculator (COMMA calculator)*
    ;
calculator
    : number (math number)*
    ;
typeNumber
    : INT| FLOATTYPE | STRINGTYPE | BOOLEANTYPE | classType
    ;
classType
    : NEW IDENT LB RB
    ; 
math
    : integerType | booleanType | floatType | stringType 
    ;
arrayType
    : ARRAYTYPE  LBR typeNumber COMMA  Integer RBR        
    ;
methodClass
    : (IDENT|DOLLAR) LB listParams? RB   blockStatement 
    ;
listParams
    :  param (SEMI param)*  
    ;
param 
    : (typeNumber|arrayType) IDENT (COMMA IDENT)* 
    ;
blockStatement
    : LP (attribute| statement|returnself|ifElse|foreach )*  RP 
    ;
calculsingle
    : (IDENT|arrayIndex) EQUAL calculator
    ;
statement
    :(calculsingle|returnself|attributecall|BREAK|CONTINUE) SEMI
    ;
returnself
    : RETURN calculator
    ;
foreach 
    : FOREACH LB IDENT IN Integer DOTDOT Integer (BY Integer)? RB blockStatement
    ;
ifElse
    : if1 elseIf* else1?
    ;
if1  
    : IF LB expressions?  RB blockStatement
    ;
else1  
    : ELSE blockStatement
    ;
elseIf
    : ELSEIF LB expressions? RB blockStatement
    ; 
 
 
number
    : Float|Integer|String|Boolean|attributecall|IDENT
    ;
arrayIndex
    : ARRAYTYPE LBR (Integer|IDENT) RBR
    ;
booleanType
    :  NOT | DOUAND DOUOR | DOUEQUAL |  NOTEQUAL
    ;
integerType
    : ADD | SUB | MUL | DIV | MOD | DOUEQUAL | NOTEQUAL | GREATER | GREQUAL | LESS | LESEQUAL
    ;
floatType 
    : ADD | SUB | MUL | DIV | GREATER | GREQUAL | LESS | LESEQUAL
    ;
stringType
    : ADDDOT | DOUEQUALDOT
    ;
arithmeticOperators
    :  ADD | SUB | MUL | DIV | MOD
    ;
booleanOperators
    : NOT | DOUAND | DOUOR | DOUEQUALDOT
    ;
stringOperators    
    : ADDDOT
    ;
relationalOperators
    : (DOUAND | NOTEQUAL | GREATER | GREQUAL | LESS | LESEQUAL)
    ;
operators
    : (relationalOperators | stringOperators | booleanOperators | arithmeticOperators)
    ;
expressions
    : number (operators number)*
    ;
attributecall
    :  instanceAttribute|staticAttribute
    ;
instanceAttribute 
    : IDENT DOT IDENT ( LB ((number|IDENT) (COMMA (number|IDENT))* )? RB)?
    ;
staticAttribute
    : IDENT COLON DOLLAR  ( LB ((number|IDENT) (COMMA (number|IDENT))* )? RB)?
    ;
array 
    : ARRAYTYPE LB (.)*? RB
    ;
Float
    : (DecimalConstant FRACTION EXPONENT
    | FRACTION EXPONENT
    | DecimalConstant EXPONENT
    | DecimalConstant FRACTION )  
    {
      self.text = self.text.replace('_' ,'')
    } 
    ;
fragment
DOUBQUOTE: '"';
String
    : DOUBQUOTE (LEGAL_THIEN)*  DOUBQUOTE  {  
      self.text = self.text[1:]
      self.text = self.text[:-1]
    }
    ; 
fragment
LEGAL_THIEN
    : ('\\'[bfrnt\\'] | '\'"'| ~[\\"])
    ;   
Boolean
    :  'True'|'False'
    ; 
Integer 
    :   (DecimalConstant 
    |   OctalConstant 
    |   HexadecimalConstant 
    |	  BinaryConstant) {  self.text = self.text.replace('_','') }
    ; 
  
Poinfloat
 : DecimalConstant FRACTION 
 ;
 
Exponentfloat
 : ( DecimalConstant | Poinfloat ) EXPONENT
 ;

fragment
FRACTION
 : DOT Digit*
 ;

fragment
EXPONENT
 : [eE] [+-]? Digit+
 ;

 
BinaryConstant
	  :	'0' [bB] '1' [01]*
	  ;
HexadecimalConstant
    :    '0' [xX] [1-9A-F] [0-9A-F_]*
    ;
 
OctalConstant
    :   '0'  [1-7] [0-7_]*
    ;
 
fragment
DecimalConstant
    :   (([1-9] [0-9_]*) |'0')  
    ;
fragment
NonzeroDigit
    :   [1-9]
    ;
fragment 
Digit
    :   [0-9]
    ;


 



BREAK:       'Break' ;
CONTINUE:    'Continue' ;
IF:          'If' ;
ELSEIF:      'Elseif' ;
ELSE:        'Else' ;
FOREACH:     'Foreach' ;
 
ARRAYTYPE:       'Array' ;
INT:         'Int' ;
IN:          'In' ;
 
FLOATTYPE:       'Float' ;
BOOLEANTYPE:     'Boolean' ;
STRINGTYPE:      'String' ;
RETURN:      'Return' ;
NULL:        'NULL' ;
CLASS:       'Class' ;
VAL:         'Val' ;
VAR:         'Var' ;
CONSTRUCTOR: 'Constructor' ;
DESTRUCTOR:  'Destructor' ;
NEW:         'New' ;
BY:          'By' ;


GREQUAL:  '>=';
LESEQUAL:   '<='; 
DOUEQUALDOT:   '==.'; 
ADDDOT:   '+.'; 
ADD:   '+';
SUB:   '-';
MUL:   '*';
DIV:   '/';
MOD:  '%'; 
NOTEQUAL:   '!=';
NOT:   '!';
DOUAND:   '&&';
DOUOR:   '||';
DOUEQUAL:   '==';
EQUAL:   '='; 
 
GREATER:   '>';
 
LESS:  '<';
 
 
 
COLON:   '::'; 
SINGCOLON: ':';
DOTDOT: '..';
DOT:   '.';

LB: '(' ; 
RB: ')';

LP:   '{';
RP:  '}';

 
SEMI: ';';
COMMA: ',';

LBR: '[';
RBR: ']';
IDENT :[a-zA-Z_] [a-zA-Z0-9_]*;
DOLLAR: '$' [a-zA-Z0-9_]+ ;
COMMENT: '##' .*? '##' -> skip;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines;

ERROR_CHAR: . {raise ErrorToken(self.text)};  

fragment
ILL_THIEN : '\\'  ~[bfrnt'\\] ;
 
ILLEGAL_ESCAPE: DOUBQUOTE (LEGAL_THIEN)* ILL_THIEN  {raise IllegalEscape(self.text[1:])};

UNCLOSE_STRING:   DOUBQUOTE (LEGAL_THIEN)*  {raise UncloseString(self.text[1:])};
  
 