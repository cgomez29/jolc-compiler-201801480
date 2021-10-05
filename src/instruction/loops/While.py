from src.abstract.Instruction import Instruction
from src.ast.Generator import Generator

class While(Instruction):
    def __init__(self, condition, instructions, line, column):
        super().__init__(line, column)
        self.condition = condition
        self.instructions = instructions

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        generator.addComment("start while")

        wlabel = generator.newLabel() #Label while
        generator.putLabel(wlabel)

        rCondition = self.condition.compile(environment)
        generator.putLabel(rCondition.trueLbl)

        for i in self.instructions:
            i.compile(environment)
        
        generator.addGoto(wlabel)

        generator.putLabel(rCondition.falseLbl)

        generator.addComment("fin while")

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass