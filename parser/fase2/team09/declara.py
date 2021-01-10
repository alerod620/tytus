import ast_op as ast_op
import reglas as r

class Declara():
    def __init__(self, metodo, instrucciones):
        self.metodo = metodo
        self.instrucciones = instrucciones

    def optimizacion(self):
        r.Reglas.optimizado = r.Reglas.optimizado + str(self.metodo) + '\n'
        ast_op.ast_op(self.instrucciones).optimizacion()