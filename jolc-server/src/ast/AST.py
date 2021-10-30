from src.abstract.Instruction import Instruction
from src.ast.Type import Type

class AST(Instruction):
    def __init__(self, instrucions, line, column):
        super().__init__(line, column)     
        self.instructions = instrucions
        self.globalEnv = None

    def compile(self, environment):
        for i in self.instructions: 
            i.compile(environment)
        self.globalEnv = environment

    def getSymbols(self):
        symbols = {}
        for key in self.globalEnv.getVariables():
            value = self.globalEnv.getVariables()[key]
            if value.getAuxType() != '':
                type = value.getAuxType()
            else:
                type = self.getType(value)
            data = f"\"column1\": \"{value.getId()}\", \"column2\": \"{type}\", \"column3\": \"{value.getEnviroment()}\", \"column4\": \"{value.getLine()}\", \"column5\": \"{value.getColumn()}\""
            
            data = "{" + data + "},"
            symbols[value.getId()] = data

        for key in self.globalEnv.getFunctions():
            value = self.globalEnv.getFunctions()[key]
            data = f"\"column1\": \"{value.getId()}\", \"column2\": \"{self.getType(value)}\", \"column3\": \"{value.getEnviroment()}\", \"column4\": \"{value.getLine()}\", \"column5\": \"{value.getColumn()}\""
            data = "{" + data + "},"
            symbols[value.getId()] = data

        return symbols


    def getType(self, value):
        if (value.getType() == Type.INT64):
            return "Int64"
        elif (value.getType() == Type.FLOAT64):
            return "Float64"
        elif (value.getType() == Type.STRING):
            return "String"
        elif (value.getType() == Type.BOOL):
            return "Bool"
        elif (value.getType() == Type.CHAR):
            return "Char"
        elif (value.getType() == Type.ARRAY):
            return "ARRAY"
        elif (value.getType() == Type.ANY):
            return "Any"
        elif (value.getType() == Type.FUNCTION):
            return "function"
        elif (value.getType() == Type.STRUCT):
            return "Struct"
        elif (value.getType() == Type.NULO):
            return "Nulo"

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass

