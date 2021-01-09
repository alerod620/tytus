from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Columna(Instruccion):
    def __init__(self, nombre, tipo, constraint, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.constraint=constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

    def getCode(self):
        codigo = 'CColumna.Columna("' + self.nombre + '", '
        codigo += self.tipo.getCode() + ', '
        if self.constraint is None:
            codigo += 'None, "' + self.strGram + '", ' + str(self.linea)
        else:
            codigo += '['
            for c in self.constraint:
                codigo += c.getCode() + ', '
            codigo = codigo[0:-2] + '], "' + self.strGram + '", ' + str(self.linea)
        codigo += ', ' + str(self.columna) + ')'
        return codigo
