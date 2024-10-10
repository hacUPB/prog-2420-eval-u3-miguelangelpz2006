[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MuElT52l)
# Unidad 3
---
## Documentación del proyecto
Nombre:  Miguel Ángel Perea Zapata
ID:  000552221
---
## INTRODUCCIÓN:
En el mundo de los negocios y el espectáculo es fundamental la agilidad y la automatización de procesos tan monótonos como lo son las reservas. Para esta problemática propongo hacer un sistema en el cual se puedan hacer las reservas de forma sencilla y sin la necesidad de personal, todo mediante una aplicación. Este sistema servirá para las pequeñas, medianas y grandes empresas, y que la persona que desee alquilar asientos en el lugar que sea, ya sea para dar una conferencia, dar una función de cine, dar un espectáculo de magia, etc.
---
## Elaboración:
### Como vendedor:
•	Datos necesarios: tipo de espectáculo, lugar del espectáculo, hora de presentación, asientos que desea vender, costo de los asientos
•	Inicio
o	#ingrese el tipo de espectáculo
o	#ingrese lugar del espectáculo
o	#ingrese hora de presentación
o	“Crear matriz (representación del espacio del espectáculo) esta será actualizada por cada comprador, poniendo un valor de 0 si está disponible el asiento y de 1 si no lo está”
o	##ingrese el número de filas
o	##ingrese el número de columnas
o	# ¿desea seleccionar el precio individualmente de cada asiento?
o	##si la respuesta es sí:
o	###crear función 
o	####utilizar la función para asignarle precio a cada asiento hasta el ultimo
o	##si la respuesta es no:
o	##ingrese el precio de cada asiento
o	##crear una matriz del mismo tamaño que la representación del espectáculo
o	#imprimir todos los datos puestos y las matrices
•	fin 
### Como comprador:
•	Ver todos los datos que ha seleccionado el vendedor y la matriz con los asientos disponibles
•	Datos necesarios: selección de asiento
•	inicio
o	#imprimir el sitio que ha seleccionado mostrándolo en la matriz 1
o	#imprimir el valor que tiene el asiento seleccionado, comparándolo con la misma posición de la matriz 2
o	#actualizar la matriz 1 y poner un 1 en el sitio que se seleccionó
•	fin
