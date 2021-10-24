from optimization.C3DInstruction import C3DInstruction

class CallFun(C3DInstruction):

    def __init__(self, id, line, column):
        super.__init__(self, line, column)
        self.id = id

    def getCode(self):
        return f'{self.id}();'