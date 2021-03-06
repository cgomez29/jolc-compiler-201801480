import re
from flask import Flask, jsonify, request
from flask_cors import CORS
# for interprete 
from src.ast.Generator import Generator
from src.ast.Environment import Environment
from grammar.compiler import grammar
from grammar.optimization import optimization 


app = Flask(__name__)
CORS(app)

route = "/api"

@app.route('/')
def index():
    return jsonify({"message": "Cristian Gomez - 201801480"})

@app.route(f"{route}/compile", methods=['POST'])
def get_compile():
    errors = ""
    symbols = ""
    resultCompile = ""

    try:
        ## Recuperando code recibido
        input = request.json['input']

        auxG = Generator()
        auxG.cleanAll()
        generator = auxG.getInstance()

        result = grammar.parse(input) # as AST
        

        env = Environment(None)
        env.setName("global")
        result.compile(env)

        #obteniendo tabla de simbolos
        result.getSymbols()

        resultCompile = generator.getCode()

        errors = generator.getExpetions()


        for key in result.getSymbols():
            symbols += result.getSymbols()[key]

        symbols = "[" + symbols[:-1] +"]" #Quitando la ultima ','

        ## Preparando el jon de respuesta
        result = {
                    "result": resultCompile,
                    "err": errors, 
                    "symbol": symbols
                }

    except:
        result = {
                "result": resultCompile,
                "err": errors, 
                "symbol": symbols
            }

    return  jsonify(result)


@app.route(f"{route}/mirilla", methods=['POST'])
def get_mirilla():
    errors = '[]'
    symbols = ''
    result = ''

    try:
        ## Recuperando code recibido
        input = request.json['input']
        print(input)

        instrucciones = optimization.parse(input)

        instrucciones.mirilla()

        # result = instrucciones.getCode()
        result = input


        result = {
                    "result": result,
                    "err": errors, 
                    "symbol": symbols
                }

    except:
        result = {
                "result": result,
                "err": errors, 
                "symbol": symbols
            }

    return  jsonify(result)

if __name__ == '__main__':
    app.debug = True
    app.run()