from src.exception.Exception import Exception
from src.ast.Generator import Generator
from src.abstract.Expression import Expression 
from src.abstract.Return import Return
from src.ast.Type import Type

class ExpCall(Expression):
    def __init__(self, id, parameters, line, column):
        super().__init__(line, column)
        self.id = id 
        self.parameters = parameters

    def compile(self, environment):
        aucG = Generator()
        generator = aucG.getInstance()

        symbolFunction = environment.searchFunction(self.id)
        if symbolFunction == None:
            generator.setException(Exception("Semántico", f"Cannot find name: {self.id}'", self.line, self.column))
            return 

        paramsValues = []
        # retorna el tamaño 
        size = generator.saveTemps(environment) 

        registeredLength = len(symbolFunction.params)
        incomingLength = len(self.parameters)

        if registeredLength != incomingLength:
            generator.setException(Exception("Semántico", f"Expected {registeredLength} arguments, but got {incomingLength}", self.line, self.column))
            return 

        index = 0

        for p in self.parameters:
            compiledParam = p.compile(environment)
            registeredType = symbolFunction.params[index]['tipo']
            incomingType = compiledParam.getType()

            if registeredType != incomingType:
                generator.setException(Exception("Semántico", f"Argument of type {incomingType} is not assignable to parameter of type {registeredType}", self.line, self.column))
                return 

            if incomingType == Type.BOOL:
                temp = generator.addTemp()
                generator.freeTemp(temp)

                tempLabel = generator.newLabel()
                generator.putLabel(compiledParam.trueLbl)
                generator.addExp(temp, 'P', environment.size + index + 1, '+')
                generator.setStack(temp, '1')
                generator.addGoto(tempLabel)
                generator.putLabel(compiledParam.falseLbl)
                generator.addExp(temp, 'P', environment.size + index + 1, '+')
                generator.setStack(temp, '0')
                generator.putLabel(tempLabel) 

            paramsValues.append(compiledParam)
            index +=1

        temp = generator.addTemp()
        generator.freeTemp(temp)
        if (len(paramsValues) != 0):
            generator.addExp(temp, 'P', environment.size + 1, '+')
            i = 0
            for value in paramsValues:
                if(value.getType() != Type.BOOL):
                    generator.freeTemp(value.getValue())
                    generator.setStack(temp, value.getValue())
                if i != len(paramsValues) -1:
                    generator.addExp(temp, temp, '1', '+')

        generator.newEnv(environment.size)
        generator.callFun(self.id)
        generator.getStack(temp, 'P')
        generator.retEnv(environment.size)
        generator.recoverTemps(environment, size)
        generator.addTempStorage(temp) # TODO: addTemp

        if symbolFunction.getType() != Type.BOOL:
            return Return(temp, symbolFunction.getType(), True)

        auxReturn = Return('', symbolFunction.getType(), False)
        if self.trueLbl == '':
            self.trueLbl = generator.newLabel()
        if self.falseLbl == '':
            self.falseLbl = generator.newLabel()
        generator.addIf(temp, '1', '==', self.trueLbl)
        generator.addGoto(self.falseLbl)
        auxReturn.trueLbl = self.trueLbl
        auxReturn.falseLbl = self.falseLbl 
        return auxReturn

    def callTrunc(self, environment, value):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.fTrunc()

        paramTemp = generator.addTemp()

        generator.addExp(paramTemp, 'P', environment.getSize(), '+')
        generator.addExp(paramTemp, paramTemp, '1', '+')
        generator.setStack(paramTemp, value)

        generator.newEnv(environment.getSize())
        generator.callFun('trunc')

        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return temp

    def callParse(self, environment, value):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.fParse()

        paramTemp = generator.addTemp()

        generator.addExp(paramTemp, 'P', environment.getSize(), '+')
        generator.addExp(paramTemp, paramTemp, '1', '+')
        generator.setStack(paramTemp, value)

        generator.newEnv(environment.getSize())
        generator.callFun('parse')

        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return temp

    def callUpperCase(self, environment, value):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.fUpperCase()

        paramTemp = generator.addTemp()

        generator.addExp(paramTemp, 'P', environment.getSize(), '+')
        generator.addExp(paramTemp, paramTemp, '1', '+')
        generator.setStack(paramTemp, value)

        generator.newEnv(environment.getSize())
        generator.callFun('uppercase')

        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return temp

    def callLowerCase(self, environment, value):
        auxG = Generator()
        generator = auxG.getInstance()
        generator.fLowerCase()

        paramTemp = generator.addTemp()

        generator.addExp(paramTemp, 'P', environment.getSize(), '+')
        generator.addExp(paramTemp, paramTemp, '1', '+')
        generator.setStack(paramTemp, value)

        generator.newEnv(environment.getSize())
        generator.callFun('lowercase')

        temp = generator.addTemp()
        generator.getStack(temp, 'P')
        generator.retEnv(environment.getSize())
        return temp

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass