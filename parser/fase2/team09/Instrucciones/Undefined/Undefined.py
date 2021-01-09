from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Undefined(Instruccion):
    def __init__(self, tipo, valor, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.tipo = tipo
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        if self.valor != None:
            self.valor = self.tipo + self.valor
        return self.valor

    def getCode(self):
        codigo = 'Undefined.Undefined("' + self.tipo + '", '
        if self.valor is None:
            codigo += 'None, "' + self.strGram + '", '
        else:
            codigo += '"' + self.valor + '", "' + self.strGram + '", '
        codigo += str(self.linea) + ', ' + str(self.columna) + ')'
        return codigo
