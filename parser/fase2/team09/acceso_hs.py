import reglas as r

class Acceso():

    def __init__(self, ins, literal, operacion):
        self.ins = ins
        self.literal = literal
        self.operacion = operacion

    def optimizacion(self):
        print('Entro a la funcion de acceso')
        operacion = ''
        if len(self.operacion) == 1:
            operacion = str(self.operacion[0])
        else:
            operacion = str(self.operacion[0]) + ' ' + str(self.operacion[1]) + ' ' + str(self.operacion[2])

        n = ''
        if self.ins == 'HEAP':
            n = 'heap[' + str(self.literal) + '] = ' + operacion
        elif self.ins == 'STACK':
            n = 'stack[' + str(self.literal) + '] = ' + operacion

        print('el codigo es -> ' + n)

        r.Reglas.optimizado = r.Reglas.optimizado + '    ' + n + '\n'