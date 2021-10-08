from src.exception.Exception import Exception
from src.ast.Generator import Generator
from src.abstract.Expression import Expression 
from src.abstract.Return import Return
from src.ast.Type import Type

class Call(Expression):
    def __init__(self, id, parameters, line, column):
        super().__init__(line, column)
        self.id = id 
        self.parameters = parameters

    def compile(self, environment):
        aucG = Generator()
        generator = aucG.getInstance()

        if(self.id == "uppercase"):
            for p in self.parameters:
                ret = p.compile(environment)
                value = ret.getValue()
                # returnType = ret.getType()
            return Return(self.callUpperCase(environment, value), Type.STRING, False) 
        elif(self.id == 'lowercase'):
            for p in self.parameters:
                ret = p.compile(environment)
                value = ret.getValue()
                # returnType = ret.getType()
            return Return(self.callLowerCase(environment, value), Type.STRING, False) 
        elif(self.id == 'parse'):
            type = self.parameters[0].compile(environment)
            if(type.getType() != Type.FLOAT64):
                return 
            param1 = self.parameters[1].compile(environment)
            
            return Return(self.callParse(environment, param1.getValue()), Type.FLOAT64, False)
        elif(self.id == 'trunc'):
            param1 = self.parameters[0].compile(environment)
            return Return(self.callTrunc(environment, param1.getValue()), Type.FLOAT64, False)

        sizeActual = environment.size

        function = environment.getFunction(self.id)
        struct = environment.getStruct(self.id) 

        if(struct == None):
            if(function == None):
                generator.setException(Exception("Semántico", f"No existe la función '{self.id}'", self.line, self.column))
                return
            # debe de tener la misma cantidad de parametros
            # if (len(function.getId().parameters) != len(self.parameters)):
            #     generator.setException(Exception("Semántico", f"Cantidad de parámetros incorrectos en '{self.id}'", self.line, self.column))
            #     return

            temp = generator.addTemp()
            returnType = None
            
            for p in self.parameters:
                environment.size += 1
                generator.addExp(temp, 'P', environment.size, '+')
                ret = p.compile(environment)
                value = ret.getValue()
                returnType = ret.getType()
                generator.setStack(temp, value)

            generator.newEnv(sizeActual)
            generator.callFun(self.id)
            generator.getStack(temp, 'P')
            generator.retEnv(sizeActual)

            return Return(temp, returnType, False)

        else: # is struct
            # Posicion de inicio en el heap
            tempStruct = generator.addTemp()
            tempH = generator.addTemp()
            generator.addExp(tempStruct, 'H', '', '')
            generator.addExp(tempH, tempStruct, '', '')

            if(len(self.parameters) != len(struct.attributes)):
                generator.setException(Exception("Semántico", f"Struct: cantidad de atributos incorrectos'{self.id}'", self.line, self.column))
                return 
            generator.addExp('H', 'H', len(self.parameters), '+') # creando las pos a las referencias hacia sus atributos
            
            for p in self.parameters:
                generator.setHeap(tempH, p.compile(environment).getValue())
                generator.addExp(tempH, tempH, '1', '+')

            type = Type.STRUCT
            if(struct.mutable):
                type = Type.MSTRUCT
            return Return(tempStruct, type, False)

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