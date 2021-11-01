from src.abstract.Instruction import Instruction

class Struct(Instruction):
    def __init__(self, id, attributes, line, column, mutable = False):
        super().__init__(line, column)
        self.id = id 
        self.attributes = attributes
        self.mutable = mutable  

    def compile(self, environment):
        environment.setStruct(self.id, self)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass