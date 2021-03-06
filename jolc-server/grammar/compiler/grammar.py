import ply.yacc as yacc
from src.ast.AST import AST 
from src.ast.Type import Type, TypeOperation

from src.instruction.Print import Print
from src.instruction.variables.Declaration import Declaration
from src.instruction.conditional.If import If
from src.instruction.loops.While import While
from src.instruction.loops.For import For 
from src.instruction.loops.Range import Range
from src.instruction.loops.Break import Break
from src.instruction.loops.Continue import Continue
from src.instruction.loops.Return import Return
from src.instruction.function.Function import Function
from src.instruction.struct.Struct import Struct
from src.instruction.array.Array import Array
from src.instruction.array.ArrayAccess import ArrayAccess
from src.instruction.array.TypeArray import TypeArray
from src.instruction.function.Call import Call
from src.expression.Unary import Unary
from src.expression.Identifier import Identifier 
from src.expression.ExpCall import ExpCall
from src.expression.ArithmeticOperation import ArithmeticOperation
from src.expression.RelationalOperation import RelationalOperation
from src.expression.LogicalOperation import LogicalOperation
from src.instruction.struct.StructGet import StructGet
from src.expression.Literal import Literal 

reservadas = {
    'println' : 'PRINTLN',
    'print' : 'PRINT',
    'function' : 'FUNCION',
    'end' : 'FIN',
    'true' : 'TRUE',
    'false' : 'FALSE',
    'if' : 'if',
    'for' : 'for',
    'in' : 'in',
    'else' : 'else',
    'elseif' : 'elseif',
    'while' : 'while',
    'return' : 'return',
    'break' : 'break',
    'continue' : 'continue',
    'local' : 'local',
    'global' : 'global',
    'nothing' : 'NULO',
    'Int64' : 'INT64',
    'Float64' : 'FLOAT64',
    'Bool' : 'BOOL',
    'Char' : 'CHAR',
    'String' : 'STRING',
    'struct' : 'STRUCT',
    'mutable' : 'MUTABLE',
    'Vector' : 'VECTOR',
}

tokens  = [
    'SEMICOLON',
    'COLON',
    'TIPOVAR',
    'CORIZQ',
    'CORDER',
    'PARIZQ',
    'PARDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'POTENCIA',
    'MODULO',
    'COMMA',
    'DOT',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CHARACTER',
    'ID',
    'IGUALIGUAL',
    'IGUAL',
    'MAYORQ',
    'MENORQ',
    'MAYORIQ',
    'MENORIQ',
    'DIFERENTE',
    'AND',
    'OR',
    'NOT',
 ] + list(reservadas.values())

# Tokens
t_CORIZQ    = r'\['
t_CORDER    = r'\]'
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_LLAVEIZQ    = r'\{'
t_LLAVEDER    = r'\}'
t_COMMA  = r'\,'
t_DOT  = r'\.'
t_SEMICOLON    = r'\;'
t_COLON    = r'\:'
t_TIPOVAR    = r'\:\:'
t_IGUAL   = r'\='

t_MAS       = r'\+'
t_MENOS     = r'\-'
t_POR       = r'\*'
t_DIVIDIDO  = r'\/'
t_POTENCIA = r'\^'
t_MODULO  = r'\%'

# Relational operation
t_MAYORQ     = r'\>'
t_MENORQ     = r'\<'
t_IGUALIGUAL = r'\=\='
t_MAYORIQ    = r'\>\='
t_MENORIQ    = r'\<\='
t_DIFERENTE    = r'\!\='

# Logical operation
t_AND    = r'\&\&'
t_OR    = r'\|\|'
t_NOT    = r'\!'

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'_*[a-zA-Z_][a-zA-Z_0-9]*_*'
    t.type = reservadas.get(t.value,'ID')    # Check for reserved words
    return t

def t_CHARACTER(t): 
    r"""\' (\\'| \\\\ | \\n | \\t | \\r | \\" | .)? \'"""
    t.value = t.value[1:-1]#removiendo comillas 
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t 

def t_CADENA(t):
    r'\"(.|[a-zA-Z????????????????????????\s]+)*?\"'
    t.value = t.value[1:-1] #removiendo comillas
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace("\\'", '\'')
    return t    

