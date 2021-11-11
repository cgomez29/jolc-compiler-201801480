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
        generator.addComment("BEGIN STRUCT ACCESS")
        
        left = self.left.compile(environment)

        if self.right != None:
            right = self.right.getId()

        temp = generator.addTemp()
        type = None
        if(left != None):
            if(left.getType() == Type.STRUCT or left.getType() == Type.MSTRUCT):
                struct = environment.getStruct(left.getAuxType())
                counter = 0
                for s in struct.attributes:
                    if (s['id'] == right):
                        type = s['tipo'] 
                        if isinstance(type, str):
                            right = environment.getStruct(type)
                            type = right.getType()

                        if(type == Type.STRUCT or type == Type.MSTRUCT):
                            generator.addExp(temp, left.getValue(), counter, '+')
                            generator.getHeap(temp, temp)
                            # generator.getHeap(temp, temp)

                            ret = Return(temp, type, True)
                            ret.setAuxType(right.getAuxType())
                            ret.setAttributes(right.getAttributes())
                            ret.setValues(right.getValues())
                            return ret
                        else: 
                            generator.addExp(temp, left.getValue(), counter, '+')
                            generator.getHeap(temp, temp)
                            break
                
                    counter += 1


        generator.addComment("END STRUCT ACCESS")
        return Return(temp, type, True)

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass