from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Simbolo import Simbolo 

class DatePart(Instruccion):
    def __init__(self, id, id2, strGram, linea, columna):
        Instruccion.__init__(self,None,linea,columna,strGram)
        self.identificador = id
        self.valor = id2
        
    def ejecutar(self, ts, arbol):
        #super().ejecutar(ts,arbol)
        #el id es para guardarlo en la tabla
        #tamaño de cadena
       
        tam = len(self.valor)
        parser = self.valor.split()
        
        segundo = 0
        minuto = 0
        hora = 0
        for x in range(0,len(parser)):
            print(parser[x])
            if(parser[x]=="seconds"):
                segundo = parser[x-1]
            elif(parser[x]=="minutes"):
                minuto = parser[x-1]
            elif(parser[x]=="hours"):
                hora = parser[x-1]
                

        if(self.identificador == "seconds"):
            #print("segundo")
            #print(str(segundo))
            return segundo
        elif(self.identificador == "minutes"):
            #print("minuto")
            #print(str(minuto))
            return minuto
        elif(self.identificador == "hour"):
            #print("hora")
            #print(str(hora))
            return hora

    def getCode(self):
        codigo  = 'DatePart.DatePart("' + self.identificador + '", "' + self.valor
        codigo += '", "' + self.strGram.replace("\n", "\\n") + '", '
        codigo += str(self.linea) + ', ' + str(self.columna) + ')'
        return codigo
