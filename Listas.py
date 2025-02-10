class NodoMantenimiento:
    def __init__(self, mantenimiento):
        self.mantenimiento = mantenimiento
        self.siguiente = None

class NodoVehiculo:
    def __init__(self, vehiculo):
        self.vehiculo = vehiculo
        self.siguiente = None
        self.anterior = None

class ListaMantenimiento:
    def __init__(self):
        self.head = None

class FlotaVehiculos:
    def __init__(self):
        self.head = None
        self.tail = None

