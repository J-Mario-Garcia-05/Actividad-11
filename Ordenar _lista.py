def quick_sort(nombres):
    if len(nombres) <= 1:
        return nombres
    pivote = nombres[0]
    menores = [x for x in nombres if x < pivote]
    iguales = [x for x in nombres if x == pivote]
    mayores = [x for x in nombres if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
nombres = []
opcion = "0"
while opcion != "3":
    print("==MENÚ==")
    print("1.Agregar nombres")
    print("2.Mostrar nombres agregados")
    print("3.Salir")
    opcion = input("\nSeleccione una opción: ")
    try:
        match opcion:
            case "1":
                cantidad = int(input("¿Cuántos nombres desea ingresar?: "))
                for i in range(cantidad):
                    nombres.append(input(f"Ingrese el nombre {i + 1}: "))
            case "2":
                if not nombres:
                    print("No ha ingresado ningún nombre")
                    continue
                print("Nombres agregados:")
                for i in nombres:
                    print(i, end= ", ")
                print("\nNombres ingresados ordenados:")
                print(quick_sort(nombres))
            case "3":
                print("Saliendo")
            case __:
                print("Opcion no disponible")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")