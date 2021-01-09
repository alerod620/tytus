from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Constraint(Instruccion):
    def __init__(self, nombre, tipo, lista_constraint, strGram=None, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.tipo = tipo
        self.lista_constraint = lista_constraint
    
    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)

    def getCode(self, tabla, controlador, arbol):
        codigo = 'Constraint.Constraint("' + self.nombre + '", '
        codigo += self.tipo.traducir() + ', '
        if self.lista_constraint is None:
            codigo += 'None, "' + self.strGram + '", ' + str(self.linea)
        else:
            codigo += '['
            for c in self.lista_constraint:
                codigo += c.getCode() + ', '
            codigo = codigo[0:-2] + '], "' + self.strGram + '", ' + str(self.linea)
        codigo += ', ' + str(self.columna) + ')'
        return codigo
