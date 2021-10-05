from src.abstract.Expression import Expression
from src.ast.Generator import Generator
from src.ast.Type import TypeOperation
from src.ast.TypeTable import TypeTable
from src.abstract.Return import Return

class ArithmeticOperation(Expression):
    def __init__(self, left, rigth, typeOperation, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.rigth = rigth
        self.typeOperation = typeOperation  

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        left = self.left.compile(environment)
        rigth = self.rigth.compile(environment)

        finalType = TypeTable()

        resultType =  finalType.getType(left.getType(), rigth.getType()) 

        temp = generator.addTemp()

        op = '' 
        if (self.typeOperation == TypeOperation.SUMA):
            op = '+'
        elif (self.typeOperation == TypeOperation.RESTA):
            op = '-'
        elif (self.typeOperation == TypeOperation.MULTIPLICACION):
            op = '*'
        elif (self.typeOperation == TypeOperation.DIVISION):
            op = '/'
        
        generator.addExp(temp, left.getValue(), rigth.getValue(), op)
        return Return(temp, resultType, True)


    def graph(self, g, father):
        pass

    def getNameSon(self):
        return 'ARITHMETIC_OPERATION'