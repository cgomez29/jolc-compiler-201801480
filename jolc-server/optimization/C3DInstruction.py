from abc import ABC, abstractmethod

class C3DInstruction(ABC):
    
    def __init__(self, line, column):
        self.line = line
        self.column = column
        self.haveInt = False
        self.deleted = False
    
    @abstractmethod
    def getCode(self):
        pass