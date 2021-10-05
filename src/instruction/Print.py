from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type

class Print(Instruction):
    def __init__(self, expression, line, column, jump=False):
        super().__init__(line, column)
        self.expression = expression
        self.jump = jump
        self.trueLbl = ''
        self.falseLbl = ''

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        for x in self.expression:
            symbol = x.compile(environment) # as Return
            
            if(symbol.getType() == Type.BOOL):
                tempLbl = generator.newLabel()

                generator.putLabel(symbol.trueLbl) 
                generator.printTrue()
                generator.addGoto(tempLbl)

                generator.putLabel(symbol.falseLbl) 
                generator.printFalse()
                generator.putLabel(tempLbl)
            
            elif(symbol.getType() == Type.STRING):
                generator.addComment('String print start')
                generator.fPrintString()
                paramTemp = generator.addTemp()

                generator.addExp(paramTemp, 'P', environment.getSize(), '+')
                generator.addExp(paramTemp, paramTemp, '1', '+')
                generator.setStack(paramTemp, symbol.getValue())

                generator.newEnv(environment.getSize())
                generator.callFun('printString')

                temp = generator.addTemp()
                generator.getStack(temp, 'P')
                generator.retEnv(environment.getSize())
                generator.addComment('String print end')
            elif(symbol.getType() == Type.INT64):
                generator.addPrint("d", symbol.getValue())
            else:
                generator.addPrint("f", symbol.getValue())

            if self.jump:
                generator.newLine()


    def graph(self, g, father):
        pass

    def getNameSon(self):
        return "PRINT"