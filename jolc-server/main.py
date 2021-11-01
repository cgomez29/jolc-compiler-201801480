from src.ast.Environment import Environment
from grammar.compiler import grammar
from src.ast.Generator import Generator
from grammar.optimization import optimization 

f = open("./input.jl", "r", encoding="utf-8")
input = f.read()

auxG = Generator()
auxG.cleanAll()
generator = auxG.getInstance()
result = grammar.parse(input) # as AST


env = Environment(None)
env.setName("global")
result.compile(env)

## Recorriendo symbols para retornar json
symbols = ''
for key in result.getSymbols():
    symbols += result.getSymbols()[key]

symbols = "[" + symbols[:-1] +"]" #Quitando la ultima ','

# imprime el codigo generado
output = generator.getCode()
# print(output)

prueba = '''
    /*----HEADER----*/
package main;

import (
	"fmt"
);

var t0 float64;
var P, H float64;
var stack [29101998]float64;
var heap [29101998]float64;



func main(){
	t0 = 5+0;
	t0 = t0+0;
	t0 = t0-0;
	t0 = 5/1;
	t0 = t0/1;
	
	if 5 > 5 {goto L0;}
	goto L1;
	
	L0:
	fmt.Printf("%c", int(116));
	fmt.Printf("%c", int(114));
	fmt.Printf("%c", int(117));
	fmt.Printf("%c", int(101));
	goto L2;
	L1:
	fmt.Printf("%c", int(102));
	fmt.Printf("%c", int(97));
	fmt.Printf("%c", int(108));
	fmt.Printf("%c", int(115));
	fmt.Printf("%c", int(101));
	L2:
	fmt.Printf("%c", int(10));
}

'''


instrucciones = optimization.parse(prueba)
instrucciones.mirilla()

print(instrucciones.getCode())