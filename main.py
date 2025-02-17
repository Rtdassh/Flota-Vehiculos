import os
import msvcrt as mv
import Listas
import Mantenimiento
import Vehiculo

def menu():
    flota = Listas.FlotaVehiculos()
    while True:
        os.system("cls")
        print("--- Taller Cifuentes ---")
        print("1. Registrar vehículo")
        print("2. Eliminar vehículo")
        print("3. Buscar vehículo")
        print("4. Listar vehículos")
        print("5. Agregar mantenimiento a un vehículo")
        print("6. Mostrar historial de mantenimientos de un vehículo")
        print("7. Costo total de mantenimientos de un vehículo")
        print("8. Salir")

        opcion = input("Seleccione una opción: ")
        os.system("cls")

        if opcion == "1":
            print("Registro de Vehículo")
            print("--------------------------")
            placa = input("Ingrese la placa del vehículo: ")
            marca = input("Ingrese la marca del vehículo: ")
            modelo = input("Ingrese el modelo del vehículo: ")
            try:
                anio = int(input("Ingrese el año del vehículo: "))
                kilometraje = float(input("Ingrese el kilometraje: "))
            except ValueError:
                print("Año o kilometraje inválido.")
                mv.getch()
                continue

            try:
                vehiculo = Vehiculo(placa, marca, modelo, anio, kilometraje)
            except ValueError as ve:
                print("Error:", ve)
                mv.getch()
                continue

            flota.registrar_vehiculo(vehiculo)   
        elif opcion == "2":
            print("Eliminar vehículo de la Lista")
            print("--------------------------")   
        elif opcion == "3":
           print("Búsqueda de Vehículo")
           print("--------------------------")   
        elif opcion == "4":
            print("Listado de Vehículos")
            print("--------------------------")   
        elif opcion == "5":
            print("Agregar Vehículo")
            print("--------------------------")   
        elif opcion == "6":
            print("Historial de Mantenimiento")
            print("--------------------------")   
        elif opcion == "7":
            print("Costo Total de Mantenimientos")
            print("--------------------------")   
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
        mv.getch()

if __name__ == "__main__":
    menu()