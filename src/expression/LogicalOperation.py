from src.abstract.Return import Return
from src.ast.Generator import Generator
from src.abstract.Expression import Expression 
from src.ast.Type import TypeOperation
from src.ast.Type import Type

class LogicalOperation(Expression):
    def __init__(self, left, right, typeOperation, line, column):
        super().__init__(line, column)    
        self.left = left
        self.right = right
        self.typeOperation = typeOperation  

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        left = self.left.compile(environment)
        rigth = None
        result = Return(None, Type.BOOL, False)
        if(self.typeOperation == TypeOperation.OR):
            # Etiqueta compartida true
            self.right.trueLbl = left.trueLbl
            generator.putLabel(left.falseLbl) # etiqueta false
            rigth = self.right.compile(environment)

            result.trueLbl = left.trueLbl
            result.falseLbl = rigth.falseLbl
        elif(self.typeOperation == TypeOperation.AND):
            self.right.falseLbl = left.falseLbl
            generator.putLabel(left.trueLbl) # etiqueta false
            rigth = self.right.compile(environment)

            result.trueLbl = rigth.trueLbl
            result.falseLbl = rigth.falseLbl
        elif(self.typeOperation == TypeOperation.NOT):
            result.trueLbl = left.falseLbl
            result.falseLbl = left.trueLbl
        
        return result

    def checkLabels(self):
        auxG = Generator()
        generator = auxG.getInstance()

        if (self.trueLbl == ''):
            self.trueLbl = generator.newLabel()
        if (self.falseLbl == ''):
            self.falseLbl = generator.newLabel()

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass