from optimization.C3DInstruction import C3DInstruction

class Print(C3DInstruction):

    def __init__(self, strTo, exp, line, column):
        C3DInstruction.__init__(self, line, column)
        self.strTo = strTo
        self.exp = exp
    
    def getCode(self):
        return f'fmt.Printf({self.strTo}, int({self.exp.getCode()}));'