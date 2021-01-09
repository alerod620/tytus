from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class TimeStamp(Instruccion):
    def __init__(self, id, strGram,linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.id = id

    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        todays = datetime.today()
        today = todays.strftime("%Y-%m-%d %H:%M:%S")
        return today

    def getCode(self):
        codigo  = 'TimeStamp.TimeStamp("' + self.id + '", "'
        codigo += self.strGram.replace("\n", "\\n") + '", '
        codigo += str(self.linea) + ', ' + str(self.columna) + ')'
        return codigo
