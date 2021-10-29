
class SymbolFunction:
    def __init__(self, id, type, size, params, line, column):
        self.type = type 
        self.id = id 
        self.size = size 
        self.params = params 
        self.line = line 
        self.column = column


    def getType(self):
        return self.type 
