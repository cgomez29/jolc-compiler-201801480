from src.ast.Environment import Environment
from src.abstract.Instruction import Instruction
from src.ast.Generator import Generator
from src.exception.Exception import Exception
from src.ast.Type import Type

class While(Instruction):
    def __init__(self, condition, instructions, line, column):
        super().__init__(line, column)
        self.condition = condition
        self.instructions = instructions

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        generator.addComment("BEGIN WHILE")
        
        continueLbl = generator.newLabel() # regresa a ka condición
        generator.putLabel(continueLbl)

        rCondition = self.condition.compile(environment)
        if(rCondition.getType() != Type.BOOL):
            generator.setException(Exception("Semántico", f"The condition is not of type BOOL", self.line, self.column))
            return
        
        newEnv = Environment(environment)

        newEnv.breakLbl = rCondition.falseLbl # break es la etiqueta false de mi condición para salirme.
        newEnv.continueLbl = continueLbl 

        generator.putLabel(rCondition.trueLbl)

        for i in self.instructions:
            i.compile(newEnv)
        
        generator.addGoto(continueLbl)

        generator.putLabel(rCondition.falseLbl)

        generator.addComment("END WHILE")

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass