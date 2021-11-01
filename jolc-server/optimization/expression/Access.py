from optimization.C3DInstruction import C3DInstruction

class Access(C3DInstruction):

    def __init__(self, StackHeap, position, line, column):
        C3DInstruction.__init__(self, line, column)
        self.StackHeap = StackHeap
        self.position = position
    
    def getCode(self):
        return f'{self.StackHeap}[int({self.position.getCode()})]'