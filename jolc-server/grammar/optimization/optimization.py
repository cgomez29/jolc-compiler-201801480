from optimization.Optimization import Optimization 

# INSTRUCCIONES GENERALES
from optimization.instruction.Assignment import Assignment
from optimization.instruction.CallFun import CallFun
from optimization.instruction.Function import Function
from optimization.instruction.Label import Label
from optimization.instruction.Print import Print
from optimization.instruction.Return import Return

# INSTRUCCIONES DE CAMBIO DE FLUJO
from optimization.goto.If import If
from optimization.goto.Goto import Goto

# INSTRUCCIONES DE EXPRESION
from optimization.expression.Access import Access
from optimization.expression.Expression import Expression
from optimization.expression.Literal import Literal

# LEXICAL ANALYSIS
rw = {
    "FLOAT64": "FLOAT64",
    "INT": "INT",
    "FUNC": "FUNC",
    "RETURN": "RETURN",
    "IF": "IF",
    "GOTO" : "GOTO",
    "FMT": "FMT",
    "PRINTF": "PRINTF",
    "PACKAGE": "PACKAGE",
    "IMPORT": "IMPORT",
    "VAR": "VAR"
}

tokens = [
    "ID",
    "INTLITERAL",
    "FLOATLITERAL",
    "STRINGLITERAL",

    "TIMES",
    "DIV",
    "PLUS",
    "MINUS",


    "GREATER",
    "LESS",
    "GREATEREQUAL",
    "LESSEQUAL",
    "EQUALSEQUALS",
    "DISTINT",

    "EQUALS",
    "SEMICOLON",
    "COLON",
    "POINT",

    "LEKEY",
    "RIKEY",

    "LEPAR",
    "RIPAR",

    "LECOR",
    "RICOR",

    "COMMA"
] + list(rw.values())

t_TIMES                 = r'\*'
t_DIV                   = r'/'
t_PLUS                  = r'\+'
t_MINUS                 = r'-'

t_GREATER               = r'>'
t_LESS                  = r'<'
t_GREATEREQUAL          = r'>='
t_LESSEQUAL             = r'<='
t_EQUALSEQUALS          = r'=='
t_DISTINT               = r'!='

t_EQUALS                = r'='
t_SEMICOLON             = r';'
t_COLON                 = r':'
t_POINT                 = r'\.'

t_LEKEY                 = r'{'
t_RIKEY                 = r'}'

t_LEPAR                 = r'\('
t_RIPAR                 = r'\)'

t_LECOR                 = r'\['
t_RICOR                 = r'\]'

t_COMMA                 = r','

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = rw.get(t.value.upper(), 'ID')
    return t

def t_FLOATLITERAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("ERROR IN PARSE TO FLOAT")
        t.value = 0
    return t

