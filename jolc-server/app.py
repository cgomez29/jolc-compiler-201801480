from flask import Flask, jsonify, request
from flask_cors import CORS
# for interprete 
from src.ast.Generator import Generator
from src.ast.Environment import Environment
from grammar.compiler import grammar


app = Flask(__name__)
CORS(app)

route = "/api"

@app.route('/')
def index():
    return jsonify({"message": "Cristian Gomez - 201801480"})

@app.route(f"{route}/compile", methods=['POST'])
def get_user():
    errors = ""
    symbols = ""
    resulCompile = ""

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

        resulCompile = generator.getCode()


        errors = generator.getExpetions()


        # ## Recorriendo symbols para retornar json
        # for key in tree.getSymbol():
        #     symbols += tree.getSymbol()[key]
        
        # symbols = "[" + symbols[:-1] +"]" #Quitando la ultima ','

    
        ## Preparando el jon de respuesta
        result = {
                    "result": resulCompile,
                    "err": errors, 
                    "symbol": symbols
                }

    except:
        result = {
                "result": resulCompile,
                "err": errors, 
                "symbol": symbols
            }

    return  jsonify(result)

if __name__ == '__main__':
    app.debug = True
    app.run()