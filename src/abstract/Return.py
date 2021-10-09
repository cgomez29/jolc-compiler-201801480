
class Return:
    def __init__(self, value, type, isTemp, auxType = ''):
        self.value = value
        self.type = type
        self.auxType = auxType
        self.isTemp = isTemp
        self.trueLbl = ''
        self.falseLbl = ''
        self.attributes = [] #typos de los atributos si el struct no tiene definido el type 
        self.values = []

    def getValue(self):
        return self.value 
        
    def getType(self):
        return self.type

    def getAuxType(self):
        return self.auxType

    def setAuxType(self, auxType):
        self.auxType = auxType

    def setAttributes(self,attributes):
        self.attributes = attributes 

    def getAttributes(self):        
        return self.attributes

    def setValues(self, values):
        self.values = values 

    def getValues(self):        
        return self.values