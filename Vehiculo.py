from Listas import ListaMantenimiento

class Vehiculo:
    def __init__(self, placa, marca, modelo, anio, kilometraje):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__kilometraje = kilometraje
        self.historial = ListaMantenimiento()