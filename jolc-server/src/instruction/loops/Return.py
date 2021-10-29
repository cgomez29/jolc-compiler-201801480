from src.ast.Generator import Generator
from src.abstract.Expression import Expression

class Return(Expression):
    def __init__(self, value, line, column):
        super().__init__(line, column)
        self.value = value

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        value = self.value.compile(environment).getValue()
        generator.setStack('P', value) 
        generator.addGoto(environment.returnLbl)


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass