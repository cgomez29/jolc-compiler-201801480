
class SymbolFunction:
    def __init__(self, id, type, size, params, line, column):
        self.type = type 
        self.auxType = ''
        self.id = id 
        self.size = size 
        self.params = params 
        self.line = line 
        self.column = column
        self.enviroment = ''

    def getAuxType(self):
        return self.auxType

    def setAuxType(self, auxType):
        self.auxType = auxType

    def getType(self):
        return self.type 

    def getId(self):
        return self.id
            
    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column

    def setEnviroment(self, enviroment):
        self.enviroment = enviroment

    def getEnviroment(self):
        return self.enviroment