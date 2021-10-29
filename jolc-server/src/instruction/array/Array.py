from src.ast.Generator import Generator
from src.abstract.Instruction import Instruction
from src.ast.Type import Type
from src.abstract.Return import Return

class Array(Instruction):
    def __init__(self, expressions, line, column):
        super().__init__(line, column)
        self.expressions = expressions

    def compile(self, environment):
        auxG = Generator()
        generator = auxG.getInstance()
        # generator.addComment("----------------INIT ARRAY -----------------------")
        tempH = generator.addTemp() # puntero heap
        tempH2 = generator.addTemp() # posiciones del arreglo
        length = len(self.expressions)
        generator.addExp(tempH, 'H', '', '') # guardando la pos del array 
        generator.addExp(tempH2, tempH, '', '')  # temp para saber las posiciones correspondientes a cada valor
        generator.addExp('H', 'H', length + 1, '+') # reservando posiciones del heap para cada valor a recorrer y sumamos por que en la pos 1 va el tamaño del arreglo
        
        # Guardando el tamaño del arreglo
        generator.setHeap(tempH2, length) # guardando valor
        generator.addExp(tempH2, tempH2, '1', '+') # cambio de lugar

        auxTypes = []
        auxValues = [] # guarda los atributos de los arreglos anidados
        counter = 1
        for e in self.expressions:
            value = e.compile(environment) # compilando valor
            
            generator.setHeap(tempH2, value.getValue()) # guardando valor
            if (counter != length):
                generator.addExp(tempH2, tempH2, '1', '+') # cambio de lugar

            counter += 1
            auxTypes.append(value.getType())
            auxValues.append(value)        

        ret = Return(tempH, Type.ARRAY, True)
        ret.setAttributes(auxTypes)
        ret.setValues(auxValues)
        # generator.addComment("----------------FIN ARRAY -----------------------")
        return ret

    def graph(self, g, father):
        pass

    def getNameSon(self):
        pass