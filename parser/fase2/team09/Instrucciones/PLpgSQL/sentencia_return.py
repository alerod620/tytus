from Instrucciones.C3D.temporal import temporal

class sentencia_return():
    def __init__(self,expre):
        self.expre = expre

    def traducir(self, tabla, controlador, arbol):
        codigo = ''
        #generar codigo de la expresion
        print('---------------------------> '+str(self.expre))
        temp_exp = self.expre.traducir(tabla, controlador, arbol)

        codigo += '    stack[P] =' +str(temp_exp.get_temp())+'\n'
        codigo += '    goto .'+str(controlador.etiqueta_salida)+'\n'
        controlador.append_3d(codigo)
        return temp_exp