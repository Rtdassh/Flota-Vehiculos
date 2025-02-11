import datetime as dt
from Listas import ListaMantenimiento

class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__kilometraje = kilometraje
        self.historial = ListaMantenimiento()

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, valor):
        if len(valor) < 5 or not valor.isalnum():
            raise ValueError("Formato de placa incorrecto. Debe ingresar al menos 5 caracteres y ser alfanumérica.")
        self.__placa = valor

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor

    @property
    def anio(self):
        return self.__anio

    @anio.setter
    def anio(self, valor):
        anio_actual = dt.datetime.now().year
        if not (1900 < valor <= anio_actual):
            raise ValueError("Año inválido. Debe ser mayor a 1900 y menor o igual al año actual.")
        self.__anio = valor

    @property
    def kilometraje(self):
        return self.__kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if valor < 0:
            raise ValueError("El kilometraje debe ser un número positivo.")
        self.__kilometraje = valor

    # Métodos historial de mantenimientos

    def agregar_mantenimiento(self, mantenimiento):
        self.historial.agregar(mantenimiento)

    def mostrar_historial(self):
        self.historial.imprimir()

    def costo_total_mantenimientos(self):
       return self.historial.calcular_costo_total()