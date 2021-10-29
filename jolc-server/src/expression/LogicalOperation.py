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

        self.checkLabels()
        lblAndOr = ''
        ret = Return(None, Type.BOOL, False)

        if self.typeOperation == TypeOperation.AND:
            lblAndOr = self.left.trueLbl = generator.newLabel()
            self.right.trueLbl = self.trueLbl
            self.left.falseLbl = self.right.falseLbl = self.falseLbl
        elif self.typeOperation == TypeOperation.OR:
            self.left.trueLbl = self.right.trueLbl = self.trueLbl
            lblAndOr = self.left.falseLbl = generator.newLabel()
            self.right.falseLbl = self.falseLbl
        else:
            ret.trueLbl = self.falseLbl
            ret.falseLbl = self.trueLbl
            return ret  

        left = self.left.compile(environment)
        if left.getType() != Type.BOOL:
            generator.setException(Exception("Semántico", f"Cannot be used in Boolean expression", self.line, self.column))
            return
        generator.putLabel(lblAndOr)
        right = self.right.compile(environment)
        if right.getType() != Type.BOOL:
            generator.setException(Exception("Semántico", f"Cannot be used in Boolean expression", self.line, self.column))
            return

        generator.addSpace()
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret

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