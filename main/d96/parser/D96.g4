grammar D96;

@lexer::header {
from lexererr import *
}

options {
	language = Python3;
}

program: classUse  EOF;
 
classUse
    :  CLASS IDENT (SINGCOLON IDENT)*    mainClass 
    ;
mainClass
    :  LP (attribute|declaration|constructor|destructor)* RP
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
declaration
    : IDENT LB listParams? RB   blockStatement 
    ;
listParams
    :  param (COMMA param)*
    ;
param 
    : number
    ;
blockStatement
    : LP (attribute| statement )*  RP 
    ;

statement
    :((IDENT|arrayIndex) EQUAL calculator SEMI)
    ;
foreach 
    : FOREACH LB IDENT IN Integer DOTDOT Integer (BY Integer)? blockStatement
    ;
ifElse
    :
    ;
if1  
    : IF LB expressions  RB blockStatement
    ;
else1  
    : ELSE blockStatement
    ;
elseIf
    : ELSEIF LB expressions RB blockStatement
    ; 
call 
    :
    ;
invocation
    :
    ;
number
    : Float|Integer|String|Boolean
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
    : DOUAND | NOTEQUAL | GREATER | GREQUAL | LESS | LESEQUAL
    ;
operators
    : relationalOperators | stringOperators | booleanOperators | arithmeticOperators
    ;
expressions
    : number operators number
    ;
instanceAttribute 
    : IDENT DOT IDENT
    ;
staticAttribute
    : IDENT COLON IDENT
    ;
Array 
    : ARRAYTYPE LB (.)*? RB
    ;
Float
    :   Poinfloat
    |   Exponentfloat
    ; 
 
String
    : DOUBQUOTE ((~["#])+)? DOUBQUOTE  {  self.text = self.text.replace('"','') }
    ;
 
     
Boolean
    :   TRUE|FALSE
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
 
FRACTION
 : DOT Digit+
 ;

 
EXPONENT
 : [eE] [+-]? Digit+
 ;

 
BinaryConstant
	  :	'0' [bB] [0-1]+
	  ;
HexadecimalConstant
    :   HexadecimalPrefix HexadecimalDigit+
    ;
HexadecimalPrefix
    :   '0' [xX]
    ;
HexadecimalDigit
    :   [0-9a-fA-F]
    ;
OctalConstant
    :   '0' OctalDigit*
    ;
OctalDigit
    :   [0-7]
    ;
DecimalConstant
    :   (([1-9] [0-9_]*) |'0')  
    ;
NonzeroDigit
    :   [1-9]
    ;
 
Digit
    :   [0-9]
    ;


DOLLAR: '$' IDENT ;
   

BREAK:       'Break' ;
CONTINUE:    'Continue' ;
IF:          'If' ;
ELSEIF:      'Elseif' ;
ELSE:        'Else' ;
FOREACH:     'Foreach' ;
TRUE:        'True' ;
FALSE:       'False' ;
ARRAYTYPE:       'Array' ;
IN:          'In' ;
INT:         'Int' ;
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
 

ADD:   '+';
SUB:   '-';
MUL:   '*';
DIV:   '/';
MOD:  '%'; 
NOT:   '!';
DOUAND:   '&&';
DOUOR:   '||';
DOUEQUAL:   '==';
EQUAL:   '='; 
NOTEQUAL:   '!=';
GREATER:   '>';
GREQUAL:  '>=';
LESS:  '<';
LESEQUAL:   '<='; 
DOUEQUALDOT:   '==.';
ADDDOT:   '+.'; 
COLON:   '::'; 
SINGCOLON: ':';
DOTDOT: '..';
DOT:   '.';

LB: '(' ; 
RB: ')';

LP:   '{';
RP:  '}';
DOUBQUOTE: '"';
SEMI: ';';
COMMA: ',';

LBR: '[';
RBR: ']';
IDENT :[a-zA-Z] [a-zA-Z0-9_]*;
COMMENT: '##' .*? '##' -> skip;
WS: [ \t\r\n]+ -> skip; // skip spaces, tabs, newlines;

ERROR_CHAR: . {raise ErrorToken(self.text)};  
UNCLOSE_STRING:   DOUBQUOTE ((~["#])+)?  {raise UncloseString(self.text.replace('"',''))};
 
 
ILLEGAL_ESCAPE: '"'(  [bfrnt"\\] | ~[\r\n\\])* '"'  {raise IllegalEscape(self.text)};
 
  