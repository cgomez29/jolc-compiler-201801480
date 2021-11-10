from src.abstract.Instruction import Instruction
from src.ast.Type import Type

class Struct(Instruction):
    def __init__(self, id, attributes, line, column, mutable = False):
        super().__init__(line, column)
        self.id = id 
        self.attributes = attributes
        self.mutable = mutable  

    def compile(self, environment):
        if self.mutable:
            environment.setStruct(self.id, self, Type.MSTRUCT)
        else:
            environment.setStruct(self.id, self, Type.STRUCT)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass