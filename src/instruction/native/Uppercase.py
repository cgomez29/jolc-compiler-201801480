from src.abstract.Instruction import Instruction

class Uppercase(Instruction):
    def __init__(self, id, parameters, instructions, line, column):
        super().__init__(line, column)
        self.id = id 
        self.parameters = parameters
        self.instructions = instructions 

    def compile(self, environment):
        print("SIIIIIU UPPERCASE")
        pass

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass

    