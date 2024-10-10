def crear_matriz_vacia(filas, columnas):
    matriz = []
    for i in range(filas):
        matriz.append([])
        for j in range(columnas):
            matriz[i].append(0)
    return matriz

def main():



    #VENDEDOR
    ##datos necesarios
    print (" ingrese de que tipo será su presentación:")
    print (" ¿será cine? o ¿una conferencia? o acaso ¿un partido de futbol? ")

    tipo_show = input()
    print ("¿En que lugar desea llevar a cabo su presentación? ")
    print ("Escriba la dirección, la ciudad y si es necesario instrucciones especifas para ingresar al sitio")
    lugar = input()
    n = input("ingrese la fecha del espectáculo separando dia, mes y año con ´/´")
    m = input("ingrese la hora ")
    fecha = f"{n} a las {m}"
    print (fecha)
    print("A continuación se hará una representación del espacio en que se hará el show")
    
    f = int(input("ingrese numero de filas "))
    matriz = crear_matriz_vacia()
    print(matriz)

if __name__ == "__main__":
    main()
