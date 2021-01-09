from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class Primitivo(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self, tipo, linea, columna, strGram)
        self.valor = valor

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor

    def traducir(self, tabla, controlador, arbol):
        if(self.tipo.tipo == Tipo_Dato.CHAR or self.tipo.tipo == Tipo_Dato.VARCHAR or self.tipo.tipo == Tipo_Dato.TEXT):
            self.valor = '\''+ str(self.valor) + '\''
        return self
    
    def get_temp(self):
        return self.valor

    def getCode(self):
        codigo  = 'Primitivo.Primitivo('
        if str(self.valor) == 'True' or str(self.valor) == 'False':
            codigo += self.valor + ', '
        else:
            try:
                int(self.valor)
                codigo += str(self.valor) + ', '
            except:
                codigo += '"' + self.valor + '", '
        codigo += self.tipo.getCode() + ', "' + self.strGram.replace('\n', '\\n')
        codigo += '", ' + str(self.linea) + ', ' + str(self.columna) + ')'
        return codigo
