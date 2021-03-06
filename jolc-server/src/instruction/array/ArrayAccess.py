from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type
from src.abstract.Return import Return
from src.exception.Exception import Exception

class ArrayAccess(Instruction):
    def __init__(self, id, access, line, column):
        super().__init__(line, column)
        self.id = id 
        self.access = access

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.addComment("BEGIN ACCESS ARRAY")

        value = environment.getVariable(self.id)

        if value == None:
            generator.setException(Exception("Semántico", f"'{self.id}' is not define", self.line, self.column))
            return  

        auxAttributes = []
        auxValues = []
        
        finalType = Type.INT64 # default int 
        
        tempItem = generator.addTemp() # guarda el valor encontrado
        tempI = generator.addTemp() # guardando el puntero 
        tempIndex = generator.addTemp() # guardando el puntero al arreglo encontrado

        size = len(self.access)

        ty = value.getType()
        
        # while ty.value != None:
        #     finalType = ty.value
        #     if type(finalType) is not TypeArray: break  
        #     ty = ty.value 

        for i in range(size):
            if i == 0: # primera iteracion 
                finalType = ty.value 

                lblTrue = generator.newLabel()
                lblFalse = generator.newLabel()
                lblExit = generator.newLabel()

                val = self.access[i].compile(environment) # compilando valor
                generator.addExp(tempI, val.getValue(), '', '') # guardando posición a acceder

                # si no es global se toma en cuenta P
                tempPos = value.pos
                if(not value.isGlobal):
                    tempPos = generator.addTemp()
                    generator.freeTemp(tempPos)
                    generator.addExp(tempPos, 'P', value.pos, "+")
                generator.getStack(tempIndex, tempPos) # recuperando el arreglo
                
                generator.getHeap(tempItem, tempIndex) # recuperando tamaño

                # comprobando que no exeda los limites
                generator.addIf(tempI, '1', '<', lblTrue) # limite inferior
                generator.addIf(tempI, tempItem, '>', lblTrue) # limite superior
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
                finalType = finalType.value

                lblTrue = generator.newLabel()
                lblFalse = generator.newLabel()
                lblExit = generator.newLabel()

                val = self.access[i].compile(environment) # compilando valor
                generator.addExp(tempI, val.getValue(), '', '') # recuperando index

                generator.addExp(tempIndex, tempItem, '', '') # guardando posición anterior
                generator.getHeap(tempItem, tempItem) # recuperando el tamaño del arreglo

                # comprobando que no exeda los limites
                generator.addIf(tempI, '1', '<', lblTrue) # limite inferior
                generator.addIf(tempI, tempItem, '>', lblTrue) #
                generator.addGoto(lblFalse)
                generator.putLabel(lblTrue)
                generator.printBoundsError()
                generator.addExp(tempItem, '0', '', '') # default result
                generator.addGoto(lblExit)
                generator.putLabel(lblFalse)# no exedio los limites
                
                generator.addComment("**************************************")
                generator.addExp(tempIndex, tempIndex, tempI, '+')
                generator.getHeap(tempItem, tempIndex)
                generator.addComment("**************************************")
                
                generator.putLabel(lblExit) # salida 

        generator.addComment("END ACCESS ARRAY")
        ret = Return(tempItem, finalType, True)
        ret.setAttributes(auxAttributes)
        ret.setValues(auxValues)
        return ret 

    def getId(self):
        return self.id

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass