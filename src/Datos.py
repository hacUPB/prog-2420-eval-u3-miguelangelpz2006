#funcion para crear matriz de vendedor
def crear_matriz_vacia(filas, columnas):
    # Crea una matriz vacía de tamaño filas x columnas con ceros
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(0)
    return matriz

#funcion para asignar precios
def asignar_precio_individual(filas, columnas):
    matriz_precios = []
    for i in range(filas):
        fila_precios = []
        for j in range(columnas):
            precio = int(input(f"Ingrese el precio del asiento en la fila {i + 1}, columna {j + 1}: "))
            fila_precios.append(precio)
        matriz_precios.append(fila_precios)
    return matriz_precios

def main():
# VENDEDOR
    # Datos necesarios que se le imprimirán al comprador 
    print("INGRESE DE QUÉ TIPO SERÁ SU PRESENTACIÓN:")
    print("¿Será cine? ¿Una conferencia? ¿O acaso un partido de futbol?")
    
    tipo_show = input()
    
    print("¿En qué lugar desea llevar a cabo su presentación?")
    print("Escriba la dirección, la ciudad y si es necesario instrucciones específicas para ingresar al sitio.")
    
    lugar = input()
    
    n = input("Ingrese la fecha del espectáculo separando día, mes y año con ‘/’: ")
    m = input("Ingrese la hora: ")
    
    fecha = f"{n} a las {m}"
    print(f"\nFecha y hora del espectáculo: {fecha}")
    
    print("\nA continuación, se hará una representación del espacio en que se hará el show.")
    
    # Dimensiones de la matriz
    filas = int(input("Ingrese número de filas: "))
    columnas = int(input("Ingrese número de columnas: "))
    
    # Crear las matrices vacías
    matriz_espacio = crear_matriz_vacia(filas, columnas)

    # Precio de los asientos
    respuesta = input("¿Desea asignar el precio individualmente a cada asiento? (si/no): ").lower()

    if respuesta == "si":
        # Crear una matriz de precios asignados individualmente
        matriz_precios = asignar_precio_individual(filas, columnas)
    else:
        # Asignar un precio global a todos los asientos
        precio_global = int(input("Ingrese el precio de cada asiento: "))
        matriz_precios = [[precio_global for _ in range(columnas)] for _ in range(filas)]

    # Representaciones de las matrices
    print("\n**** Representación del espacio (0 = disponible, 1 = ocupado) ****")
    for fila in matriz_espacio:
        print(fila)

    print("\n**** Matriz de precios de los asientos ****")
    for fila in matriz_precios:
        print(fila)

# CLIENTE     
    # Seleccionar asiento
    while True:
        fila_cliente = int(input(f"Seleccione la fila del asiento [0 a {filas - 1}]: "))
        columna_cliente = int(input(f"Seleccione la columna del asiento [0 a {columnas - 1}]: "))

        # Verificar si el asiento está disponible
        if matriz_espacio[fila_cliente][columna_cliente] == 0:
            print(f"El asiento en la fila {fila_cliente + 1}, columna {columna_cliente + 1} tiene un precio de ${matriz_precios[fila_cliente][columna_cliente]}")
            
            # Actualizar la matriz de espacio para indicar que el asiento ha sido ocupado
            matriz_espacio[fila_cliente][columna_cliente] = 1
            print("**** El asiento ha sido reservado exitosamente ****")
            break
        else:
            print("Ese asiento ya está ocupado. Por favor, seleccione otro.")

    # Mostrar matriz de asientos actualizada
    print("\n***** Representación actualizada del espacio (0 = disponible, 1 = ocupado) *****")
    for fila in matriz_espacio:
        print(fila)

    # Mostrar toda la información:
    print("Resumen del espectáculo:")
    print(f"Tipo de espectáculo: {tipo_show}")
    print(f"Lugar: {lugar}")
    print(f"Fecha: {fecha}")
    print(f"Asiento reservado: Fila {fila_cliente + 1}, Columna {columna_cliente + 1}")
    print(f"Precio del asiento: ${matriz_precios[fila_cliente][columna_cliente]}")

if __name__ == "__main__":
    main()
