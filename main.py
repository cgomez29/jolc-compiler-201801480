from src.ast.Environment import Environment
from grammar import grammar
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


print(generator.getCode())