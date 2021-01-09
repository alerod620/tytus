
from enum import Enum

class Tipo_Dato(Enum):
    # ENTERO
    SMALLINT = 1
    INTEGER = 2
    BIGINT = 3
    DECIMAL = 4
    NUMERIC = 5
    REAL = 6
    DOUBLE_PRECISION = 7
    MONEY = 8
    # CADENA
    CHAR = 9
    VARCHAR = 10
    VARYING = 11
    CHARACTER = 12
    TEXT = 13
    # FECHA
    DATE = 14
    TIMESTAMP = 15
    TIME = 16
    INTERVAL = 17
    # BOOLEAN
    BOOLEAN = 18
    TIPOENUM = 19
    # ID 
    ID = 20
    QUERY = 21
    # INDEX
    INDEX = 22
    # VOID
    VOID = 23

class Tipo():
    'Esta clase será de utilidad para la comprobación de tipos.'
    def __init__(self, tipo, dimension=None):
        self.tipo = tipo
        self.dimension = dimension
        self.nombre = ''
        
    def toString(self):
        if self.tipo == Tipo_Dato.SMALLINT:
            return "smallint"
        elif self.tipo == Tipo_Dato.INTEGER:
            return "integer"
        elif self.tipo == Tipo_Dato.BIGINT:
            return "bigint"
        elif self.tipo == Tipo_Dato.DECIMAL:
            return "decimal"
        elif self.tipo == Tipo_Dato.NUMERIC:
            return "numeric"
        elif self.tipo == Tipo_Dato.REAL:
            return "real"
        elif self.tipo == Tipo_Dato.DOUBLE_PRECISION:
            return "double precision"
        elif self.tipo == Tipo_Dato.MONEY:
            return "money"
        elif self.tipo == Tipo_Dato.CHAR:
            return "char"
        elif self.tipo == Tipo_Dato.VARCHAR:
            return "varchar"
        elif self.tipo == Tipo_Dato.VARYING:
            return "character varying"
        elif self.tipo == Tipo_Dato.CHARACTER:
            return "character"
        elif self.tipo == Tipo_Dato.TEXT:
            return "text"
        elif self.tipo == Tipo_Dato.DATE:
            return "date"
        elif self.tipo == Tipo_Dato.TIMESTAMP:
            return "timestamp"
        elif self.tipo == Tipo_Dato.TIME:
            return "time"
        elif self.tipo == Tipo_Dato.INTERVAL:
            return "interval"
        elif self.tipo == Tipo_Dato.BOOLEAN:
            return "boolean"
        elif self.tipo == Tipo_Dato.TIPOENUM:
            return "enum"
        elif self.tipo == Tipo_Dato.ID:
            return "id"
        elif self.tipo == Tipo_Dato.QUERY:
            return "query"
        elif self.tipo == Tipo_Dato.INDEX:
            return "index"
        elif self.tipo == Tipo_Dato.VOID:
            return "void"

    def traducir(self, tabla, controlador, arbol):
        codigo = 'Tipo(Tipo_Dato.' 
        if self.tipo == Tipo_Dato.SMALLINT:
            codigo += 'SMALLINT, '
        elif self.tipo == Tipo_Dato.INTEGER:
            codigo += 'INTEGER, '
        elif self.tipo == Tipo_Dato.BIGINT:
            codigo += 'BIGINT, '
        elif self.tipo == Tipo_Dato.DECIMAL:
            codigo += 'DECIMAL, '
        elif self.tipo == Tipo_Dato.NUMERIC:
            codigo += 'NUMERIC, '
        elif self.tipo == Tipo_Dato.REAL:
            codigo += 'REAL, '
        elif self.tipo == Tipo_Dato.DOUBLE_PRECISION:
            codigo += 'DOUBLE_PRECISION, '
        elif self.tipo == Tipo_Dato.MONEY:
            codigo += 'MONEY, '
        elif self.tipo == Tipo_Dato.CHAR:
            codigo += 'CHAR, '
        elif self.tipo == Tipo_Dato.VARCHAR:
            codigo += 'VARCHAR, '
        elif self.tipo == Tipo_Dato.VARYING:
            codigo += 'VARYING, '
        elif self.tipo == Tipo_Dato.CHARACTER:
            codigo += 'CHARACTER, '
        elif self.tipo == Tipo_Dato.TEXT:
            codigo += 'TEXT, '
        elif self.tipo == Tipo_Dato.DATE:
            codigo += 'DATE, '
        elif self.tipo == Tipo_Dato.TIMESTAMP:
            codigo += 'TIMESTAMP, '
        elif self.tipo == Tipo_Dato.TIME:
            codigo += 'TIME, '
        elif self.tipo == Tipo_Dato.INTERVAL:
            codigo += 'INTERVAL, '
        elif self.tipo == Tipo_Dato.BOOLEAN:
            codigo += 'BOOLEAN, '
        elif self.tipo == Tipo_Dato.TIPOENUM:
            codigo += 'TIPOENUM, '
        elif self.tipo == Tipo_Dato.ID:
            codigo += 'ID, '
        elif self.tipo == Tipo_Dato.QUERY:
            codigo += 'QUERY, '
        elif self.tipo == Tipo_Dato.INDEX:
            codigo += 'INDEX, '
        elif self.tipo == Tipo_Dato.VOID:
            codigo += 'VOID, '
        if self.dimension is None:
            codigo += 'None)'
        elif self.dimension is list:
            codigo += '['
            for r in self.dimension:
                codigo += str(r) + ', '
            codigo = codigo[0:-2] + '])'
        else:
            codigo += str(self.dimension) + ')'
        return codigo
