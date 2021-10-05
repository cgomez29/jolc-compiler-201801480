from datetime import datetime 

class Exception:
    def __init__(self, type, description, line, column):
        self.type = type 
        self.description = description 
        self.line = line 
        self.column = column 
        now = datetime.now()
        format = now.strftime('%d/%m/%Y %H:%M:%S')
        self.time = format
    
    def getType(self):
        return self.type 
    
    def getDescription(self):
        return self.description

    def getLine(self):
        return self.line

    def getColumn(self):
        return self.column

    def getTime(self):
        return self.time

    def __str__(self) -> str:
        return f"Error : {self.type} {self.description} {self.line} {self.column}  {self.time}"   