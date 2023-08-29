parser grammar IOParser;

options { tokenVocab=IOLexer; }

filespec : ( REPEAT IDENT UPTO IDENT COLON )? inputfile outputfile ;

inputfile : INPUT COLON inputline ( NL+ inputline )* ;

outputfile: OUTPUT COLON ( headerline NL+ )? outputline ;

inputline
    : values
    | vectors
    | vector
    | matrix
    ;

headerline : ( STR | IDENT )+ SEMICOL ;

outputline
    : values
    | vector
    ;

values : ( homoValues SEMICOL )+ ;

homoValues : vartype IDENT ( COMMA IDENT )* ;

vectors : LBRACE values RBRACE LBRACK arithExpr RBRACK SEMICOL;

vector : vartype LBRACK arithExpr RBRACK IDENT SEMICOL ;

matrix : vartype LBRACK arithExpr RBRACK LBRACK arithExpr RBRACK IDENT SEMICOL ;

vartype : INT | LONG | DOUBLE | CHAR | STRING ;

arithExpr
    : addend
    | arithExpr ( PLUS | MINUS ) addend
    ;

addend
    : term
    | addend ( MULT | DIV | MOD ) term
    ;

term
    : IDENT
    | NUM
    | LPAREN arithExpr RPAREN
    ;
