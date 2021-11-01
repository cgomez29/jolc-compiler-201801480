from src.graph.GraphValue import GraphValue

class GraphAST:

    def __init__(self, tree): #tree as AST
        self.tree = tree 

    def getGrafo(self):
        graph = "digraph {\n"
        graph += "nodo0[label=\"INICIO\"];\n"

        g = GraphValue(1,graph)
        self.tree.graph(g,"nodo0")
        gph = g.getGraph() + "\n}"
        return gph 