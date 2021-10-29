from optimization.C3DInstruction import C3DInstruction

class Literal(C3DInstruction):

    def __init__(self, value, line, column, constant = False):
        super.__init__(self, line, column)
        self.value = value
        self.constant = constant
    
    def getCode(self):
        return str(self.value)