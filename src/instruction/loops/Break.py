from src.abstract.Instruction import Instruction

class Break(Instruction):
    def __init__(self, line, column):
        super().__init__(line, column)

    def compile(self, environment):
        pass

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass