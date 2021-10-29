from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction

class Break(Instruction):
    def __init__(self, line, column):
        super().__init__(line, column)

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.addGoto(environment.breakLbl)


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass