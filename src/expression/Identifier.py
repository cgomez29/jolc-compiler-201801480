from src.abstract.Return import Return
from src.ast.Generator import Generator
from src.abstract.Expression import Expression
from src.ast.Type import Type

class Identifier(Expression):
    def __init__(self, id, type, line, column):
        super().__init__(line, column)
        self.id = id 
        self.type = type 

    def compile(self, environment):
        auxG = Generator()
        generator =  auxG.getInstance()
        generator.addComment("Start identifier")

        var = environment.getVariable(self.id)   
        
        if(var == None):
            print("Error, no existe la variable")
            return 

        # Temporal para guardar la variable
        temp = generator.addTemp()

        #Obtencion de la posicion de la variable
        tempPos = var.pos 
        if(not var.isGlobal):
            tempPos = generator.addTemp()
            generator.addExp(tempPos, 'P', var.pos, "+")
        generator.getStack(temp, tempPos)

        if var.type != Type.BOOL:
            generator.addComment("Fin identifier")
            generator.addSpace()
            return Return(temp, var.type, True)

        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()
        
        generator.addIf(temp, '1', '==', self.trueLbl)
        generator.addGoto(self.falseLbl)

        generator.addComment("fin identifier")
        generator.addSpace()

        ret = Return(None, Type.BOOLEAN, False)
        ret.trueLbl = self.trueLbl
        ret.falseLbl = self.falseLbl
        return ret

    def graph(self, g, father):
        pass

    def getNameSon(self):
        return "IDENTIFIER"