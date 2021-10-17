from src.abstract.Instruction import Instruction
from src.instruction.native.Uppercase import Uppercase

class AST(Instruction):
    def __init__(self, instrucions, line, column):
        super().__init__(line, column)     
        self.instructions = instrucions

    def compile(self, environment):
        for i in self.instructions: 
            i.compile(environment)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass

