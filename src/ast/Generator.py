class Generator:
    generator = None
    def __init__(self):
        # Contadores
        self.countTemp = 0
        self.countLabel = 0
        self.count_exception = 0
        # Code
        self.code = '' 
        self.funcs = ''
        self.natives = ''
        self.inFunc = False
        self.inNatives = False
        # Lista de Temporales
        self.temps = []
        
        # Lista de funciones nativas
        self.printString = False
        self.uppercase = False
        self.lowercase = False

        self.exceptions = []

    def getInstance(self):
        if Generator.generator == None:
            Generator.generator = Generator()
        return Generator.generator
        
    def cleanAll(self):
         # Contadores
        self.countTemp = 0
        self.countLabel = 0
        # Code
        self.code = ''
        self.funcs = ''
        self.natives = ''
        self.inFunc = False
        self.inNatives = False
        # Lista de Temporales
        self.temps = []
        # Lista de funciones nativas
        self.printString = False
        Generator.generator = Generator()
    
    #================================
    # CODE
    #================================
    def getHeader(self):
        ret = '/*----HEADER----*/\npackage main;\n\nimport (\n\t"fmt"\n)\n\n'
        if len(self.temps) > 0:
            ret += 'var '
            for temp in range(len(self.temps)):
                ret += self.temps[temp]
                if temp != (len(self.temps) - 1):
                    ret += ", "
            ret += " float64;\n"
        ret += "var P, H float64;\nvar stack [29101998]float64;\nvar heap [29101998]float64;\n\n"
        return ret


    def getCode(self):
        return f'{self.getHeader()}{self.natives}\n{self.funcs}\nfunc main(){{\n{self.code}\n\treturn;\n}}'

    def codeIn(self, code, tab="\t"):
        if(self.inNatives):
            if(self.natives == ''):
                self.natives = self.natives + '/*-----NATIVES-----*/\n'
            self.natives = self.natives + tab + code
        elif(self.inFunc):
            if(self.funcs == ''):
                self.funcs = self.funcs + '/*-----FUNCS-----*/\n'
            self.funcs = self.funcs + tab +  code
        else:
            self.code += '\t' +  code

    def addComment(self, comment):
        self.codeIn(f'/* {comment} */ \n')

    def addSpace(self):
        self.codeIn("\n")

    #================================
    # Manejo de Temporales
    #================================
    def addTemp(self):
        temp = f't{self.countTemp}'
        self.countTemp += 1
        self.temps.append(temp)
        return temp
    #================================
    # EXPRESIONES
    #================================
    def addExp(self, result, left, right, op):
        self.codeIn(f'{result} = {left} {op} {right};\n')

    #================================
    # INSTRUCCIONES
    #================================
    def addPrint(self, type, value):
        self.codeIn(f'fmt.Printf("%{type}", int({value}));\n')

    def printTrue(self):
        self.addPrint("c", 116)
        self.addPrint("c", 114)
        self.addPrint("c", 117)
        self.addPrint("c", 101)

    def printFalse(self):
        self.addPrint("c", 102)
        self.addPrint("c", 97)
        self.addPrint("c", 108)
        self.addPrint("c", 115)
        self.addPrint("c", 101)

    #================================
    # New line for comentary
    #================================
    def newLine(self):
        self.addPrint("c", 10)

    #================================
    # Manejo de LABEL
    #================================
    def newLabel(self):
        label = f'L{self.countLabel}'
        self.countLabel += 1
        return label
    
    def putLabel(self, label):
        self.codeIn(f'{label}:\n')

    #================================
    # GOTO
    #================================
    def addGoto(self, label):
        self.codeIn(f'goto {label};\n')

    #================================
    # FUNCTION
    #================================
    def addBeginFunc(self, id):
        if(not self.inNatives):
            self.inFunc = True
        self.codeIn(f'func {id}(){{\n', '')
    
    def addEndFunc(self):
        self.codeIn('return;\n}\n')
        if(not self.inNatives):
            self.inFunc = False

    #================================
    # IF
    #================================
    def addIf(self, left, rigth, op, label):
        self.codeIn(f'if {left} {op} {rigth} {{goto {label};}}\n')

    #================================
    # STACK
    #================================
    def setStack(self, pos, value):
        self.codeIn(f'stack[int({pos})] = {value};\n')
    
    def getStack(self, place, pos):
        self.codeIn(f'{place} = stack[int({pos})];\n')

    #================================
    # ENVS
    #================================
    def newEnv(self, size):
        self.codeIn(f'P = P + {size};\n')

    def callFun(self, id):
        self.codeIn(f'{id}();\n')

    def retEnv(self, size):
        self.codeIn(f'P = P - {size};\n')


    #================================
    # HEAP
    #================================
    def setHeap(self, pos, value):
        self.codeIn(f'heap[int({pos})] = {value};\n')

    def getHeap(self, place, pos):
        self.codeIn(f'{place} = heap[int({pos})];\n')

    def nextHeap(self):
        self.codeIn('H = H + 1;\n')

    #================================
    # NATIVES
    #================================
    def fPrintString(self):
        if(self.printString):
            return
        self.printString = True
        self.inNatives = True

        self.addBeginFunc('printString')
        # Label para salir de la funcion
        returnLbl = self.newLabel()
        # Label para la comparacion para buscar fin de cadena
        compareLbl = self.newLabel()

        # Temporal puntero a Stack
        tempP = self.addTemp()

        # Temporal puntero a Heap
        tempH = self.addTemp()

        self.addExp(tempP, 'P', '1', '+')

        self.getStack(tempH, tempP)

        # Temporal para comparar
        tempC = self.addTemp()

        self.putLabel(compareLbl)

        self.getHeap(tempC, tempH)

        self.addIf(tempC, '-1', '==', returnLbl)

        self.addPrint('c', tempC)

        self.addExp(tempH, tempH, '1', '+')

        self.addGoto(compareLbl)

        self.putLabel(returnLbl)
        self.addEndFunc()
        self.inNatives = False
    
    #================================

    def fUpperCase(self):
        if(self.uppercase):
            return
        self.uppercase = True
        self.inNatives = True

        self.addBeginFunc("uppercase")
        
        tempNewString = self.addTemp()
        self.addExp(tempNewString, 'H', '', '')

        # escape label
        returnLbl = self.newLabel() 

        # puntero stack
        tempP = self.addTemp()

        # puntero heap
        tempH = self.addTemp()

        self.addExp(tempP, 'P', '1', '+')
        self.getStack(tempH, tempP)

        #label inicio
        initLbl = self.newLabel()
        self.addGoto(initLbl)
        self.putLabel(initLbl)

        #temporal para extraer caracter´
        tempC = self.addTemp()

        self.getHeap(tempC, tempH)

        #Label para transformacion
        labelEx = self.newLabel()

        # Si temp = -1 llegamos al final de la cadena
        self.addIf(tempC, "-1", "==", returnLbl)
        self.addIf(tempC, "97", "<", labelEx)
        self.addIf(tempC, "122", ">", labelEx)
        

        # para convertirlo a mayuscula
        self.addExp(tempC, tempC, '32', '-') 

        self.putLabel(labelEx)
       
        # Guardamos en una posicion nueva del heap
        self.setHeap('H', tempC)
        # Aumentamos el heap
        self.nextHeap()

        # next puntero heap
        self.addExp(tempH, tempH, '1', '+')
        # regresamos al lbl de inicio
        self.addGoto(initLbl) 
        self.putLabel(returnLbl)

        # Guardamos el -1 indicando el fin de la cadena
        self.setHeap('H', '-1')
        # Aumentamos el heap
        self.nextHeap()

        #Guardamos el retono
        self.setStack('P', tempNewString)
        
        self.addEndFunc()
        self.inNatives = False

    #================================

    def fLowerCase(self):
        if(self.lowercase):
            return
        self.lowercase = True
        self.inNatives = True

        self.addBeginFunc("lowercase")
        
        tempNewString = self.addTemp()
        self.addExp(tempNewString, 'H', '', '')

        # escape label
        returnLbl = self.newLabel() 

        # puntero stack
        tempP = self.addTemp()

        # puntero heap
        tempH = self.addTemp()

        self.addExp(tempP, 'P', '1', '+')
        self.getStack(tempH, tempP)

        #label inicio
        initLbl = self.newLabel()
        self.addGoto(initLbl)
        self.putLabel(initLbl)

        #temporal para extraer caracter´
        tempC = self.addTemp()

        self.getHeap(tempC, tempH)

        #Label para transformacion
        labelEx = self.newLabel()

        # Si temp = -1 llegamos al final de la cadena
        self.addIf(tempC, "-1", "==", returnLbl)
        self.addIf(tempC, "65", "<", labelEx)
        self.addIf(tempC, "90", ">", labelEx)
        
        # para convertirlo a mayuscula
        self.addExp(tempC, tempC, '32', '+') 
       
        self.putLabel(labelEx)

        # Guardamos en una posicion nueva del heap
        self.setHeap('H', tempC)
        # Aumentamos el heap
        self.nextHeap()

        # next puntero heap
        self.addExp(tempH, tempH, '1', '+')
        # regresamos al lbl de inicio
        self.addGoto(initLbl) 
        self.putLabel(returnLbl)

        # Guardamos el -1 indicando el fin de la cadena
        self.setHeap('H', '-1')
        # Aumentamos el heap
        self.nextHeap()

        #Guardamos el retono
        self.setStack('P', tempNewString)
        
        self.addEndFunc()
        self.inNatives = False

    #================================
    # EXCEPTION
    #================================

    def setException(self, value): 
        self.count_exception += 1
        data = f"\"column1\": \"{self.count_exception}\", \"column2\": \"{value.getDescription()}\", \"column3\": \"{value.getLine()}\", \"column4\": \"{value.getColumn()}\", \"column5\": \"{value.getTime()}\""
        data = "{" + data + "},"
        self.exceptions.append(data)