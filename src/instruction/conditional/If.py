from src.abstract.Instruction import Instruction
from src.ast.Generator import Generator
from src.ast.Type import Type
from src.exception.Exception import Exception

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

        generator.addComment("BEGIN IF")
           
        #IF
        # Valuando condición 
        
        rCondition = self.condition.compile(environment)

        
        if(rCondition.getType() != Type.BOOL):
            generator.setException(Exception("Semántico", f"The condition is not of type BOOL", self.line, self.column))
            return

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


        generator.addComment("END IF")


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass