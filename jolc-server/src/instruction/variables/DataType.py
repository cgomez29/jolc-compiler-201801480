from src.abstract.Return import Return
from src.abstract.Expression import Expression

class DataType(Expression):
    def __init__(self, value, type, line, column):
        super().__init__(line, column)
        self.value = value 
        self.type = type
    
    def compile(self, environment):
        return Return("", self.type, False)
        

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass