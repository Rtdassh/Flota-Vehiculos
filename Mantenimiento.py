import datetime as dt

class Mantenimiento:
    def __init__(self, factura, fecha, descripcion, costo):
        self.factura = factura
        self.fecha = fecha
        self.descripcion = descripcion
        self.costo = costo
        
    @property
    def factura(self):
        return self.__factura
    @factura.setter
    def factura(self, valor):
        self.__factura = valor

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self, valor):
        try:
            dt.datetime.strptime(valor, "%d-%m-%Y")
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use DD-MM-YYYY.")
        self.__fecha = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @property
    def costo(self):
        return self.__costo

    @costo.setter
    def costo(self, valor):
        if valor <= 0:
            raise ValueError("El costo debe ser un número positivo.")
        self.__costo = valor