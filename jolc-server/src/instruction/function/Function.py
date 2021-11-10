from src.ast.Environment import Environment
from src.exception.Exception import Exception
from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type

class Function(Instruction):
    def __init__(self, id, parameters, type, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.id = id 
        self.parameters = parameters
        self.instructions = instructions 
        self.preCompile = True
        self.type = type
    
    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        if self.preCompile:
            self.preCompile = False 
            if self.validateParams():
                generator.setException(Exception("Semántico", f"Duplicate identifier: '{self.id}'", self.line, self.column))
                return 
            if not environment.addFunction(self.id, self):
                generator.setException(Exception("Semántico", f"Duplicate function implementation: {self.id}'", self.line, self.column))
                return 

        # Creamos un  nuevo entorno
        newEnv = Environment(environment)
        newEnv.setName('function')

        symbolFunction = environment.getFunction(self.id)
        returnLabel = generator.newLabel()
        tempStorage = generator.getTempStorage()

        newEnv.setEnvironmentFunction(symbolFunction, returnLabel)
    
        for i in self.parameters:
            tipo = i['tipo']
            if isinstance(tipo, str):
                struct = newEnv.getStruct(tipo)
                newEnv.setVariable(i['id'], struct.getType() , False, tipo, struct.getAttributes())
                continue
            newEnv.setVariable(i['id'], i['tipo'], False)

        generator.clearTempStorage()

        generator.addBeginFunc(self.id)

        for i in self.instructions:
            i.compile(newEnv)

        generator.addGoto(returnLabel)
        generator.putLabel(returnLabel)

        generator.addEndFunc()
        generator.setTempStorage(tempStorage)


    def validateParams(self):
        params = []
        for i in self.parameters:
            if isinstance(i, str):
                if i in params: 
                    return True
                params.append(i)
            else:
                if i['id'] in params: 
                    return True
                params.append(i['id'])
        return False

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass