parser grammar IOParser;

options { tokenVocab=IOLexer; }

fileSpec : NL* ( REPEAT IDENT UPTO IDENT COLON NL )? NL* inputFile NL+ outputFile NL* EOF ;

inputFile : INPUT COLON NL+ inputLine ( NL+ inputLine )* ;

outputFile: OUTPUT COLON NL+ ( STR NL+ )? outputLine ( NL+ outputLine )*;

inputLine
    : values
    | vectors
    | vector
    | matrix
    ;

outputLine
    : values
    | vectors
    | vector
    | matrix
    ;

values : ( homoValues SEMICOL )+ ;

homoValues : varType IDENT ( COMMA IDENT )* ;

vectors : LBRACE values RBRACE LBRACK arithExpr RBRACK SEMICOL;

vector : varType IDENT LBRACK arithExpr RBRACK SEMICOL ;

matrix : varType IDENT LBRACK arithExpr RBRACK LBRACK arithExpr RBRACK SEMICOL ;

varType : INT | LONG | DOUBLE | CHAR | STRING ;

arithExpr
    : addend
    | arithExpr ( PLUS | MINUS ) addend
    ;

addend
    : term
    | addend ( MULT | DIV ) term
    ;

term
    : IDENT
    | NUM
    | LPAREN arithExpr RPAREN
    ;
