from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class Primitivo(Instruccion):
    def __init__(self, valor, tipo, strGram, linea, columna):
        Instruccion.__init__(self,tipo,linea,columna, strGram)
        self.valor = valor
       

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla,arbol)
        return self.valor

    def traducir(self, tabla, controlador,arbol):
        if(self.tipo.tipo == Tipo_Dato.CHAR or self.tipo.tipo == Tipo_Dato.VARCHAR or self.tipo.tipo == Tipo_Dato.TEXT):
            self.valor = '\''+ str(self.valor) + '\''
        return self
    
    def get_temp(self):
        return self.valor


'''        
p = Primitivo(1,Tipo(Tipo_Dato.INTEGER),1,2)
print(p.tipo.toString())
res = p.ejecutar(None,None)
print(res)
'''