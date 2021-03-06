from src.abstract.Expression import Expression
from src.ast.Generator import Generator
from src.ast.Type import TypeOperation
from src.ast.TypeTable import TypeTable
from src.ast.Type import Type
from src.abstract.Return import Return
from src.exception.Exception import Exception

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

        if(left.getType() == Type.STRING and rigth.getType() == Type.INT64 and
            self.typeOperation == TypeOperation.POTENCIA): # String ^ INT64
            generator.fRepeatString()
            return self.repeatString(environment, left.getValue(), rigth.getValue())

        # Concatenacion de String
        if(left.getType() == Type.STRING and rigth.getType() == Type.STRING and
            self.typeOperation == TypeOperation.MULTIPLICACION): # String * String
            generator.fConcatString()
            return self.concatString(environment, left.getValue(), rigth.getValue())

        # power
        if self.typeOperation == TypeOperation.POTENCIA:
            generator.fPower()
            return self.callPower(environment, left.getValue(), rigth.getValue())

        finalType = TypeTable()
        resultType = finalType.getType(left.getType(), rigth.getType()) 


        if(resultType == Type.ERROR):
            generator.setException(Exception("Semántico", f"Type error", self.line, self.column))
            return

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
        
        # Comprobación dinámica
        generator.freeTemp(left.getValue())
        generator.freeTemp(rigth.getValue())
        if op == '/' or op == '%':
            lblTrue = generator.newLabel()
            lblExit = generator.newLabel()
            generator.addIf(rigth.getValue(), '0', '!=', lblTrue)
            generator.printMathError()
            generator.addExp(temp, '0', '', '')
            generator.addGoto(lblExit)
            generator.putLabel(lblTrue)

            if op == '%':
                generator.math = True # coloca la libreria en las importaciones
                generator.addExpModulo(temp, left.getValue(), rigth.getValue()) 
            else:
                generator.addExp(temp, left.getValue(), rigth.getValue(), op) 
            generator.putLabel(lblExit)
        else:
            generator.addExp(temp, left.getValue(), rigth.getValue(), op)

        return Return(temp, resultType, True)

    def callPower(self, environment, param1, param2):
        auxG = Generator()
        generator = auxG.getInstance()
        # paso de parámetros
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
        generator.callFun('native_power')
        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return Return(temp, Type.INT64, True)


    def repeatString(self, environment, param1, param2):
        auxG = Generator()
        generator = auxG.getInstance()
        # paso de parámetros
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
        generator.callFun('repeatString')
        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return Return(temp, Type.STRING, True)

    def concatString(self, environment, param1, param2):
        auxG = Generator()
        generator = auxG.getInstance()
        # paso de parámetros
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
        generator.callFun('concatString')

        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return Return(temp, Type.STRING, True)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        return 'ARITHMETIC_OPERATION'