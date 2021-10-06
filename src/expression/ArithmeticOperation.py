from src.abstract.Expression import Expression
from src.ast.Generator import Generator
from src.ast.Type import TypeOperation
from src.ast.TypeTable import TypeTable
from src.ast.Type import Type
from src.abstract.Return import Return

class ArithmeticOperation(Expression):
    def __init__(self, left, right, typeOperation, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.right = right
        self.typeOperation = typeOperation  

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        left = self.left.compile(environment)
        right = self.right.compile(environment)

        # finalType = TypeTable()

        # resultType = finalType.getType(left.getType(), rigth.getType()) 

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
        elif (self.typeOperation == TypeOperation.MODULO):
            op = '%'
        
        generator.addExp(temp, left.getValue(), right.getValue(), op)
        return Return(temp, Type.INT64, True)


    def graph(self, g, father):
        pass

    def getNameSon(self):
        return 'ARITHMETIC_OPERATION'