from re import T


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
        self.concatString = False
        self.repeatString = False
        self.parse = False
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
        self.codeIn(f'{result} = {left}{op}{right};\n')

    #================================
    # INSTRUCCIONES
    #================================
    def addPrint(self, type, value):
        if(type == 'f'):
            self.codeIn(f'fmt.Printf("%{type}", {value});\n')
        else:
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

    def printNothing(self):
        self.addPrint("c", 110) # n
        self.addPrint("c", 111) # o
        self.addPrint("c", 116) # t
        self.addPrint("c", 104) # h
        self.addPrint("c", 105) # i
        self.addPrint("c", 110) # n
        self.addPrint("c", 103) # g

    def printMathError(self):
        self.addPrint("c", 77) # M
        self.addPrint("c", 97) # a
        self.addPrint("c", 116) # t
        self.addPrint("c", 104) # h
        self.addPrint("c", 69) # E
        self.addPrint("c", 114) # r
        self.addPrint("c", 114) # r
        self.addPrint("c", 111) # o
        self.addPrint("c", 114) # r

    def printBoundsError(self):
        self.addPrint("c", 66) # B
        self.addPrint("c", 111) # o
        self.addPrint("c", 117) # u
        self.addPrint("c", 110) # n
        self.addPrint("c", 100) # d
        self.addPrint("c", 115) # s
        self.addPrint("c", 69) # E
        self.addPrint("c", 114) # r
        self.addPrint("c", 114) # r
        self.addPrint("c", 111) # o
        self.addPrint("c", 114) # r
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
        self.addIf(tempC, "97", ">", labelEx)
        self.addIf(tempC, "122", "<", labelEx)
        
        self.putLabel(labelEx)

        # para convertirlo a mayuscula
        self.addExp(tempC, tempC, '32', '-') 
       
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
        self.addIf(tempC, "65", ">", labelEx)
        self.addIf(tempC, "90", "<", labelEx)
        
        self.putLabel(labelEx)

        # para convertirlo a mayuscula
        self.addExp(tempC, tempC, '32', '+') 
       
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

    def fConcatString(self):
        if(self.concatString):
            return
        self.concatString = True
        self.inNatives = True
        self.addBeginFunc("concatString")
        #temp new String
        tempNewString = self.addTemp()

        tempP = self.addTemp()
        tempP2 = self.addTemp()
        tempH = self.addTemp()

        # label de salida
        returnLbl = self.newLabel()
        # label de inicio
        initLbl = self.newLabel()

        # Guardando el inicio de mi concatenacion
        self.addExp(tempNewString, 'H', '', '')

        #extrayendo parametros
        #Parametro1
        self.addExp(tempP, 'P', '1', '+')
        self.getStack(tempP, tempP)
        #Parametro1
        self.addExp(tempP2, 'P', '2', '+')
        self.getStack(tempP2, tempP2)

        ## Inicio de recorrido
        self.addGoto(initLbl)
        self.putLabel(initLbl)

        #extrayendo valor del heap
        self.getHeap(tempH,tempP)

        # labels para primer parámetro
        lblTrue1 = self.newLabel() 
        lblFalse1 = self.newLabel() 

        self.addIf(tempH, '-1', '==', lblFalse1)
        self.addGoto(lblTrue1)
        self.putLabel(lblTrue1)
        # concatenando....
        self.setHeap('H',tempH)
        self.nextHeap()
        self.addExp(tempP, tempP, '1', '+')
        self.addGoto(initLbl)

        #continua con el segundo parametro
        self.putLabel(lblFalse1)

        #extrayendo valor del heap
        self.getHeap(tempH,tempP2)
        
        # labels para segundo parámetro
        lblTrue1 = self.newLabel() 
        # lblFalse1 = self.newLabel() 

        self.addIf(tempH, '-1', '==', returnLbl)
        self.addGoto(lblTrue1)
        self.putLabel(lblTrue1)
        # concatenando....
        self.setHeap('H',tempH)
        self.nextHeap()
        self.addExp(tempP2, tempP2, '1', '+')
        self.addGoto(lblFalse1) #regresamos al lbl falso del primer parámetro
        
        # salida function
        self.putLabel(returnLbl)

        # Ingresando el simbolo de terminación de la cadena
        self.setHeap('H', '-1')
        self.nextHeap()

        # valor de retorno
        self.setStack('P', tempNewString)

        self.addEndFunc()
        self.inNatives = False

    #================================

    def fRepeatString(self):
        if(self.repeatString):
            return
        self.repeatString = True
        self.inNatives = True
        self.addBeginFunc("repeatString")
        # temp new String
        tempNewString = self.addTemp()
        # temp counter iteraciones
        tempCounter = self.addTemp()

        # Guardando pos del string a repetir
        tempR = self.addTemp() 
        
        tempP = self.addTemp()
        tempP2 = self.addTemp()
        tempH = self.addTemp()

        # label de salida
        returnLbl = self.newLabel()
        # label de inicio
        initLbl = self.newLabel()

        # Guardando el inicio de mi concatenacion
        self.addExp(tempNewString, 'H', '', '')
        self.addExp(tempCounter, '1', '', '')

        #extrayendo parametros
        #Parametro1
        self.addExp(tempP, 'P', '1', '+')
        self.getStack(tempP, tempP)
        #Parametro1
        self.addExp(tempP2, 'P', '2', '+')
        self.getStack(tempP2, tempP2)

        ## Inicio de recorrido
        # self.addGoto(initLbl)
        self.addExp(tempR, tempP, '', '')
        self.putLabel(initLbl)

        #extrayendo valor del heap
        self.getHeap(tempH,tempP)

        # labels para primer parámetro
        lblTrue1 = self.newLabel() 
        # lblFalse1 = self.newLabel() 

        self.addIf(tempH, '-1', '==', lblTrue1)
        # self.addGoto(lblFalse1)
        # self.putLabel(lblFalse1)

        # Guardando nuevo string
        self.setHeap('H', tempH)
        self.addExp(tempP, tempP, '1', '+')
        self.nextHeap()
        # regresando al inicio
        self.addGoto(initLbl)
        # termino la cadena 
        self.putLabel(lblTrue1)
        self.addIf(tempP2, tempCounter, '==', returnLbl)
        self.addExp(tempCounter, tempCounter, '1', '+')
        # regresandoe el puntero para recorrer nuevamente el string 
        self.addExp(tempP, tempR, '', '')
        self.addGoto(initLbl)
        
        # salida
        self.putLabel(returnLbl)

        # colocando simbolo de finalizacion
        self.setHeap('H', '-1')
        self.nextHeap()

        # valor de retorno
        self.setStack('P', tempNewString)

        self.addEndFunc()
        self.inNatives = False

    def fParse(self):
        if(self.parse):
            return
        self.parse = True
        self.inNatives = True
        self.addBeginFunc("parse")

        tempP = self.addTemp()
        tempH = self.addTemp()
        tempNum = self.addTemp()
        tempBase = self.addTemp()

        self.addExp(tempBase, '10', '', '')

        # label de salida
        returnLbl = self.newLabel()
        # label de inicio
        initLbl = self.newLabel()

        #extrayendo parametros
        #Parametro1
        self.addExp(tempP, 'P', '1', '+')
        self.getStack(tempP, tempP)

        #inicio recorrido
        self.putLabel(initLbl)

        # extrayendo digito
        self.getHeap(tempH, tempP)

        lblDecimal = self.newLabel()
        lblTrue = self.newLabel()

        # es numero
        self.addIf(tempH, '46', '==', lblTrue)
        # self.addIf(tempH, '48', '<', lblTrue)
        # self.addIf(tempH, '57', '>', lblTrue)

        self.addExp(tempH, tempH, '48', '-')
        self.addExp(tempNum, tempNum, tempH, '+')
        self.addExp(tempP, tempP, '1', '+')

        self.addGoto(initLbl)

        self.putLabel(lblTrue)
        self.addExp(tempP, tempP, '1', '+')

        self.putLabel(lblDecimal)

        # extrayendo digito
        self.getHeap(tempH, tempP)

        self.addIf(tempH, '-1', '==', returnLbl)

        self.addExp(tempH, tempH, '48', '-')
        self.addExp(tempH, tempH, tempBase, '/')
        self.addExp(tempNum, tempNum, tempH, '+')
        self.addExp(tempP, tempP, '1', '+')
        self.addExp(tempBase, tempBase, '10', '*')
        
        self.addGoto(lblDecimal)
        # label de salida
        self.putLabel(returnLbl)

        # valor de retorno
        self.setStack('P', tempNum)
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