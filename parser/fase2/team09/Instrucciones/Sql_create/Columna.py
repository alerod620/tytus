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
            codigo += 'None, '
        else:
            codigo += self.constraint.traducir(tabla, controlador, arbol) + ', "'
        codigo += self.strGram + '", ' + str(self.linea) + ', ' + str(self.columna) + ').ejecutar(tabla, arbol)\n'
        return codigo
