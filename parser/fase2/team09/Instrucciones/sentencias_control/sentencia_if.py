from Instrucciones.TablaSimbolos.Tipo import Tipo_Dato, Tipo

class sentencia_if():
    def __init__(self, si, lista_sino, sino):
        self.si = si 
        self.lista_sino = lista_sino
        self.sino = sino 
        self.lista_if = []

    def traducir(self, tabla, controlador, arbol):
        codigo = ''
        print('entro al traducir de la sentencia if')
        
        #guardo todo en una lista 
        self.lista_if.append(self.si)

        if(self.lista_sino != None):
            for i in self.lista_sino:
                self.lista_if.append(i)

        if(self.sino != None):
            self.lista_if.append(self.sino)

        #etiqueta para el c3d
        cond1_ls = controlador.get_etiqueta() #etiqueta de salida

        #Voy a la clase sino a generar el codigo
        for i in self.lista_if:
            print(str(i))
            i.cond1_ls = cond1_ls  #se asigna la etiqueta de salida
            i.traducir(tabla, controlador, arbol)
        
        codigo = '    label .'+cond1_ls+'\n'
        codigo +='    #Fin de la sentencia de control IF \n'
        controlador.append_3d(codigo)