from src.ast.Environment import Environment
from src.ast.Generator import Generator
from src.abstract.Expression import Expression 
from src.abstract.Return import Return
from src.ast.Type import Type
from src.exception.Exception import Exception

class Call(Expression):
    def __init__(self, id, parameters, line, column):
        super().__init__(line, column)
        self.id = id 
        self.parameters = parameters

    def compile(self, environment):
        aucG = Generator()
        generator = aucG.getInstance()

        sizeActual = environment.size

        function = environment.getFunction(self.id)

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

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass