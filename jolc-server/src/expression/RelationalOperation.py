from src.abstract.Expression import Expression 
from src.ast.Generator import Generator
from src.ast.TypeTable import Type
from src.abstract.Return import Return
from src.ast.Type import TypeOperation

class RelationalOperation(Expression):

    def __init__(self, left, rigth, type, line, column):
        Expression.__init__(self, line, column)
        self.left = left
        self.rigth = rigth
        self.type = type  

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()

        # generator.addComment('Start relational expression')

        left = self.left.compile(environment)
        rigth = None

        result = Return(None, Type.BOOL, False)

        if left.getType() != Type.BOOL:
            rigth = self.rigth.compile(environment)
            if ((left.getType() == Type.INT64 or left.getType() == Type.FLOAT64) and
                (rigth.getType() == Type.INT64 or rigth.getType() == Type.FLOAT64) or left.getType() == Type.ANY):
                self.checkLabels()
                generator.freeTemp(left.getValue())
                generator.freeTemp(rigth.getValue())
                generator.addIf(left.getValue(), rigth.getValue(), self.getOp(), self.trueLbl)
                generator.addGoto(self.falseLbl)
            elif (left.getType() == Type.STRING and rigth.getType() == Type.STRING):
                self.checkLabels()
                generator.fCompareString()
                generator.freeTemp(left.getValue())
                generator.freeTemp(rigth.getValue())
                generator.addIf(self.compareString(environment, left.getValue(), rigth.getValue()), '1', '==', self.trueLbl)
                generator.addGoto(self.falseLbl)

        else: 
            gotoRigth = generator.newLabel()
            leftTemp = generator.addTemp()
            generator.freeTemp(leftTemp)

            generator.putLabel(left.trueLbl)    
            generator.addExp(leftTemp, '1', '','')
            generator.addGoto(gotoRigth)

            generator.putLabel(left.falseLbl)
            generator.addExp(leftTemp, '0', '', '')

            generator.putLabel(gotoRigth)

            right = self.rigth.compile(environment)
            if right.type != Type.BOOL:
                # print("Error, no se pueden comparar")
                return
            gotoEnd = generator.newLabel()
            rightTemp = generator.addTemp()
            generator.freeTemp(right)

            generator.putLabel(right.trueLbl)
            
            generator.addExp(rightTemp, '1', '', '')
            generator.addGoto(gotoEnd)

            generator.putLabel(right.falseLbl)
            generator.addExp(rightTemp, '0', '', '')

            generator.putLabel(gotoEnd)

            self.checkLabels()
            generator.addIf(leftTemp, rightTemp, self.getOp(), self.trueLbl)
            generator.addGoto(self.falseLbl)

        # generator.addComment("FIN DE EXPRESION RELACIONAL")
        generator.addSpace()
        result.trueLbl = self.trueLbl
        result.falseLbl = self.falseLbl

        return result     

    def compareString(self, environment, param1, param2):
        auxG = Generator()
        generator = auxG.getInstance()
        # paso de par??metros
        # Parametro 1 
        paramTemp = generator.addTemp()
        generator.addExp(paramTemp, 'P', environment.getSize(), '+')
        generator.addExp(paramTemp, paramTemp, '1', '+')
        generator.setStack(paramTemp, param1)
        # Parametro 2 
        paramTemp1 = generator.addTemp()
        generator.addExp(paramTemp1, paramTemp, '1', '+')
        generator.setStack(paramTemp1, param2)
        
        # Cambio y llamada a entorno
        generator.newEnv(environment.getSize())
        generator.callFun('compareString')
        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return temp

    def checkLabels(self):
        auxG = Generator()
        generator = auxG.getInstance()

        if (self.trueLbl == ''):
            self.trueLbl = generator.newLabel()
        if (self.falseLbl == ''):
            self.falseLbl = generator.newLabel()

    def getOp(self): 
        if(self.type == TypeOperation.IGUAL):
            return '=='
        elif(self.type == TypeOperation.MAYORQ):
            return '>'
        elif(self.type == TypeOperation.MENORQ):
            return '<'
        elif(self.type == TypeOperation.MAYORIQ):
            return '>='
        elif(self.type == TypeOperation.MENORIQ):
            return '<='
        elif(self.type == TypeOperation.DIFERENTE):
            return '!='

    def graph(self, g, father):
        pass

    def getNameSon(self):
        return 'RELATIONAL_OPERATION'