from importlib.util import set_loader


class Proyecto:
    def __init__(self, codigo, nombre, precio): #self se refiere a los mismos atributos de la clase
        self.__codigo = codigo #__ aquí se refiere a un atributo privado
        self.__nombre = nombre
        self.__precio = precio

#Aquí se definen los getters y setters

    @property #getter
    def codigo(self):
        return self.__codigo

    @codigo.setter #setter
    def codigo(self, valor):
        self.__codigo = valor
        
    @property #getter
    def nombre(self):
        return self.__nombre

    @nombre.setter #setter
    def nombre(self, valor):
        self.__nombre = valor

    @property #getter
    def precio(self):
        return self.__precio

    @precio.setter #setter
    def precio(self, valor):
        self.__precio = valor