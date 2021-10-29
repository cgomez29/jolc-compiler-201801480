from optimization.C3DInstruction import C3DInstruction

class If(C3DInstruction):
    def __init__(self, condition, label, line, column):
        super().__init__(line, column)
        self.label = label
        self.condition = condition

    def getCode(self):
        return f'if ({self.condition.getCode()}) {{ goto {self.label}; }}'