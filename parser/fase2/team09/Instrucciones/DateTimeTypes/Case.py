from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 

class Case(Instruccion):
    def __init__(self, id, operacion, id2, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.identificador = id
        self.valor = id2
        self.operacion = operacion

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #el id es para guardarlo en la tabla
        exp = Simbolo(self.identificador,self.operacion,self.valor,self.linea,self.columna)
        ts.setVariable(exp)
        print("imprimir_declaracion")

    def getCode(self):
        codigo  = 'Case.Case(None, None, None, "'
        codigo += self.strGram.replace("\n", "\\n") + '", '
        codigo += str(self.linea) + ', ' + str(self.columna) + ')'
        return codigo
