from src.abstract.Instruction import Instruction

class DataType(Instruction):
    def __init__(self, value, type, line, column):
        super().__init__(line, column)
        self.value = value 
        self.type = type

    def compile(self, environment):
        pass

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass