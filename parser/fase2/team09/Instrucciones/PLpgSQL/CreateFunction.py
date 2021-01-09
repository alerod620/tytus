from Instrucciones.TablaSimbolos.Instruccion import Instruccion
from Instrucciones.Excepcion import Excepcion
from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo
from Instrucciones.TablaSimbolos.Simbolo import Simbolo
from Instrucciones.TablaSimbolos.Funcion import Funcion
from Instrucciones.TablaSimbolos.Tabla import Tabla
from Instrucciones.C3D.temporal import temporal
from Instrucciones.PLpgSQL.sentencia_return import sentencia_return

class CreateFunction(Instruccion):
    def __init__(self, nombre, tipo, parametros, declaraciones, instrucciones, strGram, linea, columna):
        Instruccion.__init__(self, tipo, linea, columna, strGram)
        self.nombre = nombre
        self.parametros = parametros
        self.declaraciones = declaraciones
        self.instrucciones = instrucciones
        self.tipo = tipo
        self.linea = linea
        self.columna = columna 

    def ejecutar(self, tabla, arbol):
        #super().ejecutar(tabla,arbol)
        #Aqui vamos a guardar la funcion
        tabla.setFuncion(self)

    def traducir(self, tabla, controlador, arbol):
        codigo =''

        #validar si la funcion existe en la ts
        funcion = tabla.getFuncion(self.nombre)
        if(funcion == None):
            #tabla de simbolos del entorno de la funcion
            tabla_local = Tabla(tabla)

            etiqueta_salida = controlador.get_etiqueta()
            aux = controlador.etiqueta_salida
            controlador.etiqueta_salida = etiqueta_salida

            codigo += '\n@with_goto \ndef '+str(self.nombre)+'(): \n'
            controlador.append_3d(codigo)
            codigo = ''
            controlador.set_stack(0)
            peso_funcion = len(self.parametros) + len(self.declaraciones)

            #se suma 1 por el return
            peso_funcion = peso_funcion + 1
            
            aux_peso = controlador.peso_fun_actual
            controlador.peso_fun_actual = peso_funcion

            #guardando en la ts los parametros 
            for parametro in self.parametros:
                nuevo_simbolo = Simbolo(parametro.nombre,parametro.tipo,controlador.get_stack(),parametro.linea, parametro.columna)
                print('pos_stack -> ' + str(nuevo_simbolo))
                tabla_local.setVariable(nuevo_simbolo)
            
            #generar el codigo de las declaraciones 
            for declaracion in self.declaraciones:
                declaracion.traducir(tabla_local, controlador, arbol)
            #generando codigo de las sentencias
            for instruccion in self.instrucciones:
                instruccion.traducir(tabla_local, controlador, arbol)
            
            codigo += '    label. '+ str(etiqueta_salida)
            
            controlador.append_3d(codigo)
            controlador.etiqueta_salida = aux
            controlador.peso_fun_actual = aux_peso
            funcion = Funcion(self.nombre,self.tipo,self.parametros,self.declaraciones,self.linea, self.columna)
            tabla.setFuncion(funcion)

        else:
            error = Excepcion('40514',"Semántico","La funcion "+str(self.nombre)+" No existe",self.linea,self.columna)
            arbol.excepciones.append(error)
            arbol.consola.append(error.toString())
            return error 



'''
instruccion = CreateFunction("hola mundo",None, 1,2)

instruccion.ejecutar(None,None)
'''