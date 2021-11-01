from abc import ABC, abstractmethod

class Instruction(ABC):
    def __init__(self,line, column):
        self.line = line 
        self.column = column

    @abstractmethod
    def compile(self, environment):
        pass

    @abstractmethod
    def graph(self, g, father):
        pass

    @abstractmethod
    def getNameSon(self):
        pass