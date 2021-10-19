from src.ast.Environment import Environment
from src.ast.Type import Type
from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.exception.Exception import Exception

class For(Instruction):
    def __init__(self, id, expression, instructions, line, column):
        super().__init__(line, column)
        self.id = id 
        self.expression = expression
        self.instructions = instructions

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        newEnv = Environment(environment)
    
        generator.addComment("BEGIN FOR")

        value = self.expression.compile(environment)
        
        temp = generator.addTemp()
        generator.freeTemp(temp)

        if value.getType() == Type.RANGE: 
            pass 
        elif value.getType() ==  Type.STRING:
            var = newEnv.setVariable(self.id, Type.CHAR, True)
            generator.addExp(temp, 'P', var.pos, '+')
            generator.setStack(temp, value.getValue())

            continueLbl = generator.newLabel() # regresa a ka condición
            breakLbl = generator.newLabel() # regresa a ka condición

            newEnv.continueLbl = continueLbl
            newEnv.breakLbl = breakLbl

            tempI = generator.addTemp()
            generator.addExp(temp, 'P', var.pos, '+')
            generator.getStack(tempI, temp)

            generator.putLabel(continueLbl)# inicio for
            tempH = generator.addTemp()
            generator.getHeap(tempH,tempI) # si es -1 termina la cadena 
            generator.setStack(temp, tempI) # guardando nuevo valor

            generator.addIf(tempH, '-1', '==', breakLbl)
            
            for x in self.instructions:
                x.compile(newEnv)
            
            generator.addExp(tempI, tempI, '1', '+')

            generator.addGoto(continueLbl)            
            generator.putLabel(breakLbl)

        elif value.getType() ==  Type.ARRAY:
            pass  
        else:
            generator.setException(Exception("Semántico", f"The expression must be RANGE||STRING||ARRAY", self.line, self.column))
            return
        generator.addComment("END FOR")

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass