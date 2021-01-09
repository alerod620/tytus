from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.C3D.temporal import temporal

class Asignacion(Instruccion):
    def __init__(self, nombre, expresion, query, strGram, linea, columna):
        Instruccion.__init__(self, None, linea, columna, strGram)
        self.nombre = nombre
        self.expresion = expresion
        self.query = query

    def ejecutar(self, tabla, arbol):
        super().ejecutar(tabla, arbol)

    def traducir(self, tabla, controlador, arbol):
        #self.ejecutar(tabla, arbol)
        codigo = ''
        #validar que la variable exista 
        variable = tabla.getVariable(self.nombre)

        if( variable == None):
            error = Excepcion('40514',"Semántico","La variable No existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 
        else:

            exp = self.expresion.traducir(tabla, controlador, arbol)
           
            if(variable.tipo == exp.tipo.tipo):
                controlador.cont_temp = controlador.cont_temp + 1
                temp = temporal(controlador.cont_temp,None)

                codigo += '    #asignacion de variable \n'
                codigo += '    '+str(temp.get_temp()) + ' = P + '+str(variable.valor)+'\n'
                codigo += '    stack['+str(temp.get_temp())+'] = '+ str(exp.get_temp())+'\n'

                controlador.append_3d(codigo)
                return temp
            else:
                print('tipo variable '+ str(variable.tipo))
                print('tipo exp '+ str(exp.tipo))
                error = Excepcion('40524',"Semántico","Error de tipos",self.linea,self.columna)
                arbol.excepciones.append(error)
                arbol.consola.append(error.toString())
                return error 


