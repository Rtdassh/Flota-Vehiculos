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

    def registrar_vehiculo(self, vehiculo):
        if self.buscar_vehiculo(vehiculo.placa) is not None:
            print("El vehículo con esa placa ya está registrado.")
            return False
        nuevo_nodo = NodoVehiculo(vehiculo)
        if self.head is None:
            self.head = self.tail = nuevo_nodo
        else:
            self.tail.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.tail
            self.tail = nuevo_nodo
        print("Vehículo registrado con éxito.")
        return True

    def _buscar_nodo(self, placa):
        actual = self.head
        while actual:
            if actual.vehiculo.placa == placa:
                return actual
            actual = actual.siguiente
        return None

    def buscar_vehiculo(self, placa):
        nodo = self._buscar_nodo(placa)
        if nodo:
            return nodo.vehiculo
        return None

    def eliminar_vehiculo(self, placa):
        nodo = self._buscar_nodo(placa)
        if nodo is None:
            print("Vehículo no encontrado.")
            return False
        if nodo.anterior:
            nodo.anterior.siguiente = nodo.siguiente
        else:
            self.head = nodo.siguiente
        if nodo.siguiente:
            nodo.siguiente.anterior = nodo.anterior
        else:
            self.tail = nodo.anterior
        print("Vehículo eliminado con éxito.")
        return True

    def listar_vehiculos(self):
        if self.head is None:
            print("No hay vehículos registrados.")
            return
        actual = self.head
        while actual:
            v = actual.vehiculo
            print(f"Placa: {v.placa}, Marca: {v.marca}, Modelo: {v.modelo}, Año: {v.anio}, Kilometraje: {v.kilometraje}")
            actual = actual.siguiente

