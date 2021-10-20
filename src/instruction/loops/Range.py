from src.ast.Generator import Generator
from src.ast.Type import Type
from src.abstract.Return import Return
from src.abstract.Expression import Expression


class Range(Expression):
    def __init__(self, start, end, line, column):
        super().__init__(line, column)
        self.start = start 
        self.end = end 

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        tempRange =  generator.addTemp()
        start = self.start.compile(environment)
        end = self.end.compile(environment)

        generator.addExp(tempRange, 'H', '', '')
        generator.setHeap('H', start.getValue())
        generator.nextHeap()
        generator.setHeap('H', end.getValue())
        generator.nextHeap()

        return Return(tempRange, Type.RANGE, True)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass