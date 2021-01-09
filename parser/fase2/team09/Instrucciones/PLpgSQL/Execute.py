from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from Instrucciones.C3D.temporal import temporal

class Execute(Instruccion):
    def __init__(self, nombre, parametros, strGram, linea, columna):
        self.nombre = nombre
        self.parametros = parametros

    def ejecutar(self, tabla, arbol):
        print("Execute", self.nombre, self.parametros)

    def traducir(self, tabla, controlador, arbol):
        codigo = ''
        funcion = tabla.getFuncion(self.nombre)
        count_parametro=1
        if(funcion != None):
            #verificar lista parametros
            #print('PARAMETROS EXECUTE -> ' +str(self.parametros))
            for para in self.parametros:
                controlador.cont_temp = controlador.cont_temp + 1
                temp = temporal(controlador.cont_temp,None)
                #traducir parametros 
                temp_para = para.traducir(tabla, controlador, arbol)
                codigo += '    '+str(temp.get_temp()) + ' = P +'+str(count_parametro)+'\n'
                codigo += '    stack['+str(temp.get_temp())+'] = '+str(temp_para.get_temp()) +'\n'
                count_parametro = count_parametro +1

            peso_funcion = len(funcion.campos) + len(funcion.ids) + 1

            codigo += '    P = P + '+str(controlador.peso_fun_actual)+'\n'
            codigo += '    '+str(self.nombre)+'()\n'

            #valor de retorno
            controlador.cont_temp = controlador.cont_temp + 1
            temp_retorno = temporal(controlador.cont_temp,None)
            codigo += '    '+str(temp_retorno.get_temp())+' = stack[P]\n'
            codigo += '    P = P - '+str(controlador.peso_fun_actual)+'\n'
            controlador.append_3d_ejecutar(codigo)
            return temp_retorno

        else:
            error = Excepcion('40534',"Semántico","La funcion "+str(self.nombre)+" No existe",0,0)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 