from src.ast.Type import Type

class TypeTable:
    def __init__(self):
        # Tabla de colisiones de Types
        self.types = [
                [Type.INT64,    Type.FLOAT64, Type.INT64,   Type.CHAR,  Type.ERROR], 
                [Type.FLOAT64,  Type.FLOAT64, Type.ERROR,   Type.ERROR, Type.ERROR], 
                [Type.INT64,    Type.FLOAT64, Type.BOOL,    Type.ERROR, Type.ERROR], 
                [Type.CHAR,     Type.ERROR,   Type.CHAR,    Type.CHAR,  Type.ERROR], 
                [Type.ERROR,    Type.ERROR,   Type.ERROR,   Type.ERROR, Type.ERROR], 
            ] 
    # @param left Operando izquierdo 
    # @param rigth Operandor derecho
    # @returns retorna el Type que tendra la operacion final
    def getType(self, left, rigth):
        return self.types[left.value][rigth.value]