from src.ast.Generator import Generator
from src.abstract.Return import Return
from src.abstract.Expression import Expression

class Unary(Expression):
    def __init__(self, expression, line, column):
        self.line = line 
        self.column = column
        self.expression = expression
        self.trueLbl = ''
        self.falseLbl = ''

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        temp = generator.addTemp()

        value = self.expression.compile(environment)
        
        generator.addExp(temp, '0', value.getValue(), '-')
        
        return Return(temp, value.getType(), True) 


    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass