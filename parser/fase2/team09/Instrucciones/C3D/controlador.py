
class controlador():
    def __init__(self):
        #encabezado del archivo de salia en python
        self.c3d  = 'from Instrucciones import Relaciones\n'
        self.c3d += 'from Instrucciones.DateTimeTypes import Case , CurrentDate, CurrentTime, DatePart, Extract, Now, Por, TimeStamp\n'
        self.c3d += 'from Instrucciones.Excepcion import Excepcion\n'
        self.c3d += 'from Instrucciones.Expresiones import Aritmetica, Logica, Primitivo, Relacional, Between\n'
        self.c3d += 'from Instrucciones.FunctionAgregate import Avg, Count, Greatest, Least, Max, Min, Sum, Top\n'
        self.c3d += 'from Instrucciones.FunctionBinaryString import Convert, Decode, Encode, GetByte, Length, Md5, SetByte, Sha256, Substr, Substring, Trim\n'
        self.c3d += 'from Instrucciones.FunctionMathematical import Abs, Cbrt, Ceil, Ceiling, Degrees, Div, Exp, Factorial, Floor, Gcd, Lcm, Ln, Log, Log10, MinScale, Mod, PI, Power, Radians, Random, Round, Scale, SetSeed, Sign, Sqrt, TrimScale, Trunc, WidthBucket\n'
        self.c3d += 'from Instrucciones.FunctionTrigonometric import Acos, Acosd, Acosh, Asin, Asind, Asinh, Atan, Atan2, Atan2d, Atand, Atanh, Cos, Cosd, Cosh, Cot, Cotd, Sin, Sind, Sinh, Tan, Tand, Tanh\n'
        self.c3d += 'from Instrucciones.Identificador import Identificador\n'
        self.c3d += 'from Instrucciones.PLpgSQL import Asignacion, Body, CaseWhen, Continue, CreateFunction, Execute, Exit, For, IfElse, Llamada, Loop, Parametro, Variable, While\n'
        self.c3d += 'from Instrucciones.Sql_alter import AlterDatabase, AlterDBOwner, AlterIndex, AlterTable, AlterTableAddColumn, AlterTableAddConstraintFK, Columna, AlterTableDropColumn, AlterTableAddConstraint, AlterTableAddFK, AlterTableAlterColumn, AlterTableDropConstraint, AlterTableAlterColumnType, AlterTableAddCheck\n'
        self.c3d += 'from Instrucciones.Sql_create import CreateDatabase, CreateIndex, Campo, CreateOrReplace, CreateTable, CreateType, Use, ShowDatabases,Set\n'
        self.c3d += 'from Instrucciones.Sql_create import Columna as CColumna\n'
        self.c3d += 'from Instrucciones.Sql_create.Tipo_Constraint import *\n'
        self.c3d += 'from Instrucciones.Sql_declare import Declare\n'
        self.c3d += 'from Instrucciones.Sql_delete import DeleteTable\n'
        self.c3d += 'from Instrucciones.Sql_drop import DropDatabase, DropIndex, DropTable\n'
        self.c3d += 'from Instrucciones.Sql_insert import insertTable\n'
        self.c3d += 'from Instrucciones.Sql_Joins import Join, JoinFull, JoinInner, JoinLeft, JoinRight\n'
        self.c3d += 'from Instrucciones.Sql_select import GroupBy, Having, Limit, OrderBy, Select, Where, SelectLista\n'
        self.c3d += 'from Instrucciones.Sql_truncate import Truncate\n'
        self.c3d += 'from Instrucciones.Sql_update import UpdateTable\n'
        self.c3d += 'from Instrucciones.TablaSimbolos.Instruccion import Instruccion\n'
        self.c3d += 'from Instrucciones.TablaSimbolos.Tipo import Tipo, Tipo_Dato\n'
        self.c3d += 'from Instrucciones.Undefined import Undefined\n'
        self.c3d += 'from Instrucciones.PLpgSQL.sentencia_return import sentencia_return\n'
        self.c3d += 'from Instrucciones.TablaSimbolos.Tabla import Tabla\n'
        self.c3d += 'from Instrucciones.TablaSimbolos.Arbol import Arbol\n'
        self.c3d += 'from goto import with_goto\n'
        self.c3d += 'tabla = Tabla(None)\n'
        self.c3d += 'arbol = Arbol(None)\n'
        self.c3d += '\n#declaracion de heap y stack \nheap = [10000] \nstack = [10000] \nP = 0 \nH = 0 \n'
        
        self.c3d += '#inicialisacion de heap y stack \nfor i in range(1000): \n    stack.append(i) \n    heap.append(i)'

        self.cont_temp = 0
        self.etiquetas = 0
        self.heap = 0
        self.stack = 0
        self.errores = []
        self.etiqueta_salida = ''
        self.c3d_ejecutar = '\n#### ejecucion de codigo 3d #### \n@with_goto\ndef ejecutar_3d():\n'
        self.c3d_ejecutar += '    global P \n    global H \n    global heap \n    global stack\n'
        self.peso_fun_actual = 0

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
    