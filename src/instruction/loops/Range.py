from src.ast.Type import Type
from src.abstract.Return import Return
from src.abstract.Expression import Expression


class Range(Expression):
    def __init__(self, start, end, line, column):
        super().__init__(line, column)
        self.start = start 
        self.end = end 

    def compile(self, environment):
        

        return Return("r", Type.RANGE, False)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass