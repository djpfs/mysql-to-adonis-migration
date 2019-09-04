import re
f = open("colaboradores.sql","r")


class SqlToLucid:

    def typeOfString(self, typeOf):
        if "int(" in typeOf:
            return "integer"
        elif "varchar" in typeOf:
            return "string"
        elif "tinyint" in typeOf:
            return "integer"
        elif "datetime" in typeOf:
            return "datetime"
        elif "date" in typeOf:
            return "date"
        elif "time" in typeOf:
            return "time"
        elif "bool" in typeOf:
            return "bool"
        else:
            return ""

    def getSize(self, string):
        number = re.sub("\D", "", string)
        if (len(number) >= 1): return ', ' + str(number)
        else: return ''

    def __init__(self, obj):
        self.field = obj[2]
        self.type = obj[3]

    def toString(self):
        tipo = self.typeOfString(str(self.type))
        return 'table.' + tipo + '(' + self.field + self.getSize(self.type) + ')'

campos = []

for x in f:
    value = SqlToLucid(x.split(" "))
    if (value.field != "`colaboradores`" and value.field != "DEFAULT"):
        campos.append(value)

for x in campos:
  print(x.toString())




