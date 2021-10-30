from src.ast.Environment import Environment
from grammar.compiler import grammar
from src.ast.Generator import Generator

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

print(generator.getCode())