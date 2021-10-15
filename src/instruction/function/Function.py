from src.ast.Environment import Environment
from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type

class Function(Instruction):
    def __init__(self, id, parameters, instructions, line, column):
        Instruction.__init__(self, line, column)
        self.id = id 
        self.parameters = parameters
        self.instructions = instructions 
    
    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.clearTemps()

        environment.setFunction(self.id, self) # guardando funcion en el entorno global
        
        newEnv = Environment(environment)
        newEnv.setFunction(self.id, self)
        newEnv.setName('function')

        returnLabel = generator.newLabel()
        newEnv.returnLbl = returnLabel

        generator.addBeginFunc(self.id)

        newEnv.size = 1 # new env 
        for p in self.parameters:
            newEnv.setVariable(p, Type.ANY, False)

        for i in self.instructions:
            i.compile(newEnv)

        # generator.addGoto(returnLabel)
        generator.putLabel(returnLabel)

        generator.addEndFunc()
        generator.clearTemps()

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass