from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type
from src.abstract.Return import Return

class ArrayAccess(Instruction):
    def __init__(self, id, access, line, column):
        super().__init__(line, column)
        self.id = id 
        self.access = access

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        value = environment.getVariable(self.id)

        if value == None:
            generator.setException(Exception("Semántico", f"'{self.id}' is not define", self.line, self.column))
            return  

        auxAttributes = []
        auxValues = []
        
        finalType = None 
        tempItem = generator.addTemp() # guarda el valor encontrado
        size = len(self.access)


        for i in range(size):
            finalType = Type.INT64 # default int 
            if i == 0: # primera iteracion 
                lblTrue = generator.newLabel()
                lblFalse = generator.newLabel()
                lblExit = generator.newLabel()

                tempI = generator.addTemp() # valor de index a acceder
                tempIndex = generator.addTemp() # guardando el puntero al arreglo encontrado
                generator.addExp(tempI, self.access[i].value, '', '')
                index = self.access[i].value - 1 # obteniendo la posición que se desea acceder 
                if index <= size:
                    finalType = value.getAttributes()[index] # obteniendo typo del item buscado

                    auxAttributes = value.getValues()[index].getAttributes()
                    auxValues = value.getValues()[index].getValues()

                generator.getStack(tempItem, value.pos)
                generator.addExp(tempIndex, tempItem, '', '') # guardando el puntero al arreglo encontrado
                generator.getHeap(tempItem, tempItem)

                # comprobando que no exeda los limites
                generator.addIf(tempI, '1', '<', lblTrue) # limite inferior
                generator.addIf(tempI, tempItem, '>', lblTrue) #
                generator.addGoto(lblFalse)
                generator.putLabel(lblTrue)
                generator.printBoundsError()
                generator.addExp(tempItem, '0', '', '') # default result
                generator.addGoto(lblExit)
                generator.putLabel(lblFalse)# no exedio los limites
                
                generator.addExp(tempIndex, tempIndex, tempI, '+')
                generator.getHeap(tempItem, tempIndex)
                
                generator.putLabel(lblExit) # salida 
            else: # mas accesos 
                lblTrue = generator.newLabel()
                lblFalse = generator.newLabel()
                lblExit = generator.newLabel()

                tempI = generator.addTemp() # valor de index a acceder
                # tempItem = generator.addTemp() # guarda el valor encontrado
                tempIndex = generator.addTemp() # guardando el puntero al arreglo encontrado

                generator.addExp(tempI, self.access[i].value, '', '')
                index = self.access[i].value - 1 # obteniendo la posición que se desea acceder 
                if index <= size:
                    finalType = value.getAttributes()[index] # obteniendo typo del item buscado

                    auxAttributes = value.getValues()[index].getAttributes()
                    auxValues = value.getValues()[index].getValues()

                
                generator.getHeap(tempIndex, tempItem) # recuperando el tamaño del arreglo

                # comprobando que no exeda los limites
                generator.addIf(tempI, '1', '<', lblTrue) # limite inferior
                generator.addIf(tempI, tempIndex, '>', lblTrue) #
                generator.addGoto(lblFalse)
                generator.putLabel(lblTrue)
                generator.printBoundsError()
                generator.addExp(tempItem, '0', '', '') # default result
                generator.addGoto(lblExit)
                generator.putLabel(lblFalse)# no exedio los limites
                
                generator.addExp(tempIndex, tempItem, tempI, '+')
                generator.getHeap(tempItem, tempIndex)
                
                generator.putLabel(lblExit) # salida 
        
        ret = Return(tempItem, finalType, True)
        ret.setAttributes(auxAttributes)
        ret.setValues(auxValues)
        return ret 


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass