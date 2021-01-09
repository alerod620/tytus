
from enum import Enum

class Tipo_Dato_Constraint(Enum):
    # ENTERO
    PRIMARY_KEY = 1
    FOREIGN_KEY = 2
    REFERENCES = 3
    DEFAULT = 4
    NOT_NULL = 5
    NULL = 6
    UNIQUE = 7
    CONSTRAINT = 8
    CHECK = 9

class Tipo_Constraint():
    'Esta clase será de utilidad para la comprobación de tipos.'
    def __init__(self, id, tipo, expresion):
        self.id = id
        self.tipo = tipo
        self.expresion = expresion
        self.referencia = ''

    def toString(self):
        if self.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
            return "primary_key"
        elif self.tipo == Tipo_Dato_Constraint.FOREIGN_KEY:
            return "foreign_key"
        elif self.tipo == Tipo_Dato_Constraint.REFERENCES:
            return "references"
        elif self.tipo == Tipo_Dato_Constraint.DEFAULT:
            return "default"
        elif self.tipo == Tipo_Dato_Constraint.NOT_NULL:
            return "not_null"
        elif self.tipo == Tipo_Dato_Constraint.NULL:
            return "null"
        elif self.tipo == Tipo_Dato_Constraint.UNIQUE:
            return "unique"
        elif self.tipo == Tipo_Dato_Constraint.CONSTRAINT:
            return "constraint"
        elif self.tipo == Tipo_Dato_Constraint.CHECK:
            return "check"

    def traducir(self, tabla, controlador, arbol):
        codigo = 'Tipo_Constraint('
        if self.id is None:
            codigo += 'None, Tipo_Dato_Constraint.'
        elif self.id is list:
            codigo += '['
            for id in self.id:
                codigo += '"' + id + '", '
            codigo = codigo[0:-2] + '], Tipo_Dato_Constraint.'
        else:
            codigo += '"' + self.id + '", Tipo_Dato_Constraint.'
        if self.tipo == Tipo_Dato_Constraint.PRIMARY_KEY:
            codigo += 'PRIMARY_KEY, '
        elif self.tipo == Tipo_Dato_Constraint.FOREIGN_KEY:
            codigo += 'FOREIGN_KEY, '
        elif self.tipo == Tipo_Dato_Constraint.REFERENCES:
            codigo += 'REFERENCES, '
        elif self.tipo == Tipo_Dato_Constraint.DEFAULT:
            codigo += 'DEFAULT, '
        elif self.tipo == Tipo_Dato_Constraint.NOT_NULL:
            codigo += 'NOT_NULL, '
        elif self.tipo == Tipo_Dato_Constraint.NULL:
            codigo += 'NULL, '
        elif self.tipo == Tipo_Dato_Constraint.UNIQUE:
            codigo += 'UNIQUE, '
        elif self.tipo == Tipo_Dato_Constraint.CONSTRAINT:
            codigo += 'CONSTRAINT, '
        elif self.tipo == Tipo_Dato_Constraint.CHECK:
            codigo += 'CHECK, '
        if self.expresion is None:
            codigo += 'None)'
        elif self.expresion is list:
            codigo += '['
            for exp in self.expresion:
                codigo += '"' + exp + '", '
            codigo = codigo[0:-2] + '])'
        else:
            codigo += self.expresion.traducir(tabla, controlador, arbol) + ')'
        return codigo
