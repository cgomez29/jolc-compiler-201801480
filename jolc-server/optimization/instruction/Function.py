from optimization.C3DInstruction import C3DInstruction

class Function(C3DInstruction):

    def __init__(self, instr, id, line, column):
        super.__init__(self, line, column)
        self.instr = instr
        self.id = id
    
    def getCode(self):
        ret = f'func {self.id}(){{\n'
        for ins in self.instr:
            auxText = ins.getCode()
            if(auxText == ''):
                continue
            ret = ret + f'\t{auxText}\n'
        ret = ret + '}'
        return ret