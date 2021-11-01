
class Symbol:
    def __init__(self, id, type, position = 0, globalVar = None, inHeap = None):
        self.id = id 
        self.auxType = ''
        # self.value = value 
        self.type = type 
        self.isTemp = None
        self.trueLbl = ''
        self.falseLbl = ''
        self.isGlobal = globalVar
        self.inHeap = inHeap
        self.pos = position
        self.attributes = [] # types attributes
        self.values = []
        self.line = 0
        self.column = 0
        self.enviroment = ""
    
    def getId(self):
        return self.id
            
    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column

    def getAuxType(self):
        return self.auxType

    def setAuxType(self, auxType):
        self.auxType = auxType

    def getType(self):
        return self.type

    def getIsTemp(self):
        return self.isTemp

    def setIsTemp(self, isTemp):
        self.isTemp = isTemp

    def setAttributes(self,attributes):
        self.attributes = attributes 

    def getAttributes(self):        
        return self.attributes

    def setEnviroment(self, enviroment):
        self.enviroment = enviroment

    def getEnviroment(self):
        return self.enviroment

    def setValues(self, values):
        self.values = values 

    def getValues(self):        
        return self.values
