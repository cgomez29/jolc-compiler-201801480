from src.abstract.Expression import Expression
from src.ast.Type import Type
from src.ast.Generator import Generator
from src.abstract.Return import Return

class Literal(Expression):
    def __init__(self,value,type,line,column):
        Expression.__init__(self, line, column)
        self.value = value 
        self.type = type 

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        if(self.type == Type.INT64 or self.type == Type.FLOAT64):
            return Return(str(self.value), self.type, False)
        if self.type == Type.BOOL:
            if self.trueLbl == '':
                self.trueLbl = generator.newLabel()
            if self.falseLbl == '':
                self.falseLbl = generator.newLabel()
            
            if(self.value):
                generator.addGoto(self.trueLbl)
                generator.addComment("goto -> evitar error de GO")
                generator.addGoto(self.falseLbl)
            else:
                generator.addGoto(self.falseLbl)
                generator.addComment("goto -> evitar error de GO")
                generator.addGoto(self.trueLbl)

            ret = Return(str(self.value), self.type, False)
            ret.falseLbl = self.falseLbl
            ret.trueLbl = self.trueLbl
            return ret
        elif self.type == Type.STRING:
            retTemp = generator.addTemp()
            generator.addExp(retTemp, 'H', '', '')

            for char in str(self.value):
                generator.setHeap('H', ord(char))
                generator.nextHeap()
            generator.setHeap('H', '-1') # fin de cadena
            generator.nextHeap()
            return Return(retTemp, Type.STRING, True)
        else:
            # Float64 and Int64
            return Return(str(self.value), self.type, False)
        
    def graph(self, g, father):
        pass

    def getNameSon(self):
        return 'LITERAL'