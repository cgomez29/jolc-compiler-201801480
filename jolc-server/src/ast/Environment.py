from src.ast.Type import Type
from src.ast.SymbolFunction import SymbolFunction
from src.ast.Symbol import Symbol


class Environment:

    def __init__(self, previous):
        self.previous = previous
        self.name = ""
        self.variables = {}
        self.functions = {}
        self.structs = {}
        self.symbolStructs = {}

        # Nuevo
        self.size = 0
        self.breakLbl = ''
        self.continueLbl = ''
        self.returnLbl = '' 

        self.currentFunction = None

        if(previous != None):
            self.size = self.previous.size
            self.breakLbl = self.previous.breakLbl 
            self.continueLbl = self.previous.continueLbl 
            self.returnLbl = self.previous.returnLbl 
            self.currentFunction = self.previous.currentFunction
    
    def setName(self, name):
        self.name = name 

    def getName(self):
        return self.name

    def getVariables(self):
        return self.variables

    def getStructs(self):
        return self.structs

    def getFunctions(self):
        return self.functions

    def getVariable(self, id):
        env = self 
        while env != None: 
            if id in env.variables.keys(): return env.variables[id]
            env = env.previous
        return None

    def setVariable(self, id, type, inHeap, auxType = '', typeAttributes = [], values = []):
        if id in self.variables.keys():
            print("Variable ya existe")
        else:
            newSymbol = Symbol(id, type, self.size, self.previous == None, inHeap)
            newSymbol.setAuxType(auxType)
            newSymbol.setAttributes(typeAttributes)
            newSymbol.setValues(values)
            newSymbol.setEnviroment(self.name)
            self.size += 1
            self.variables[id] = newSymbol
        return self.variables[id]

    def setStruct(self, id, struct):
        self.structs[id] = struct

    # Retorna el simbolo del struct buscado
    def getStruct(self, id):
        env = self 
        while env != None: 
            if id in env.structs.keys(): return env.structs[id]
            env = env.previous
        return None

    def getGlobalEnviroment(self):
        environment = self
        while environment.previous != None: 
            environment = environment.previous 
        return environment

    def getIfEnvironment(self):
        environment = self
        while environment.anterior != None: 
            if environment.name != "if": 
                break
            environment = environment.anterior 
        return environment

    def getForEnvironment(self):
        environment = self
        while environment.anterior != None: 
            if environment.name != "for": 
                break
            environment = environment.anterior 
        return environment


    def getSize(self):
        return self.size

    def getGlobal(self):
        env = self
        while env.prev != None:
            env = env.prev
        return env

    def setEnvironmentFunction(self, currentFunction, returnLbl):
        self.returnLbl = returnLbl
        self.size = 1
        self.currentFunction = currentFunction


    def getFunction(self, id):
        return self.functions[id]

    # Retorna el simbolo de la funcion guardada
    def searchFunction(self, id):
        env = self 
        while env != None: 
            if id in env.functions.keys(): return env.functions[id]
            env = env.previous
        return None

    def addFunction(self, id, func):
        if( id not in self.functions.keys()):
            if func.type == Type.ANY:
                type = Type.INT64
            else:
                type = func.type 
            sfunc = SymbolFunction(id, type, len(func.parameters), func.parameters, func.line, func.column)
            sfunc.setEnviroment(self.name)
            self.functions[id] = sfunc
            return True
        return False 