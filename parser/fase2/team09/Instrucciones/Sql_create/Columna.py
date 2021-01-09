from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Columna(Instruccion):
    def __init__(self, nombre, tipo, constraint, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.constraint=constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

    def traducir(self, tabla, controlador, arbol):
        codigo = 'CColumna.Columna("' + self.nombre + '", '
        codigo += self.tipo.traducir(tabla, controlador, arbol) + ', '
        if self.constraint is None:
            codigo += 'None, "'
        else:
            codigo += '['
            for c in self.constraint:
                codigo += c.traducir(tabla, controlador, arbol) + ', '
            codigo = codigo[0:-2] + '], "'
        codigo += self.strGram + '", ' + str(self.linea) + ', '
        return codigo + str(self.columna) + ')'
