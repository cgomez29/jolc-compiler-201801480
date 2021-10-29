from optimization.C3DInstruction import C3DInstruction

class Return(C3DInstruction):

    def __init__(self, line, column):
        super.__init__(self, line, column)
    
    def getCode(self):
        return 'return;'