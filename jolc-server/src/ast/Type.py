from enum import Enum

class Type(Enum):
    INT64 = 0
    FLOAT64 = 1
    BOOL = 2
    CHAR = 3
    STRING = 4 
    ERROR = 5
    NULO = 6
    # ARREGLO = 7 
    IDENTIFICADOR = 8  
    FUNCTION = 9
    RETURN = 10
    BREAK = 11 
    CONTINUE = 12
    NATIVE = 13
    STRUCT = 14
    MSTRUCT = 15 # Struct mutable
    RANGE = 16
    ARRAY = 17
    ANY = 18
    TEMP = 19
    VECTOR = 20

class TypeOperation(Enum):
    SUMA = 0
    RESTA = 1 
    MULTIPLICACION = 2 
    DIVISION = 3 
    MENOSUNARIO = 4
    AND = 5
    OR = 6 
    NOT = 7
    IGUAL = 8
    MAYORQ = 9
    MENORQ = 10
    MAYORIQ = 11
    MENORIQ = 12
    MODULO = 13
    DIFERENTE = 14
    POTENCIA = 15