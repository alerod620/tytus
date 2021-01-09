from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.C3D.temporal import temporal

class Variable(Instruccion):
    def __init__(self, nombre, const, tipo, nulo, valor, alias, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.const = const
        self.tipo = tipo
        self.nulo = nulo
        self.valor = valor
        self.alias = alias

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)


    def traducir(self, tabla, controlador,arbol): 
       # print('************** TRADUCIR VARIABLE *****************')
        #print('print tipo-> '+ str(self.tipo.tipo))
        #print('print tipo-> '+ str(self.tipo))
        #solo se puede declarar 
        codigo =''

        controlador.cont_temp = controlador.cont_temp + 1
        temp_resultado = temporal(controlador.cont_temp,None)

        if(self.tipo.tipo == Tipo_Dato.DECIMAL or self.tipo.tipo == Tipo_Dato.NUMERIC or self.tipo.tipo == Tipo_Dato.INTEGER 
            or self.tipo.tipo == Tipo_Dato.BOOLEAN):
            posicion_stack = str(controlador.get_stack())

            n_simbolo = Simbolo(self.nombre, self.tipo.tipo,posicion_stack,self.linea,self.columna)
            agregar = tabla.setVariable(n_simbolo)
            if(agregar != 0):
                codigo += '     # declaracion de variable \n'
                codigo += '    '+ str(temp_resultado.get_temp()) + ' = P + ' + posicion_stack +'\n'
                codigo += '    stack['+ str(temp_resultado.get_temp()) + '] = 0 \n'
                controlador.append_3d(codigo)
                return temp_resultado     
            else:
                error = Excepcion('40504',"Semántico","La variable ya existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error 

        elif(self.tipo.tipo == Tipo_Dato.CHAR or self.tipo.tipo == Tipo_Dato.TEXT 
            or self.tipo.tipo == Tipo_Dato.CHARACTER or self.tipo.tipo == Tipo_Dato.VARCHAR):
            posicion_stack = str(controlador.get_stack())

            n_simbolo = Simbolo(self.nombre, self.tipo.tipo,posicion_stack,self.linea,self.columna)
            agregar = tabla.setVariable(n_simbolo)
            if(agregar != 0):
                codigo += '     # declaracion de variable \n'
                codigo += '    '+ str(temp_resultado.get_temp()) + ' = P +' + posicion_stack +'\n'
                codigo += '     stack['+ str(temp_resultado.get_temp()) + '] = \'\' \n'
                controlador.append_3d(codigo)
                return  temp_resultado
            else:
                error = Excepcion('40504',"Semántico","La variable ya existe",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error 

        else:
            controlador.append_3d('entro al else :((')