def t_INTLITERAL(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("ERROR IN PARSE TO INT")
        t.value = 0
    return t

def t_STRINGLITERAL(t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

t_ignore = " \t"

def t_MLCOMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count("\n")

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lexer1 = lex.lex()

# SYNTACTIC ANALYSIS

def p_start(t):
    '''start :  PACKAGE ID SEMICOLON IMPORT LEPAR STRINGLITERAL RIPAR SEMICOLON declarations codeList'''
    t[0] = Optimizador(t[6], t[9], t[10])

def p_declarations(t):
    '''declarations : declarations declaration
                    | declaration'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_declaration(t):
    '''declaration :     VAR idList LECOR INTLITERAL RICOR FLOAT64 SEMICOLON
                    |   VAR idList type SEMICOLON'''
    if len(t) == 5:
        t[0] = f'{t[2]} {t[3]};'
    else:
        t[0] = f'{t[2]}[{t[4]}] float64;'

def p_type(t):
    '''type : INT
            | FLOAT64'''
    if t[1] == "int":
        t[0] = "int"
    else:
        t[0] = "float64"

def p_idList(t):
    '''idList :   idList COMMA ID
                | ID'''
    if len(t) == 2:
        t[0] = f'{t[1]}'
    else:
        t[0] = f'{t[1]}, {t[3]}'

def p_codeList(t):
    '''codeList : codeList code
                | code'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_code(t):
    'code : FUNC ID LEPAR RIPAR statement'
    t[0] = Function(t[5], t[2], t.lineno(1), t.lexpos(1))

def p_statement(t):
    '''statement : LEKEY instruction RIKEY'''
    t[0] = t[2]

def p_instruction(t):
    '''instruction : instruction instruction
                    | instruction'''
    if len(t) == 2:
        t[0] = [t[1]]
    else:
        t[1].append(t[2])
        t[0] = t[1]

def p_instruction(t):
    '''instruction :  assign SEMICOLON
                    | print SEMICOLON
                    | if
                    | gotoSt SEMICOLON
                    | label
                    | callFunc SEMICOLON
                    | retSt SEMICOLON'''
    t[0] = t[1]

def p_return(t):
    'retSt : RETURN'
    t[0] = Return(t.lineno(1), t.lexpos(1))

def p_callFunc(t):
    'callFunc : ID LEPAR RIPAR'
    t[0] = CallFun(t[1], t.lineno(2), t.lexpos(2))

def p_label(t):
    'label : ID COLON'
    t[0] = Label(t[1], t.lineno(2), t.lexpos(2))

def p_goto(t):
    'gotoSt : GOTO ID'
    t[0] = Goto(t[2], t.lineno(1), t.lexpos(1))

def p_if(t):
    'if : IF expression LEKEY GOTO ID SEMICOLON RIKEY'
    t[0] = If(t[2], t[5], t.lineno(1), t.lexpos(1))

def p_assign(t):
    'assign : access EQUALS finalExp'
    t[0] = Assignment(t[1], t[3], t.lineno(2), t.lexpos(2))

def p_assign2(t):
    '''assign :   ID EQUALS expression
                | ID EQUALS access'''
    aux = Literal(t[1], t.lineno(1), t.lexpos(1))
    t[0] = Assignment(aux, t[3], t.lineno(2), t.lexpos(2))

def p_print(t):
    'print : FMT POINT PRINTF LEPAR STRINGLITERAL COMMA printValue RIPAR'
    t[0] = Print(t[5], t[7], t.lineno(1), t.lexpos(1))

def p_printValue(t):
    '''printValue :   INT LEPAR finalExp RIPAR
                    | finalExp'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[3].haveInt = True
        t[0] = t[3]

def p_expression(t):
    '''expression :   finalExp PLUS finalExp
                    | finalExp MINUS finalExp
                    | finalExp TIMES finalExp
                    | finalExp DIV finalExp
                    | finalExp GREATER finalExp
                    | finalExp LESS finalExp
                    | finalExp GREATEREQUAL finalExp
                    | finalExp LESSEQUAL finalExp
                    | finalExp EQUALSEQUALS finalExp
                    | finalExp DISTINT finalExp
                    | finalExp'''
    if len(t) == 2:
        t[0] = t[1]
    else:
        t[0] = Expression(t[1], t[3], t[2], t.lineno(2), t.lexpos(2))

def p_finalExp(t):
    '''finalExp : ID
                | INTLITERAL
                | MINUS INTLITERAL
                | FLOATLITERAL'''
    if len(t) == 3:
        t[0] = Literal(0-t[2], t.lineno(1), t.lexpos(1))
    else:
        t[0] = Literal(t[1], t.lineno(1), t.lexpos(1))

def p_access(t):
    '''access :   ID LECOR INT LEPAR finalExp RIPAR RICOR
                | ID LECOR finalExp RICOR'''
    if len(t) == 5:
        t[0] = Access(t[1], t[3], t.lineno(2), t.lexpos(2))
    else:
        t[0] = Access(t[1], t[5], t.lineno(2), t.lexpos(2))
        t[0].haveInt = True

def p_error(t):
    print(t)
    print("Syntactic error in '%s'" % t.value)

import ply.yacc as yacc
parser2 = yacc.yacc()

def parse(input):
    return parser2.parse(input, lexer=lexer1)