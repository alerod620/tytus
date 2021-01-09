
class controlador():
    def __init__(self):
        #encabezado del archivo de salia en python
        self.c3d = '\nfrom goto import with_goto \n \n#declaracion de heap y stack \nheap = [10000] \nstack = [10000] \nP = 0 \nH = 0 \n'
        
        self.cont_temp = 0
        self.etiquetas = 0
        self.heap = 0
        self.stack = 0
        self.errores = []
        self.etiqueta_salida = ''
        self.c3d_ejecutar = '\n#### ejecucion de codigo 3d #### \n@with_goto\ndef ejecutar_3d():\n'

    def append_3d(self, codigo):
        self.c3d += codigo +'\n'

    def append_3d_ejecutar(self,codigo):
        self.c3d_ejecutar += codigo +'\n'

    def get_etiqueta(self):
        self.etiquetas = self.etiquetas+1
        return 'L' +  str(self.etiquetas)

    def set_stack(self,pos):
        self.stack = pos

    def get_stack(self):
        self.stack = self.stack + 1
        return self.stack
    