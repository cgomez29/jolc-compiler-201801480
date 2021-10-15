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

        function = environment.getFunction(self.id)

        if(function == None):
            generator.setException(Exception("Semántico", f"No existe la función '{self.id}'", self.line, self.column))
            return
       
        generator.addSpace()
        if environment.getName() != 'function': 
            generator.addComment("INICIO llamada a funcion1 <====================")
            temp = generator.addTemp()
            returnType = None

            counter = 0     
    
            for p in self.parameters:
                ret = p.compile(environment)
                counter+=1
                generator.addExp(temp, 'P', environment.size + counter, '+')
                value = ret.getValue()
                returnType = ret.getType()
                generator.setStack(temp, value)

            generator.newEnv(environment.size)
            generator.callFun(self.id)
            generator.getStack(temp, 'P')
            generator.retEnv(environment.size)
            generator.addComment("FIN llamada a funcion <====================")
            generator.addSpace()
            return Return(temp, returnType, False)
        else:
            generator.addComment("INICIO llamada a funcion2 <====================")
            temp_save = (generator.getSaveTemps())
            returnType = None

            if len(temp_save) > 0:
                generator.addComment("Guardando temporales")
                saveSize = environment.size 
                t = generator.addTemp()
                generator.addExp(t, 'P', saveSize, '+')
                generator.setStack(t, temp_save[-1])
                generator.addComment("FIN Guardando temporales")

            generator.clearTemps()
            temp = generator.addTemp()
            
            flag = 1
            currentSize = environment.size
            for p in self.parameters:
                # generator.clearTemps()# eliminando temporales guardados en esta llamada
                environment.size +=1
                ret = p.compile(environment)
                environment.size -=1
                generator.addExp(temp, 'P', currentSize+flag, '+')
                flag += 1
                value = ret.getValue()
                
                generator.clearTemps() # borando temporales
                generator.saveTemps(value) # agregando temporales

                returnType = ret.getType()
                generator.setStack(temp, value)

            generator.newEnv(currentSize)
            generator.callFun(self.id)
            generator.getStack(temp, 'P')
            generator.retEnv(currentSize)    
            
            if len(temp_save) > 0:
                generator.addComment("Recuperando temporales")
                t = generator.addTemp()
                generator.addExp(t, 'P', saveSize, '+')
                generator.getStack(temp_save[-1], t)
                generator.addComment("FIN Recuperando temporales")

            generator.addComment("FIN llamada a funcion <====================")
            generator.addSpace()
            
            # generator.setSaveTemps(temp_save)
            generator.clearTemps() # TODO: Se modifico aca
            return Return(temp, returnType, False)

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