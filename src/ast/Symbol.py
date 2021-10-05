
class Symbol:
    def __init__(self, id, type, position = 0, globalVar = None, inHeap = None):
        self.id = id 
        # self.value = value 
        self.type = type 
        self.isTemp = None
        self.trueLbl = ''
        self.falseLbl = ''
        self.isGlobal = globalVar
        self.inHeap = inHeap
        self.pos = position

    def getId(self):
        return self.id
            
    # def getValue(self):
    #     return self.value 
        
    def getType(self):
        return self.type

    def getLine(self):
        return self.line 

    def getColumn(self):
        return self.column 

    def getIsTemp(self):
        return self.isTemp

    def setIsTemp(self, isTemp):
        self.isTemp = isTemp

