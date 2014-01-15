grammar CC2;

options {
   language = Python;
// debug = false;
   output = AST;
   ASTLabelType = CommonTree;
//   backtrack = true;
//   memoize = true;
}

tokens {
   VARDEF;
   CONSTDEF;
   CONDITION;
   ITERATE;
   CALL;
   INDEX;
   FIELDACCESS;
   SLIST;

}

/*
@members {
constants = {}
functions = {}
threads = {}
}
*/
module
/*
scope {
        symbols
}
@init {
        $module::symbols = {}
}
*/
        :       (type_definition | variable_declaration | const_expr | thread_definition| function_definition)*
        ;


type_definition
        :        TYPE ID LCURLY declaration+ RCURLY
        ;

declaration
        :       any_type ID SEMI
        ;

array_spec
        :       LBRACK constant_expression RBRACK
        ;

qname
        : ID
        | ID DOT ID
        ;

constant_expression
        :       INT_CONST
        ;


variable_declaration
        :       any_type ID (array_spec)? (COMMA ID (array_spec)?)* SEMI
        ;


const_expr
        :       CONST ID (LBRACK RBRACK)? ASSIGN primary_expression (COMMA scalar_value)* SEMI
        ;


thread_definition
        :       THREAD ID LCURLY thread_body RCURLY
        ;

thread_body
        :       /* (assignment | primary_expression)* */
        variable_declaration*
        statement*
        ;


function_definition
        :       FUNCTION ID function_header function_body
        ;

function_header
        :       LPAREN parameter_list? RPAREN returns_clause?
        ;

parameter_list
        :       any_type ID     (COMMA any_type ID)*
        ;

function_body
        :       LCURLY RCURLY
        ;

returns_clause
        :       RETURNS
        ;

statement
        :       assignment
        |       primary_expression
        |       invocation
        ;

invocation
        :       function_call
        |       builtin_invocation
        ;


function_call
        :       qname '(' primary_expression (COMMA primary_expression)* ')' SEMI -> qname primary_expression*

        ;


builtin_invocation
        :       'wait' primary_expression SEMI
        ;

assignment
        :       ID ASSIGN primary_expression SEMI
        ;

expr
        :       primary_expression
        |       invocation
        ;


primary_expression
        :       or_expression
        ;

or_expression
        : and_expression ((OR | NOR | XOR)^ and_expression)*
        ;

and_expression
        : comp_expression ((AND | NAND)^ comp_expression)*
        ;

comp_expression
        : shift_expression (('==' | '!=' | '>' | '<' | '>=' | '<=')^    shift_expression)*
        ;

shift_expression
        : additive_expression ((SHL | SHR)^ additive_expression)*
        ;

additive_expression
        : multiplicative_expression (('+'| '-')^ multiplicative_expression)*
        ;

multiplicative_expression
        : unaryExpr (('*' | '/' | MOD)^ unaryExpr)*
        ;

unaryExpr:          unary_operator? atom;
        //;

atom
        : scalar_value
        | LPAREN! primary_expression RPAREN!

        ;


unary_operator:      '+' | '-' | NOT
        ;


numerical_type
        :       BYTE
        |       INT
        |       LONG
        |       FLOAT
        ;

builtin_type
        :       numerical_type
        |       STRING
        ;

any_type
        :       builtin_type
        |       ID
        ;

scalar_value
        :       CHAR
        |       INT_CONST
        |       FLOAT_CONST
        |       STRING_CONST
        ;


// ----------------------------------------------------------------------------
//                               KEYWORDS
// ----------------------------------------------------------------------------
AND             : 'and'
                | '&'
                ;
BREAK           : 'break'
                ;
BYTE            :'byte'
                ;
CAPTURE         :'capture'
                ;
CONST           :'const'
                ;
CONTINUE        :'continue'
                ;
DO              :'do'
                ;
ELSE            :'else'
                ;
FLOAT           :'float'
                ;
FOR             :'for'
                ;
FUNCTION        :'function'
                ;
HALT            :'halt'
                ;
IF              :'if'
                ;
INLINE          :'inline'
                ;
INT             :'int'
                ;
LONG            :'long'
                ;
LOOP            :'loop'
                ;
MOD             :'mod'
                | '%'
                ;
NAND            :'nand'
                | '!&'
                ;
NOR             :'nor'
                | '!|'
                ;
NOT             :'not'
                | '!'
                ;
OR              :'or'
                | '|'
                ;
QUIT            :'quit'
                ;
RELEASE         :'release'
                ;
RESET           :'reset'
                ;
RESUME          :'resume'
                ;
RETURN          :'return'
                ;
RETURNS         :'returns'
                ;
RUN             :'run'
                ;
SHL             :'shl'
                | '<<'
                ;
SHR             :'shr'
                | '>>'
                ;
SLEEP           :'sleep'
                ;
STEP            :'step'
                ;
STRING          :'string'
                ;
THREAD          :'thread'
                ;
TYPE            :'type'
                ;
WAIT            :'wait'
                ;
WHILE           :'while'
                ;
XOR             :'xor'
                | '^'
                ;
YIELD           :'yield'
                ;

ASSIGN          : '='
                ;
LPAREN          : '('
                ;
RPAREN          : ')'
                ;
LCURLY          : '{'
                ;
RCURLY          : '}'
                ;
LBRACK          : '['
                ;
RBRACK          : ']'
                ;
COMMA           : ','
                ;
SEMI            : ';'
                ;
range           : '...'
                ;
DOT             : '.'
                ;

ID              : ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*
                ;

INT_CONST       : '0'..'9'+
                ;

/*
DEC_INT
HEX_INT
OCT_INT
BIN_INT
*/


FLOAT_CONST     : ('0'..'9')+ '.' ('0'..'9')* EXPONENT?
                |   '.' ('0'..'9')+ EXPONENT?
                |   ('0'..'9')+ EXPONENT
                ;

COMMENT         : '//' ~('\n'|'\r')* '\r'? '\n' {$channel=HIDDEN;}
                | '/*' ( options {greedy=false;} : . )* '*/' {$channel=HIDDEN;}
                ;

WS              : ( ' '
                |   '\t'
                |   '\r'
                |   '\n') {$channel=HIDDEN;}
                ;

STRING_CONST    : '"' ( ESC_SEQ | ~('\\'|'"') )* '"'
                ;

CHAR            : '\'' ( ESC_SEQ | ~('\''|'\\') ) '\''
                ;

fragment
EXPONENT        : ('e'|'E') ('+'|'-')? ('0'..'9')+
                ;

fragment
HEX_DIGIT       : ('0'..'9'|'a'..'f'|'A'..'F')
                ;

fragment
ESC_SEQ         : '\\' ('b'|'t'|'n'|'f'|'r'|'\"'|'\''|'\\')
                | UNICODE_ESC
                | OCTAL_ESC
                ;

fragment
OCTAL_ESC       : '\\' ('0'..'3') ('0'..'7') ('0'..'7')
                | '\\' ('0'..'7') ('0'..'7')
                | '\\' ('0'..'7')
                ;

fragment
UNICODE_ESC     : '\\' 'u' HEX_DIGIT HEX_DIGIT HEX_DIGIT HEX_DIGIT
                ;

