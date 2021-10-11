from os import symlink
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
                self.isString(generator, symbol.getValue(), environment)
            elif(symbol.getType() == Type.INT64):
                generator.addPrint("d", symbol.getValue())
            elif(symbol.getType() == Type.ARRAY):
                temp = generator.addTemp()
                generator.getHeap(temp, symbol.getValue()) # recuperando el arreglo
                generator.addPrint("c", '91')
                for a in range(len(symbol.getAttributes())):
                    generator.getHeap(temp, a)
                    if(symbol.getAttributes()[a] == Type.INT64):
                        generator.addPrint("d", temp)
                    elif(symbol.getAttributes()[a] == Type.ARRAY):
                        self.isArray(a, symbol.getValues()[a])
                    if a != len(symbol.getAttributes()) -1:
                        generator.addPrint("c", '44')
                generator.addPrint("c", '93')
            else:
                generator.addPrint("f", symbol.getValue())

            if self.jump:
                generator.newLine()
    # pos: posicion del arreglo en el heap
    # attributes: types de los valores
    def isArray(self, pos, attributes):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.addComment("RECURSIVOOO")
        temp = generator.addTemp()
        generator.getHeap(temp, pos) # recuperando el arreglo
        generator.addPrint("c", '91')
        for a in range(len(attributes)):
            generator.getHeap(temp, temp)
            if(attributes[a] == Type.INT64):
                generator.addPrint("d", temp)
            elif(attributes[a] == Type.ARRAY):
                self.isArray(a, attributes[a])
            if a != len(attributes) -1:
                generator.addPrint("c", '44')
        generator.addPrint("c", '93')
        generator.addComment("RECURSIVOOO")

    def isString(self,generator, value, environment):
        generator.addComment('String print start')
        generator.fPrintString()
        paramTemp = generator.addTemp()

        generator.addExp(paramTemp, 'P', environment.getSize(), '+')
        generator.addExp(paramTemp, paramTemp, '1', '+')
        generator.setStack(paramTemp, value)
        
        generator.newEnv(environment.getSize())
        generator.callFun('printString')
        
        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        generator.addComment('String print end')

    def graph(self, g, father):
        pass

    def getNameSon(self):
        return "PRINT"