# Comentario multi linea #= ... =#
def t_COMENTARIOML(t):
    r'\#\=(.|\n)*\=\#'
    t.lexer.lineno += t.value.count("\n")

# Comentario simple # ...
def t_COMENTARIO(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def find_column(token):
    global input
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador l??xico
import ply.lex as lex
lexer = lex.lex()


# Asociaci??n de operadores y precedencia
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('left','IGUALIGUAL','DIFERENTE'),
    ('left','MAYORIQ','MENORIQ', 'MAYORQ', 'MENORQ'),
    ('left','MAS','MENOS'),
    ('left','POR','DIVIDIDO', 'MODULO'),
    ('right','POTENCIA'),
    ('right','NOT'),
    ('right','UMENOS'),
    ('left','DOT'),
)


# Definici??n de la gram??tica

#=======================================================================================
# INICIO 
#=======================================================================================

def p_init(t):
    'init   : scripts'
    t[0] = AST(t[1],0,0)
    #t[0].execute()

def p_init_empty(t):
    'init            : empty'
    t[0] = t[1]

def p_empty(t) :
    'empty :'
    t[0] = []

#=======================================================================================
# SCRIPTS
#=======================================================================================

def p_scripts_list(t): 
    'scripts : scripts script '
    t[1].append(t[2])
    t[0] = t[1]

def p_scripts_script(t):
    'scripts : script'
    t[0] = [t[1]]

def p_script_evaluar(t):
    '''script   :   function SEMICOLON
                |   instruccion
    '''
    t[0] = t[1]

#=======================================================================================
# FUNCTIONS
#=======================================================================================

