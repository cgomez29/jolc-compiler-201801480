from src.exception.Exception import Exception
from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type

class Declaration(Instruction):
    def __init__(self, scope, id, value, line, column, type= True):
        super().__init__(line, column)
        self.scope = scope
        self.id = id 
        self.value = value 
        self.type = type #la asignacion tiene tipo declarado

    def compile(self, environment):
        auxGen = Generator()
        generator = auxGen.getInstance()

        if isinstance(self.id, str):# es solo un id

            isAssign = environment.getVariable(self.id)

            if (isinstance(self.value, str)):
                val = self.value.compile(environment)   
            else:
                if (self.type):
                    val = self.value.compile(environment) 
                else:
                    val = self.value['value'].compile(environment)   
                    if val.getType() == Type.MSTRUCT or val.getType() == Type.STRUCT:
                        if self.value['tipo'] != val.auxType:    
                            generator.setException(Exception("Semántico", f"Tipo incorrecto'{self.id}'", self.line, self.column))
                            return 
                    elif(self.value['tipo'] != val.getType()):
                        generator.setException(Exception("Semántico", f"Tipo incorrecto'{self.id}'", self.line, self.column))
                        return 

            #Guardado y obtencion de la variable
            #Contiene la posicion para asignarlo en el heap
            if(isAssign == None): # Solo se debe de crear si no existe
                if (val.type == Type.STRUCT or val.type == Type.MSTRUCT):
                    newVar = environment.setVariable(self.id, val.getType(), True, val.getAuxType(), val.getAttributes(), val.getValues())
                elif (val.type == Type.ARRAY):
                    newVar = environment.setVariable(self.id, val.getType(), True, val.getAuxType(), val.getAttributes(), val.getValues())
                else:
                    newVar = environment.setVariable(self.id, val.getType(), False)
            
            # Obtencion de posicion de la variable 
            if(isAssign == None): # Esta validacion se da solo si el id no se ha creado
                tempPos = newVar.pos
                if(not newVar.isGlobal):
                    tempPos = generator.addTemp()
                    generator.addExp(tempPos, 'P', newVar.pos, "+")
            else: 
                tempPos = isAssign.pos

            if(val.type == Type.BOOL):
                tempLbl = generator.newLabel()
                
                generator.putLabel(val.trueLbl)
                generator.setStack(tempPos, "1")
                
                generator.addGoto(tempLbl)

                generator.putLabel(val.falseLbl)
                generator.setStack(tempPos, "0")

                generator.putLabel(tempLbl)
            else:
                generator.setStack(tempPos, val.value)
            generator.addSpace()
        else: # asignacion de un valor para un struct 
            var = environment.getVariable(self.id[0])

            if var == None:
                generator.setException(Exception("Semántico", f"'{self.id}' is not define", self.line, self.column))
                return 

            if var.getType() == Type.STRUCT or var.getType() == Type.MSTRUCT:

                generator.addComment("BEGIN STRUCT")

                # ejecutando nuevo valor
                value = self.value.compile(environment)
                struct = environment.getStruct(var.getAuxType())

                tempH = generator.addTemp()
                for x in range(len(self.id)-1):
                    x =+ 1 # empieza en 1 por que el 0 es el struct 
                    counter = 0
                    for s in struct.attributes:
                        if (s['id'] == self.id[x]):
                            generator.getStack(tempH, var.pos)
                            generator.addExp(tempH, tempH, counter, '+')
                            generator.setHeap(tempH, value.getValue())
                            break
                        counter +=1
                    
                generator.addComment("END STRUCT")
            else: # is array
                self.dec_array(var, environment, self.id[1])

    def dec_array(self, value, environment, access):
        auxGen = Generator()
        generator = auxGen.getInstance()

        size = len(access)
        tempItem = generator.addTemp() # guardando el puntero la posición encontrada
        for i in range(size):
            if i == 0: # primera iteracion 
                lblTrue = generator.newLabel()
                lblFalse = generator.newLabel()
                lblExit = generator.newLabel()

                tempAccess = generator.addTemp() # valor de index a acceder
                temp = generator.addTemp()

                generator.addExp(tempAccess, access[i].value, '', '')

                generator.addExp(temp, value.pos, '', '')
                generator.getHeap(tempItem, temp)

                # comprobando que no exeda los limites
                generator.addIf(tempAccess, '1', '<', lblTrue) # limite inferior
                generator.addIf(tempAccess, tempItem, '>', lblTrue) #
                generator.addGoto(lblFalse)
                generator.putLabel(lblTrue)
                generator.printBoundsError()
                generator.addExp(tempItem, '0', '', '') # default result
                generator.addGoto(lblExit)
                generator.putLabel(lblFalse)# no exedio los limites
                
                generator.addExp(tempItem, temp, tempAccess, '+')
                val = self.value.compile(environment)
                if i == size-1:
                    generator.setHeap(tempItem, val.getValue()) # guardando nuevo valor
                else:
                    generator.getHeap(tempItem, tempItem) # retornando posición del nuevo arreglo
                generator.putLabel(lblExit) # salida 
            else: # mas accesos
                lblTrue = generator.newLabel()
                lblFalse = generator.newLabel()
                lblExit = generator.newLabel()

                tempAccess = generator.addTemp() # valor de index a acceder
                temp = generator.addTemp()

                generator.addExp(tempAccess, access[i].value, '', '')

                generator.addExp(temp, tempItem, '', '') # accediendo al nuevo arreglo
                generator.getHeap(tempItem, temp)

                # comprobando que no exeda los limites
                generator.addIf(tempAccess, '1', '<', lblTrue) # limite inferior
                generator.addIf(tempAccess, tempItem, '>', lblTrue) #
                generator.addGoto(lblFalse)
                generator.putLabel(lblTrue)
                generator.printBoundsError()
                generator.addExp(tempItem, '0', '', '') # default result
                generator.addGoto(lblExit)
                generator.putLabel(lblFalse)# no exedio los limites
                
                generator.addExp(tempItem, temp, tempAccess, '+')
                val = self.value.compile(environment)
                if i == size-1:
                    generator.setHeap(tempItem, val.getValue()) # guardando nuevo valor
                else:
                    generator.getHeap(tempItem, tempItem) # retornando posición del nuevo arreglo
                generator.putLabel(lblExit) # salida 


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass