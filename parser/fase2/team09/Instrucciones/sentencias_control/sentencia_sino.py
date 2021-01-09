from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class sentencia_sino():

    def __init__(self, condicion, lista_inst):
        self.condicion = condicion
        self.lista_inst = lista_inst
        self.cond1_ls = ''
        
    def traducir(self, tabla, controlador, arbol):
        codigo = ''
        #print('entro al traducir de la clase sino')

        if(self.condicion != None):
            if(self.condicion.tipo.tipo == Tipo_Dato.BOOLEAN):
                #etiquetas para el c3d
                cond1_lv = controlador.get_etiqueta()
                cond1_lf = controlador.get_etiqueta()

                #declaraciones

                tmp_cond = self.condicion.traducir(tabla, controlador, arbol)
                codigo = '    #sentencia if | else if  \n'
                codigo += '    if('+str(tmp_cond.get_temp()) + '== 1): \n'
                codigo += '        goto .'+ cond1_lv +'\n'
                codigo += '    goto .'+ cond1_lf +' \n'
                codigo += '    label .'+cond1_lv + '\n'
                controlador.append_3d(codigo)


                for i in self.lista_inst: 
                    i.traducir(tabla, controlador, arbol)

                
                codigo = '    goto .'+ self.cond1_ls +' \n'
                codigo += '    label .'+cond1_lf + '\n'
                controlador.append_3d(codigo)
            else:
                #error
                error =''
        else:
            codigo = '    #sentencia else  \n'
            controlador.append_3d(codigo)

            #declaraciones

            #solo necesito ejecutar instrucciones
            for i in self.lista_inst: 
                i.traducir(tabla, controlador, arbol)