def p_script_function(t): 
    '''function : FUNCION ID PARIZQ PARDER instrucciones FIN
                | FUNCION ID PARIZQ PARDER TIPOVAR TIPO instrucciones FIN
                | FUNCION ID PARIZQ PARAMETROSTIPO PARDER instrucciones FIN
                | FUNCION ID PARIZQ PARAMETROSTIPO PARDER TIPOVAR TIPO instrucciones FIN
    '''
    if(len(t) == 7):
        t[0] = Function(t[2], [], Type.ANY, t[5], t.lineno(1), find_column(t.slice[1]))
    elif(len(t) == 9):
        t[0] = Function(t[2], [], t[6], t[7], t.lineno(1), find_column(t.slice[1]))
    elif(len(t) == 8):
        t[0] = Function(t[2], t[4], Type.ANY, t[6], t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = Function(t[2], t[4], t[7], t[8], t.lineno(1), find_column(t.slice[1]))

#=======================================================================================

def p_parametro_list(t):
    '''PARAMETROS : PARAMETROS COMMA PARAMETRO '''
    t[1].append(t[3])
    t[0] = t[1]

def p_parametro_item(t):
    '''PARAMETROS : PARAMETRO'''
    t[0] = [t[1]]

def p_parametro_valor(t):
    '''PARAMETRO    :   expresion'''
    t[0] = t[1]

#=======================================================================================

def p_parametrotipo_list(t):
    '''PARAMETROSTIPO : PARAMETROSTIPO COMMA PARAMETROTIPO '''
    t[1].append(t[3])
    t[0] = t[1]

def p_parametrotipo_item(t):
    '''PARAMETROSTIPO : PARAMETROTIPO'''
    t[0] = [t[1]]

def p_parametrotipo_valor(t):
    '''PARAMETROTIPO    :   ID TIPOVAR TIPO
                        |   ID TIPOVAR ID
                        |   ID'''
    if(len(t) == 2):
        t[0] = {"id":t[1],"tipo": Type.ANY}
    else: 
        t[0] = {"id": t[1], "tipo": t[3]}
        

#=======================================================================================
# INSTRUCCIONES
#=======================================================================================
def p_instrucciones_lista(t):
    '''instrucciones    :  instrucciones instruccion '''
    t[1].append(t[2])
    t[0] = t[1]

def p_instrucciones_instruccion(t):
    '''instrucciones    :  instruccion '''
    t[0]  = [t[1]]

def p_instruccion_evaluar(t):
    '''instruccion  : imprimir SEMICOLON
                    | call SEMICOLON
                    | STRUCTS SEMICOLON
                    | IF SEMICOLON
                    | FOR SEMICOLON
                    | WHILE SEMICOLON
                    | BREAK SEMICOLON
                    | CONTINUE SEMICOLON
                    | RETURN SEMICOLON
                    | DECLARACION SEMICOLON'''
    t[0] = t[1]

#=======================================================================================
# STRUCT
#=======================================================================================

def p_instruccion_struct(t):
    '''STRUCTS   :   MUTABLE STRUCT ID ATIBUTOSSTRUCT FIN
                |   MUTABLE STRUCT ID FIN
                |   STRUCT ID ATIBUTOSSTRUCT FIN
                |   STRUCT ID FIN
                '''
    if(len(t) == 6):
        t[0] = Struct(t[3], t[4], t.lineno(1), find_column(t.slice[1]), True)
    elif(len(t) == 5):
        if(t[1] == "mutable"):
           t[0] = Struct(t[3], [], t.lineno(1), find_column(t.slice[1]), True)
        else: 
           t[0] = Struct(t[2], t[3], t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = Struct(t[2], [], t.lineno(1), find_column(t.slice[1]))

def p_struct_atributos(t):
    '''ATIBUTOSSTRUCT   :   ATIBUTOSSTRUCT ATRIBUTOSTRUCT SEMICOLON'''
    t[1].append(t[2])
    t[0] = t[1]

def p_struct_actributo(t):
    '''ATIBUTOSSTRUCT   :   ATRIBUTOSTRUCT SEMICOLON'''
    t[0] = [t[1]]

def p_atributo_item(t):
    '''ATRIBUTOSTRUCT   :   ID TIPOVAR TIPO 
                        |   ID TIPOVAR ID
                        |   ID '''
    if(len(t)==2):
        t[0] = {"id":t[1],"tipo": Type.ANY}
    else:
        t[0] = {"id":t[1],"tipo": t[3]}

def p_struct_gets(t):
    '''STRUCTGETS   : STRUCTGETS DOT STRUCTGET'''
    t[1].append(t[3])
    t[0] = t[1]

def p_struct_get(t):
    '''STRUCTGETS   : STRUCTGET'''
    t[0] = [t[1]]

def p_get_item(t):
    '''STRUCTGET    :   ID'''
    t[0] = t[1] 

#=======================================================================================
# ARRAY
#=======================================================================================
def p_intruccion_array(t):
    '''ARREGLO : CORIZQ PARAMETROS CORDER'''
    t[0] = Array(t[2], t.lineno(1), find_column(t.slice[1]))

def p_array_list(t):
    '''ARRAYGETS   :  ARRAYGETS ARRAYGET'''
    t[1].append(t[2])
    t[0] = t[1]
#=======================================================================================

def p_array_item(t):
    '''ARRAYGETS   :    ARRAYGET'''
    t[0] = [t[1]]

def p_array_value(t):
    '''ARRAYGET    :  CORIZQ expresion CORDER'''
    t[0] = t[2] 

#=======================================================================================
def p_array_type(t):
    '''ARRAYTYPE    : VECTOR LLAVEIZQ TIPO LLAVEDER'''
    t[0] = TypeArray( t[3], Type.ARRAY, t.lineno(1), find_column(t.slice[1]))

#=======================================================================================
# IF
#=======================================================================================

def p_instruccion_if(t):
    ''' IF  : if expresion instrucciones FIN
            | if expresion instrucciones else instrucciones FIN
            | if expresion instrucciones LIST_ELSEIF
    '''

    if(t[4] == "end"):
        t[0] = If(t[2], t[3], None, None, t.lineno(1), find_column(t.slice[1]))
    elif(t[4] == "else"):
        t[0] = If(t[2], t[3], t[5], None, t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = If(t[2], t[3], None, t[4], t.lineno(1), find_column(t.slice[1]))

def p_instruccion_list_elseif(t):
    '''LIST_ELSEIF : LIST_ELSEIF ELSEIF'''
    t[1].append(t[2])
    t[0] = t[1]

def p_instruccion_elseif_item(t):
    '''LIST_ELSEIF : ELSEIF'''
    t[0]  = [t[1]]

def p_instruccion_elseif(t):
    ''' ELSEIF  : elseif expresion instrucciones FIN 
                | elseif expresion instrucciones else instrucciones FIN 
                | elseif expresion instrucciones LIST_ELSEIF
    ''' 
    if(t[4] == "end"):
        t[0] = If(t[2], t[3], None, None, t.lineno(1), find_column(t.slice[1]))
    elif(t[4] == "else"):
        t[0] = If(t[2], t[3], t[5], None, t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = If(t[2], t[3], None, t[4], t.lineno(1), find_column(t.slice[1]))

#=======================================================================================
# FOR
#=======================================================================================

def p_instruccion_for(t):
    '''FOR  :   for ID in expresion instrucciones FIN
            |   for ID in expresion FIN'''
    if(len(t) == 7):
        t[0] = For(t[2], t[4], t[5], t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = For(t[2], t[4], [],t.lineno(1), find_column(t.slice[1]))

def p_instruccion_rango(t):
    '''RANGO    :   expresion COLON expresion'''
    t[0] = Range(t[1], t[3], t.lineno(1), find_column(t.slice[2]))


#=======================================================================================
# WHILE
#=======================================================================================

def p_instruccion_while(t):
    '''WHILE : while expresion instrucciones FIN'''
    t[0] =  While(t[2], t[3], t.lineno(1), find_column(t.slice[1]))

def p_instruccion_return(t):
    '''RETURN : return expresion'''
    t[0] = Return(t[2], t.lineno(1), find_column(t.slice[1]))

def p_instruccion_break(t):
    '''BREAK : break'''
    t[0] = Break(t.lineno(1), find_column(t.slice[1]))

def p_instruccion_continue(t):
    '''CONTINUE : continue'''
    t[0] = Continue(t.lineno(1), find_column(t.slice[1]))

#=======================================================================================
# DECLARATION
#=======================================================================================
def p_instruccion_declaration(t):
    ''' DECLARACION     :   local ID
                        |   global ID
                        |   ID IGUAL expresion
                        |   global ID IGUAL expresion 
                        |   local ID IGUAL expresion 
                        |   ID IGUAL expresion TIPOVAR TIPO
                        |   global ID IGUAL expresion TIPOVAR TIPO
                        |   local ID IGUAL expresion TIPOVAR TIPO
                        |   STRUCTGETS IGUAL expresion
                        |   ID ARRAYGETS IGUAL expresion
    '''
    if(len(t) == 4): # ID IGUAL expresion
        t[0] =  Declaration(None, t[1], t[3], t.lineno(1), find_column(t.slice[2]))
    elif(len(t) == 5): # [global/local] ID IGUAL expresion 
        if(str(t[1]) == "local" or str(t[1]) == "global"):
            t[0] =  Declaration(t[1], t[2], t[4], t.lineno(1), find_column(t.slice[1]))
        else:
            # ID ARRAYGETS IGUAL expresion
            value = [t[1], t[2]] # [id, arreglo de accesos]
            t[0] =  Declaration(None, value, t[4], t.lineno(1), find_column(t.slice[3]))
    elif(len(t) == 6): # ID IGUAL expresion TIPOVAR TIPO
        x = {"value": t[3], "tipo": t[5]}
        t[0] =  Declaration(None, t[1], x, t.lineno(1), find_column(t.slice[1]), False)
    elif(len(t) == 3):
        t[0] =  Declaration(t[1], t[2], None, t.lineno(2), find_column(t.slice[2]), False)
    else: # [global/local] ID IGUAL expresion TIPOVAR TIPO
        x = {"value": t[4], "tipo": t[6]}
        t[0] =  Declaration(t[1], t[2], x, t.lineno(3), find_column(t.slice[1]), False)

#=======================================================================================
# PRINT
#=======================================================================================

def p_instrucion_imprimir(t):
    '''imprimir : PRINTLN PARIZQ PARAMETROS PARDER
                | PRINT PARIZQ PARAMETROS PARDER
                | PRINT PARIZQ PARDER
                | PRINTLN PARIZQ PARDER
    '''
    if len(t) == 5:
        if t[1] == "print":
            t[0] = Print(t[3], t.lineno(1), find_column(t.slice[1]))
        else:
            t[0] = Print(t[3], t.lineno(1), find_column(t.slice[1]), True)
    else: 
        if t[1] == "print":
            t[0] = Print([], t.lineno(1), find_column(t.slice[1]))
        else:
            t[0] = Print([], t.lineno(1), find_column(t.slice[1]), True)


#=======================================================================================
# EXPRESIONES
#=======================================================================================

def p_expresion_aritmetica(t):
    '''expresion : expresion MAS expresion
                  | expresion MENOS expresion
                  | expresion POR expresion
                  | expresion DIVIDIDO expresion
                  | expresion POTENCIA expresion
                  | expresion MODULO expresion
                  | expresion DOT expresion'''
    if t[2] == '+'  : t[0] = ArithmeticOperation(t[1],t[3], TypeOperation.SUMA, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '-': t[0] = ArithmeticOperation(t[1],t[3], TypeOperation.RESTA, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '*': t[0] = ArithmeticOperation(t[1],t[3], TypeOperation.MULTIPLICACION, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '/': t[0] = ArithmeticOperation(t[1],t[3], TypeOperation.DIVISION, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '%': t[0] = ArithmeticOperation(t[1],t[3], TypeOperation.MODULO, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '^': t[0] = ArithmeticOperation(t[1],t[3], TypeOperation.POTENCIA, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '.': t[0] = StructGet(t[1],t[3], t.lineno(2), find_column(t.slice[2]))

def p_expresion_relacional(t):
    '''expresion : expresion IGUALIGUAL expresion
                | expresion MAYORQ expresion
                | expresion MENORQ expresion
                | expresion MAYORIQ expresion
                | expresion MENORIQ expresion
                | expresion DIFERENTE expresion'''
    if t[2] == '=='  : t[0] = RelationalOperation(t[1],t[3], TypeOperation.IGUAL, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '>': t[0] = RelationalOperation(t[1],t[3], TypeOperation.MAYORQ, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '<': t[0] = RelationalOperation(t[1],t[3], TypeOperation.MENORQ, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '>=': t[0] = RelationalOperation(t[1],t[3], TypeOperation.MAYORIQ, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '<=': t[0] = RelationalOperation(t[1],t[3], TypeOperation.MENORIQ, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '!=': t[0] = RelationalOperation(t[1],t[3], TypeOperation.DIFERENTE, t.lineno(2), find_column(t.slice[2]))

def p_expresiones_logicas(t):
    '''expresion : expresion AND expresion
                | expresion OR expresion'''
    if t[2] == '&&'  : t[0] = LogicalOperation(t[1],t[3], TypeOperation.AND, t.lineno(2), find_column(t.slice[2]))
    elif t[2] == '||'  : t[0] = LogicalOperation(t[1],t[3], TypeOperation.OR, t.lineno(2), find_column(t.slice[2]))

def p_expresiones_logicasNOT(t):
    '''expresion : NOT expresion '''
    if t[1] == '!'  : t[0] = LogicalOperation(t[2],None, TypeOperation.NOT, t.lineno(1), find_column(t.slice[1]))

def p_expresion_agrupacion(t):
    'expresion : PARIZQ expresion PARDER'
    t[0] = t[2]

def p_expresion_unaria(t):
    'expresion : MENOS expresion %prec UMENOS'
    t[0] = Unary(t[2], t.lineno(1), find_column(t.slice[1]))

#=======================================================================================
# CALL
#=======================================================================================

def p_instruccion_call(t):
    '''call : ID PARIZQ PARDER
            | ID NOT PARIZQ PARDER
            | ID PARIZQ PARAMETROS PARDER  
            | ID NOT PARIZQ PARAMETROS PARDER  
            '''
    if(len(t) == 4):
        t[0] = Call(t[1], [], t.lineno(1), find_column(t.slice[1]))
    elif(len(t) == 5):
        if(t[2] == '!'):
            id = str(t[1]) + str(t[2])
            t[0] = Call(id, [], t.lineno(1), find_column(t.slice[1]))
        else:
            t[0] = Call(t[1], t[3], t.lineno(1), find_column(t.slice[1]))
    else: 
        id = str(t[1]) + str(t[2])
        t[0] = Call(id, t[4], t.lineno(1), find_column(t.slice[1]))

#=======================================================================================

def p_expresion_call(t):
    '''excall : ID PARIZQ PARDER
            | ID NOT PARIZQ PARDER
            | ID PARIZQ PARAMETROS PARDER  
            | ID NOT PARIZQ PARAMETROS PARDER  
            '''
    if(len(t) == 4):
        t[0] = ExpCall(t[1], [], t.lineno(1), find_column(t.slice[1]))
    elif(len(t) == 5):
        if(t[2] == '!'):
            id = str(t[1]) + str(t[2])
            t[0] = ExpCall(id, [], t.lineno(1), find_column(t.slice[1]))
        else:
            t[0] = ExpCall(t[1], t[3], t.lineno(1), find_column(t.slice[1]))
    else: 
        id = str(t[1]) + str(t[2])
        t[0] = ExpCall(id, t[4], t.lineno(1), find_column(t.slice[1]))

def p_expresion_calls(t):
    'expresion : excall'
    t[0] = t[1]

#=======================================================================================
# LITERALS
#=======================================================================================

def p_expresion_number(t):
    '''expresion    : ENTERO'''
    t[0] = Literal(t[1], Type.INT64, t.lineno(1), find_column(t.slice[1]))

def p_expresion_number_float(t):
    '''expresion    : DECIMAL'''
    t[0] = Literal(t[1], Type.FLOAT64, t.lineno(1), find_column(t.slice[1]))

def p_expresion_string(t):
    '''expresion    :  CADENA'''
    t[0] = Literal(t[1], Type.STRING, t.lineno(1), find_column(t.slice[1]))

def p_expresion_char(t):
    '''expresion    :  CHARACTER'''
    t[0] = Literal(t[1], Type.CHAR, t.lineno(1), find_column(t.slice[1]))

def p_expresion_id(t):
    '''expresion    :  ID'''
    t[0] = Identifier(t[1], Type.IDENTIFICADOR, t.lineno(1), find_column(t.slice[1]))

def p_expresion_boolean(t):
    '''expresion    : TRUE 
                    | FALSE
                    | NULO'''
    if(str(t[1]) == "true"):
        t[0] = Literal(True, Type.BOOL, t.lineno(1), find_column(t.slice[1]))
    elif(str(t[1]) == "false"): 
        t[0] = Literal(False, Type.BOOL, t.lineno(1), find_column(t.slice[1]))
    else:
        t[0] = Literal(None, Type.NULO, t.lineno(1), find_column(t.slice[1]))

#=======================================================================================

def p_expresion_arrayget(t):
    'expresion : ID ARRAYGETS'
    t[0] = ArrayAccess(t[1], t[2], t.lineno(1), find_column(t.slice[1]))

def p_expresion_array(t):
    'expresion : ARREGLO'
    t[0] = t[1]

def p_expresion_rango(t):
    'expresion : RANGO'
    t[0] = t[1]

def p_expresion_tipo(t):
    'expresion : TIPO'
    t[0] = t[1]

def p_tipo(t):
    '''TIPO :   INT64
            |   FLOAT64
            |   BOOL 
            |   CHAR
            |   ID
            |   STRING
            |   ARRAYTYPE
    '''
    if(t[1] == "Int64"):
        t[0] = Type.INT64
    elif(t[1] == "Float64"):
        t[0] = Type.FLOAT64
    elif(t[1] == "Bool"):
        t[0] = Type.BOOL
    elif(t[1] == "Char"):
        t[0] = Type.CHAR
    elif(t[1] == "String"):
        t[0] = Type.STRING
    elif(type(t[1]) == TypeArray):
        t[0] = t[1]
    else:
        t[0] = t[1]


#=======================================================================================
# ERRORES
#=======================================================================================
def p_error(t):
    print("Error sint??ctico en '%s'" % t.value)

parser = yacc.yacc()

input = ""

def parse(code):
    global input
    global lexer
    global parser
    input = code
    lexer = lex.lex()
    parser = yacc.yacc()
    return parser.parse(code)