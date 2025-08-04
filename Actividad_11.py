def quick_sort(nombres):
    if len(nombres) <= 1:
        return nombres
    pivote = nombres[0]
    menores = [x for x in nombres if x < pivote]
    iguales = [x for x in nombres if x == pivote]
    mayores = [x for x in nombres if x > pivote]
    return quick_sort(menores) + iguales + quick_sort(mayores)
nombres = []
try:
    cantidad = int(input("¿Cuántos nombres desea ingresar?: "))
    for i in range(cantidad):
        nombre = input(f"Ingrese el nombre {i + 1}: ")
        nombres.append(nombre)
except Exception as e:
    print(f"Ha ocurrido un error: {e}")
print("Nombres ingresados ordenados:")
print(quick_sort(nombres))