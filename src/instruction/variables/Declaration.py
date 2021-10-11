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
            # generator.addComment("Inicio Variable")
            val = self.value.compile(environment)
            # generator.addComment("Fin de variable")

            #Guardado y obtencion de la variable
            #Contiene la posicion para asignarlo en el heap
            if (val.type == Type.STRUCT or val.type == Type.MSTRUCT):
                newVar = environment.setVariable(self.id, val.getType(), True, val.getAuxType(), val.getAttributes(), val.getValues())
            elif (val.type == Type.ARRAY):
                newVar = environment.setVariable(self.id, val.getType(), True, val.getAuxType(), val.getAttributes(), val.getValues())
            else:
                newVar = environment.setVariable(self.id, val.getType(), (val.type == Type.STRING))
            
            # Obtencion de posicion de la variable
            tempPos = newVar.pos
            if(not newVar.isGlobal):
                tempPos = generator.addTemp()
                generator.addExp(tempPos, 'P', newVar.pos, "+")

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
            var_struct = environment.getVariable(self.id[0])

            if var_struct == None:
                generator.setException(Exception("Semántico", f"No se definio un valor para'{self.id}'", self.line, self.column))
                return 
            generator.addComment("init set struct")

            # ejecutando nuevo valor
            value = self.value.compile(environment)
            struct = environment.getStruct(var_struct.getAuxType())

            tempH = generator.addTemp()
            for x in range(len(self.id)-1):
                x =+ 1 # empieza en 1 por que el 0 es el struct 
                counter = 0
                for s in struct.attributes:
                    if (s['id'] == self.id[x]):
                        generator.getStack(tempH, var_struct.pos)
                        generator.addExp(tempH, tempH, counter, '+')
                        generator.setHeap(tempH, value.getValue())
                        break
                    counter +=1
                
            generator.addComment("fin set struct")


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass