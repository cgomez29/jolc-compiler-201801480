from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type
from src.abstract.Return import Return

class StructGet(Instruction):
    def __init__(self, left, right, line, column):
        super().__init__(line, column)
        self.left = left
        self.right = right
    
    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        
        left = self.left.compile(environment)

        if self.right != None:
            right = self.right.getId()

        temp = None
        type = None
        if(left != None):
            if(left.getType() == Type.STRUCT or left.getType() == Type.MSTRUCT):
                temp = generator.addTemp()
                # tempValue = generator.addTemp()
                # generator.getStack(temp, left.getValue())
                
                struct = environment.getStruct(left.getAuxType())
                counter = 0
                for s in struct.attributes:
                    if (s['id'] == right):
                        type = left.getAttributes()[counter]
                        generator.addExp(left.getValue(), left.getValue(), counter, '+')
                        generator.getHeap(temp, left.getValue())
                        if(type == Type.STRUCT or type == Type.MSTRUCT):
                            right = left.getValues()[counter]
                            ret = Return(temp, type, True)
                            ret.setAuxType(right.getAuxType())
                            ret.setAttributes(right.getAttributes())
                            ret.setValues(right.getValues())
                            return ret
                        break
                    counter += 1

        return Return(temp, type, True)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass