import reglas as r

class Asignacion():
    def __init__(self, cadena):
        self.cadena = cadena

    def optimizacion(self):
        r.Reglas.pendiente = r.Reglas.pendiente + '    ' + self.cadena + '\n'