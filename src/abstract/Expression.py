from abc import ABC, abstractmethod

class Expression(ABC):
    def __init__(self,line, column):
        self.line = line 
        self.column = column
        self.trueLbl = ''
        self.falseLbl = ''

    @abstractmethod
    def compile(self, environment):
        pass

    @abstractmethod
    def graph(self, g, father):
        pass

    @abstractmethod
    def getNameSon(self):
        pass