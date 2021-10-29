from optimization.C3DInstruction import C3DInstruction

class Label(C3DInstruction):

    def __init__(self, id, line, column):
        super.__init__(self, line, column)
        self.id = id
    
    def getCode(self):
        if self.deleted:
            return ''
        return f'{self.id}:'