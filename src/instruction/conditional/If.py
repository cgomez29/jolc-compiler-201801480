from src.abstract.Instruction import Instruction
from src.ast.Generator import Generator

class If(Instruction):
    def __init__(self, condition, instructions, instrElse, instrElseIf, line, column):
        super().__init__(line, column)
        self.condition = condition
        self.instructions = instructions
        self.instrElse = instrElse 
        self.instrElseIf = instrElseIf

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        generator.addComment("Start if")
           
        #IF
        # Valuando condición 
        rCondition = self.condition.compile(environment)
        generator.putLabel(rCondition.trueLbl)

        for i in self.instructions:
            i.compile(environment)

        if self.instrElseIf != None:
            exitLabel = generator.newLabel()
            generator.addGoto(exitLabel)
            generator.putLabel(rCondition.falseLbl)

            for i in self.instrElseIf:
                i.compile(environment)
            generator.putLabel(exitLabel)                
        elif self.instrElse != None: # else
            exitLabel = generator.newLabel()
            generator.addGoto(exitLabel)
            generator.putLabel(rCondition.falseLbl)

            for i in self.instrElse:
                i.compile(environment)
            generator.putLabel(exitLabel)
        elif(self.instrElseIf == None and self.instrElse == None):
            generator.putLabel(rCondition.falseLbl)


        generator.addComment("Fin if")


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass