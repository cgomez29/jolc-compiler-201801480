from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type
from src.exception.Exception import Exception

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
            elif(symbol.getType() == Type.CHAR):
                temp = generator.addTemp()
                generator.getHeap(temp, symbol.getValue())
                generator.addPrint("c", temp)
            elif(symbol.getType() == Type.ARRAY):

                temp = generator.addTemp()
                temp2 = generator.addTemp()
                
                generator.addExp(temp2, symbol.getValue(), '1', '+') # guardando posición del arreglo
                # generator.getHeap(temp, symbol.getValue()) # recuperando el arreglo
                generator.addPrint("c", '91')
                for a in range(len(symbol.getAttributes())):
                    generator.getHeap(temp, temp2) # recuperando item 

                    if(symbol.getAttributes()[a] == Type.INT64):
                        generator.addPrint("d", temp)
                    elif(symbol.getAttributes()[a] == Type.STRING):
                        generator.addPrint("c", '34')
                        self.isString(generator, temp, environment)
                        generator.addPrint("c", '34')
                    elif(symbol.getAttributes()[a] == Type.ARRAY):
                        self.isArray(temp, symbol.getValues()[a], environment)

                    if a != len(symbol.getAttributes()) -1:
                        generator.addPrint("c", '44')
                    generator.addExp(temp2, temp2, 1, '+') # cambiando de posición 
                
                generator.addPrint("c", '93')
            else:
                generator.addPrint("f", symbol.getValue())

        if self.jump:
            generator.newLine()

    # pos: posicion del arreglo en el heap
    # attributes: types de los valores
    def isArray(self, tempH, attribute, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        
        temp = generator.addTemp()
        temp2 = generator.addTemp()
        
        generator.addExp(temp2, tempH, '1', '+')
        # generator.getHeap(temp, tempH) # recuperando el arreglo
        generator.addPrint("c", '91')
        for a in range(len(attribute.getAttributes())):
            generator.getHeap(temp, temp2) # recuperando item 
            
            if(attribute.getAttributes()[a] == Type.INT64):
                generator.addPrint("d", temp)
            elif(attribute.getAttributes()[a] == Type.STRING):
                generator.addPrint("c", '34')
                self.isString(generator, temp, environment)
                generator.addPrint("c", '34')
            elif(attribute.getAttributes()[a] == Type.ARRAY):
                self.isArray(temp, attribute.getValues()[a], environment)
            
            if a != len(attribute.getAttributes()) -1:
                generator.addPrint("c", '44')
            generator.addExp(temp2, temp2, 1, '+') # cambiando de posición 
                
        generator.addPrint("c", '93')

    def isString(self,generator, value, environment):
        generator.addComment('BEGIN PRINT STRING')
        generator.fPrintString()
        paramTemp = generator.addTemp()

        generator.addExp(paramTemp, 'P', environment.getSize(), '+')
        generator.addExp(paramTemp, paramTemp, '1', '+')
        generator.setStack(paramTemp, value)
        
        generator.newEnv(environment.getSize())
        generator.callFun('native_print_string')
        
        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        generator.addComment('END PRINT STRING')

    def graph(self, g, father):
        pass

    def getNameSon(self):
        return "PRINT"