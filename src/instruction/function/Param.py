from src.abstract.Instruction import Instruction

class Param(Instruction):
    def __init__(self, id, type, line, column):
        super().__init__(line, column)  
        self.id = id 
        self.type = type 

    def compile(self, environment):
        pass
        
    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass