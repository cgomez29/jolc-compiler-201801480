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
        newEnv = Environment(environment)

        # exitLabel = generator.newLabel()
        environment.setFunction(self.id, self)
        generator.addBeginFunc(self.id)

        # temp = generator.addTemp()
        newEnv.size += 1##Contando cuantos valores ya hay
        for p in self.parameters:
            # tempParam = generator.addTemp()
            # generator.addExp(tempParam, 'P', '1', '+')
            newEnv.setVariable(p, Type.ANY, False)
            # generator.getStack(temp, tempParam)

        for i in self.instructions:
            
            i.compile(newEnv)

        # generator.addGoto(exitLabel)
        # generator.putLabel(exitLabel)

        generator.addEndFunc()

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass