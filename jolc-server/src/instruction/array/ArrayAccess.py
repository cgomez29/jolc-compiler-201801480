from src.expression.Identifier import Identifier
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


        posAnterior = 0
        for i in range(size):
            finalType = Type.INT64 # default int 
            if i == 0: # primera iteracion 
                lblTrue = generator.newLabel()
                lblFalse = generator.newLabel()
                lblExit = generator.newLabel()

                tempI = generator.addTemp() # valor de index a acceder
                tempIndex = generator.addTemp() # guardando el puntero al arreglo encontrado
                if type(self.access[i]) is Identifier:
                    # FIXME: Repara no se puede acceder cuando el arr[i] es un identificador
                    val = environment.getVariable(self.access[i].id)
                    generator.addExp(tempI, self.access[i].value, '', '')
                else: 
                    generator.addExp(tempI, self.access[i].value, '', '')
                    index = self.access[i].value - 1 # obteniendo la posición que se desea acceder 
                posAnterior = index
                if index <= size:
                    finalType = value.getAttributes()[index] # obteniendo typo del item buscado

                    auxAttributes = value.getValues()[index].getAttributes()
                    auxValues = value.getValues()[index]

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
                    # auxAttributes = value.getValues()[posAnterior].getAttributes()
                    # finalType = auxAttributes[index] # obteniendo type del item buscado
                    # posAnterior = index
                    # auxValues = value.getValues()[index].getValues()
                    
                    auxAttributes = auxValues.getAttributes()
                    finalType = auxAttributes[index] # obteniendo type del item buscado
                    auxValues = auxValues.getValues()[index]

                
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