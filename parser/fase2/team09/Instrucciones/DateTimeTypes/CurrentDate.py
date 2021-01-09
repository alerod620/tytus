from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 
from datetime import datetime 

class CurrentDate(Instruccion):
    def __init__(self, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        
    def ejecutar(self, ts, arbol):
        super().ejecutar(ts,arbol)
        #año-mes-dia
        todays_date = datetime.today()
        date = todays_date.strftime("%Y-%m-%d")
        return date

    def getCode(self):
        codigo  = 'CurrentDate.CurrentDate("' + self.strGram.replace("\n", "\\n")
        codigo += '", ' + str(self.linea) + ', ' + str(self.columna) + ')'
        return codigo
