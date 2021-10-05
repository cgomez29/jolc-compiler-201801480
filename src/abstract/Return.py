
class Return:
    def __init__(self, value, type, isTemp, auxType = ""):
        self.value = value
        self.type = type
        self.auxType = auxType
        self.isTemp = isTemp
        self.trueLbl = ''
        self.falseLbl = ''
            
    def getValue(self):
        return self.value 
        
    def getType(self):
        return self.type