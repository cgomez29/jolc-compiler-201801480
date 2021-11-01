from optimization.instruction.Assignment import Assignment
from optimization.instruction.CallFun import CallFun
from optimization.instruction.Function import Function
from optimization.instruction.Label import Label
from optimization.instruction.Print import Print
from optimization.instruction.Return import Return

from optimization.goto.If import If
from optimization.goto.Goto import Goto

from optimization.expression.Access import Access
from optimization.expression.Expression import Expression
from optimization.expression.Literal import Literal

class Optimization:
    def __init__(self, packages, temps, code):
        self.packages = packages
        self.temps = temps
        self.code = code 

    def getCode(self):
        ret = f'package main;\n\nimport (\n\t"{self.packages}"\n);\n'
        for temp in self.temps:
            ret += f'var {temp}\n'
        ret +='\n'

        for func in self.code:
            ret += func.getCode() + '\n\n'

        return ret 


    def mirilla(self):
        # por cada función 
        for func in self.code:
            size = 20
            # Mientras no nos hemos pasado del size (Fin del codigo)
            while size <= len(func.instr):
                flagOpt = False 

                # 10 pasadas, con el size actual
                for i in range(10):
                    aux = 0
                    while (size + aux) <= len(func.instr):
                        flagOpt = flagOpt or self.regla3(func.instr[0+aux: size +aux])
                        flagOpt = flagOpt or self.regla6(func.instr[0+aux: size +aux])
                        aux += 1
                # si no hubo optimizacion en las pasadas, se aumenta el size
                if not flagOpt:
                    size += 20


    def regla3(self, array):
        ret = False 

        for i in range(len(array)):
            actual = array[i]
            # si la instruccion es un IF 
            if type(actual) is If and not actual.deleted:
                nextInst = array[i+1]
                # Si el siguiente es un GOTO
                if type(nextInst) is Goto and not nextInst.deleted:
                    # Se debe eliminar i+1 e i+2 Goto Lbl y Lbl:
                    actual.condition.getContrary()
                    actual.label = nextInst.label 
                    nextInst.deleted = True 
                    array[i+2].deleted = True 
                    ret = True

        return ret

    def regla6(self, array):
        ret = False  

        for i in range(len(array)):
            actual = array[i]
            # si la instruccion es una asignanción 
            if type(actual) is Assignment and not actual.deleted:
                # si esta asignado a si mismo
                if actual.selfAssignment():
                    actualOpt = actual.exp.neutralOps()
                    
                    if actualOpt:
                        ret = True 
                        actual.deleted = True
        return ret 
        