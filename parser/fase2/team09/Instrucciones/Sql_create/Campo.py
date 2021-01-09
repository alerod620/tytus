from Instrucciones.TablaSimbolos.Instruccion import Instruccion

class Campo(Instruccion):
    def __init__(self, nombre, lower, orden, null, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.lower = lower
        self.orden = orden
        self.null = null
        self.existe = False
        self.dupli = False
        self.restricciones = ";"

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)
        self.restricciones = ""
        if self.lower:
            self.restricciones = ".lower()"
        else:
            self.lower = None
        self.orden = self.orden.ejecutar(tabla, arbol)
        if self.orden is not None:
            if self.lower is not None:
                self.restricciones = self.restricciones + ", "
            else:
                self.restricciones = self.restricciones + " "
            self.restricciones = self.restricciones + self.orden
        self.null = self.null.ejecutar(tabla, arbol)
        if self.null is not None:
            if self.orden is not None:
                self.restricciones = self.restricciones + " "
            elif self.lower is not None:
                self.restricciones = self.restricciones + ", "
            else:
                self.restricciones = self.restricciones + " "
            self.restricciones = self.restricciones + self.null
        self.restricciones = self.restricciones + "; "

    def getCode(self):
        codigo = 'Campo.Campo("' + self.nombre + '", ' + str(self.lower) + ', '
        codigo += self.orden.getCode() + ', ' + self.null.getCode() + ', "'
        codigo += self.strGram + '", ' + str(self.linea) + ', '
        return codigo + str(self.columna) + ')'
