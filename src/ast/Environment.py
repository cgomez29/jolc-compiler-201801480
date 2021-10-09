from src.ast.Symbol import Symbol


class Environment:

    def __init__(self, previous):
        self.previous = previous
        self.name = ""
        self.variables = {}
        self.functions = {}
        self.structs = {}

        # Nuevo
        self.size = 0
        # print("ACTUAL", self.size)
        if(previous != None):
            # print("ES NUEVOO")
            self.size = self.previous.size
            # print("ES NUEVOO", self.size)
    
    def setName(self, name):
        self.name = name 

    def getName(self):
        return self.name

    def getVariable(self, id):
        env = self 
        while env != None: 
            if id in env.variables.keys(): return env.variables[id]
            env = env.previous
        return None

    def setVariable(self, id, type, inHeap, auxType = '', typeAttributes = [], values = []):
        newSymbol = Symbol(id, type, self.size, self.previous == None, inHeap)
        newSymbol.setAuxType(auxType)
        newSymbol.setAttributes(typeAttributes)
        newSymbol.setValues(values)
        if( id not in self.variables.keys()):
            self.size += 1
        self.variables[id] = newSymbol
        return self.variables[id]

    # Retorna el simbolo de la funcion guardada
    def getFunction(self, id):
        env = self 
        while env != None: 
            if id in env.functions.keys(): return env.functions[id]
            env = env.previous
        return None

    def setFunction(self, id, function):
        self.functions[id] = function

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