lexer grammar IOLexer;

// Types.
INT : 'int' ;
LONG : 'long' ;
DOUBLE : 'double' ;
CHAR : 'char' ;
STRING : 'string' ;

// Arithmetic operators.
PLUS : '+' ;
MINUS : '-' ;
MULT : '*' ;
DIV : '/' ;

// Parentheses.
LPAREN : '(' ;
RPAREN : ')' ;
LBRACK : '[' ;
RBRACK : ']' ;
LBRACE : '{' ;
RBRACE : '}' ;

// Separators.
COMMA : ',' ;
COLON: ':' ;
SEMICOL: ';' ;
NL : '\n' ;

// Section keywords.
REPEAT : 'repeat' ;
UPTO : 'upto' ;
INPUT : 'input' ;
OUTPUT : 'output' ;

// Ignored sequences.
WS : [ \t\r] -> skip ;
INLINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;

// String literals.
STR : '"' ~["]* '"' ;

// Number literal (positive).
NUM : ( '1'..'9' ( '0'..'9' )* ) ;

// Identifiers.
IDENT : [a-zA-Z][a-zA-Z0-9_]* ;
