from src.ast.Generator import Generator
from src.abstract.Expression import Expression
from src.ast.Type import Type

class Return(Expression):
    def __init__(self, value, line, column):
        super().__init__(line, column)
        self.value = value

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        value = self.value.compile(environment)
        if(value.type == Type.BOOL):
            tempLbl = generator.newLabel()
            
            generator.putLabel(value.trueLbl)
            generator.setStack('P', '1')
            generator.addGoto(tempLbl) 

            generator.putLabel(value.falseLbl)
            generator.setStack('P', '0')

            generator.putLabel(tempLbl)
        else:
            generator.setStack('P', value.value)
        generator.addGoto(environment.returnLbl)
        # generator.setStack('P', value) 
        # generator.addGoto(environment.returnLbl)


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass