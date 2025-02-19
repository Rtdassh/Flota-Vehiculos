import os
import msvcrt as mv
import Listas
import Mantenimiento
import Vehiculo as Vc

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
                vehiculo = Vc.Vehiculo(placa, marca, modelo, anio, kilometraje)
            except ValueError as ve:
                print("Error:", ve)
                mv.getch()
                continue

            flota.registrar_vehiculo(vehiculo)   
        elif opcion == "2":
            print("Eliminar vehículo de la Lista")
            print("--------------------------")   
            placa = input("Ingrese la placa del vehículo a eliminar: ")
            flota.eliminar_vehiculo(placa)

        elif opcion == "3":
            print("Búsqueda de Vehículo")
            print("--------------------------")   
            placa = input("Ingrese la placa del vehículo a buscar: ")
            Vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo:
                print(f"Vehículo encontrado:\nPlaca: {vehiculo.placa}, Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}, Kilometraje: {vehiculo.kilometraje}")
            else:
                print("Vehículo no encontrado.")
        elif opcion == "4":
            print("Listado de Vehículos")
            print("--------------------------") 
            flota.listar_vehiculos()  
        elif opcion == "5":
            print("Agregar Vehículo")
            print("--------------------------")
            placa = input("Ingrese la placa del vehículo para agregar mantenimiento: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo is None:
                print("Vehículo no encontrado.")
                mv.getch()
                continue
            factura = input("Ingrese el número de Factura: ")
            fecha = input("Ingrese la fecha del mantenimiento (DD-MM-YYYY): ")
            descripcion = input("Ingrese la descripción del mantenimiento: ")
            try:
                costo = float(input("Ingrese el costo del mantenimiento: "))
            except ValueError:
                print("Costo inválido.")
                mv.getch()
                continue

            try:
                mantenimiento = Mantenimiento.Mantenimiento(factura,fecha, descripcion, costo)
            except ValueError as ve:
                print("Error:", ve)
                mv.getch()
                continue

            vehiculo.agregar_mantenimiento(mantenimiento)
            print("Mantenimiento agregado con éxito.")   
        elif opcion == "6":
            print("Historial de Mantenimiento")
            print("--------------------------")
            placa = input("Ingrese la placa del vehículo para ver su historial de mantenimientos: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo is None:
                print("Vehículo no encontrado.")
                mv.getch()
                continue
            print(f"\nHistorial de mantenimientos del vehículo {vehiculo.placa}:")
            vehiculo.mostrar_historial()   
        elif opcion == "7":
            print("Costo Total de Mantenimientos")
            print("--------------------------")
            placa = input("Ingrese la placa del vehículo para calcular el costo total de mantenimientos: ")
            vehiculo = flota.buscar_vehiculo(placa)
            if vehiculo is None:
                print("Vehículo no encontrado.")
                mv.getch()
                continue
            total = vehiculo.costo_total_mantenimientos()
            print(f"Costo total de mantenimientos: {total}")

        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
        mv.getch()

if __name__ == "__main__":
    menu()