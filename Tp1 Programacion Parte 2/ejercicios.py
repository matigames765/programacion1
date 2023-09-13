#1.	Calcular el perímetro y área de un rectángulo dada su base y su altura.

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
perimetro = base * 2 + altura * 2
area = base * altura
print(f"El perimetro del rectangulo es {perimetro} y el area {area}")

#2.	Dados los catetos de un triángulo rectángulo, calcular su hipotenusa.
cateto1 = float(input("Ingrese la medida del primer cateto: "))
cateto2 = float(input("Ingrese la medida del segundo cateto: "))
hipotenusa = (cateto1**2 + cateto2**2)**(1/2)
print(f"La hipotenusa del triangulo rectangulo es {hipotenusa}")

#3.	Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
numero1 = float(input("Introduce el primer numero: "))
numero2 = float(input("Introduce el segundo numero: "))
suma = numero1 + numero2
resta = numero1 - numero2
division = numero1 / numero2
multiplicacion = numero1 * numero2
print(f"{numero1} + {numero2}: {suma}")
print(f"{numero1} - {numero2}: {resta}")
print(f"{numero1} / {numero2}: {division}")
print(f"{numero1} * {numero2}: {multiplicacion}")


'''4.	Escribir un programa que convierta un valor dado en grados Fahrenheit a 
grados Celsius. Recordar que la fórmula para la conversión es: C = (F-32)*5/9'''

farenheit = float(input("Introduce temperatura en farenheit para convertirla a celsius"))
celsius = (farenheit - 32) * (5/9)
print(f"{farenheit}F pasado a celsius son {celsius}Cº")


'''5.	¿Qué problemas tienen las siguientes instrucciones?¿Cómo las solucionarías?

a)	A = input(nombre, “¿Cuál es tu canción favorita?”)
b)	precio = input(“Precio: “)
total = precio + (precio * 0.1)
c)	edad = int(input(“Edad: “))
print(tu edad es, edad)
d)	edad = int(input(“Edad: “))
print(“Veamos si tu edad es 18…”, edad=18)
Resolucion: 
a) El problema es que no esta definido nombre, lo solucionaria definiendo nombre antes o
borrandolo del input
b) El problema es que ingresaremos un valor numerico y el input recibe strings, lo solucionaria
transformando el float el ingreso del input
c) El problema es que la cadena que se quiere mostrar se deberia ingresar entre comillas simples
o dobles y lo solucionaria colocando alguna de las comillas
d) El problema es que le esta asignado el valor dentro a una variable dentro de un print, lo 
solucionaria eliminando esta accion
'''

'''6.	Calcular la media de tres números pedidos por teclado.'''
numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
numero3 = float(input("Ingrese el tercer numero: "))
media = (numero1 + numero2 + numero3)/3
print(f"La media de los tres numeros es {media}")

'''7.	Realiza un programa que reciba una cantidad de minutos y muestre por pantalla a 
cuantas horas y minutos corresponde. Por ejemplo: 1000 minutos son 16 horas y 40 minutos.'''
minutos = float(input("Ingrese una cantidad de minutos para pasarlo a horas y minutos: "))
horas = int(minutos / 60)
horas = float(horas)
minutos_restantes = minutos - horas * 60
print(f"{minutos} horas son {horas} horas y {minutos_restantes} minutos")

'''8.	Un vendedor recibe un sueldo base mas un 10% extra por comisión de sus ventas, 
el vendedor desea saber cuanto dinero obtendrá por concepto de comisiones por las tres 
ventas que realiza en el mes y el total que recibirá en el mes tomando en cuenta su 
sueldo base y comisiones.'''
sueldo_base = float(input("Ingrese su sueldo base: "))
sueldo_comision = sueldo_base * 0.30
sueldo_total = sueldo_comision + sueldo_base
print(f"Sueldo por comision de las tres ventas: {sueldo_comision}$")
print(f"Sueldo total del mes: {sueldo_total}$")

'''9. Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente desea 
saber cuanto deberá pagar finalmente por su compra.'''
compra = float(input("Ingrese el valor de la compra: "))
pago_final = compra * 0.85
print(f"Pagara finalmente con 15% de descuento {pago_final}$")

'''10.	Un alumno desea saber cual será su calificación final en la materia de Algoritmos. 
Dicha calificación se compone de los siguientes porcentajes:
•	    55% del promedio de sus tres calificaciones parciales.
•	    30% de la calificación del examen final.
•	    15% de la calificación de un trabajo final.
'''
parcial1 = float(input("Ingrese la nota del primer parcial: "))
parcial2 = float(input("Ingrese la nota del segundo parcial: "))
parcial3 = float(input("Ingrese la nota del tercer parcial: "))
examen_final = float(input("Ingrese la nota obtenida en el examen final: "))
trabajo_final = float(input("Ingrese la nota obtenida en el trabajo final: "))
nota_final = ((parcial1 + parcial2 + parcial3)/3) * 0.55 + examen_final * 0.3 + trabajo_final * 0.15
print(f"La calificacion final en la materia Algoritmos es de {nota_final}")

'''11.	Pide al usuario dos números y muestra la “distancia” entre ellos 
(el valor absoluto de su diferencia, de modo que el resultado sea siempre positivo).'''
print("A continuacion ingresara dos numeros para saber la distancia entre ellos")
numero1 = float(input("Ingrese un numero: "))
numero2 = float(input("Ingrese otro numero: "))
diferencia = numero1 - numero2
distancia = abs(diferencia)
print(f"La distancia entre los dos numeros es de {distancia}")

'''12.	Realizar un algoritmo que lea un número y que muestre su raíz cuadrada 
y su raíz cúbica.'''
numero = float(input("Ingrese un numero para saber su raiz cuadrada y su raiz cubica: "))
raiz_cuadrada = (numero) ** (1/2)
raiz_cubica = (numero) ** (1/3)
print(f"({numero}) ^ 1/2 = {raiz_cuadrada:.2f}")
print(f"({numero}) ^ 1/3 = {raiz_cubica:.2f}")


'''13.	Dado un número de dos cifras, diseñe un algoritmo que permita obtener el número 
invertido. Ejemplo, si se introduce 23 que muestre 32.'''
num_dos_cifras = float(input("Ingrese un numero de dos cifras: "))
num_dos_cifras = int(num_dos_cifras)
primera_cifra = int(num_dos_cifras/10)
segunda_cifra = num_dos_cifras % 10
print(f"El numero al revez es {segunda_cifra}{primera_cifra}")


'''14.	Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide realizar 
un algoritmo que intercambie los valores de ambas variables y muestre cuanto valen al 
final las dos variables.'''
a = float(input("Ingrese un numero: "))
b = float(input("Ingrese otro numero: "))
print(f"a = {a}, b = {b}")
auxiliar = b
b = a
a = auxiliar
print(f"Y ahora los valores son a = {a}, b = {b}")


'''15.	Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos. 
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos. 
Escribir un algoritmo que determine la hora de llegada a la ciudad B.
'''
hh = int(input("Ingrese la hora de partida de la ciudad A: "))
mm = int(input("Ingrese el minuto de partida: "))
ss = int(input("Ingrese el segundo de partida: "))
t = int(input("Ingrese los segundos de viaje hasta la ciudad B: "))
inicio_horas = hh + mm/60 + ss/3600
fin_horas = inicio_horas + t/3600
hora_fin = int(fin_horas)
print(f"La hora de llegada a la ciudad B va a ser a las {hora_fin} horas")


'''16.	Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.'''
nombre = input("Ingrese su nombre: ")
apellido1 = input("Ingrese su primer apellido: ")
apellido2 = input("Ingrese su segundo apellido: ")
inicial_nombre, inicial_apellido1, inicial_apellido2 = nombre[0], apellido1[0], apellido2[0]
print(f"La inicial de su nombre es {inicial_nombre}, del primer apellido {inicial_apellido1}, y del segundo {inicial_apellido2}")

'''17.	Solicitar al usuario que ingrese su nombre. El nombre se debe almacenar en una 
variable llamada usuario. A continuación mostrar por pantalla: 
“Ahora estás en la matrix, [nombre del usuario]”.'''
usuario = input("Ingrese su nombre: ")
print(f"Ahora estás en la matrix, [{usuario}]")


'''18.	Hacer un programa que solicite al usuario cuánto costó una cena en un restaurante. 
A ese valor, sumarle un 6.2% en concepto de servicio y un 10% de propina. 
Imprimir en pantalla el monto final a pagar.
'''
costo_cena = float(input("Ingrese cuanto costo la cena: "))
monto_final = costo_cena + costo_cena * 0.062 + costo_cena * 0.1
print(f"El monto final a pagar considerando servicio y propina es de {monto_final:.2f}$")

'''19.	Solicitar al usuario que ingrese el día, mes y año de su nacimiento y almacenar 
cada uno de ellos en una variable numérica (en total, tres variables diferentes). 
Finalmente, mostrar la fecha en formato dd/mm/aaaa.'''
dia = int(input("Ingrese el numero de su dia de nacimiento: "))
mes = int(input("Ingrese el numero de su mes de nacimiento: "))
anio = int(input("Ingrese su año de nacimiento: "))
print(f"Fecha de nacimiento: {dia}/{mes}/{anio}")


'''20.	Hacer otra versión del programa, pero esta vez almacenado todo en una única 
variable con formato DDMMAAA.'''
ddmmaa = int(input("Ingrese su fecha de nacimiento en forma numerica DDMMAAA: "))
digito1_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito2_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito3_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito4_anio = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito1_mes = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito2_mes = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito1_dia = str(ddmmaa % 10)
ddmmaa = int(ddmmaa / 10)
digito2_dia = str(ddmmaa)
anio = digito4_anio + digito3_anio + digito2_anio + digito1_anio
mes = digito2_mes + digito1_mes
dia = digito2_dia + digito1_dia
print(f"Su fecha de nacimiento es {dia}/{mes}/{anio}")


'''21.	Una pareja de motociclistas necesita hacer ciertos cálculos antes de emprender un 
viaje en moto, para saber cuántos tanques de combustible consumirá el viaje entero.
Para eso deben ingresar: cuántos kilómetros puede recorrer su moto con 1 litro de combustible,
 qué capacidad (en litros) tiene el tanque y cuántos kilómetros en total recorrerán.
Hacer un programa que solicite los datos necesarios y luego informe la cantidad de 
tanques de combustible necesarios.
'''
km_1litro = float(input("Ingrese la cantidad de kilometros que puede recorrer con un litro de combustible: "))
capacidad = float(input("Ingrese que capacidad tiene el tanque de combustible: "))
km_total = float(input("Ingrese cuantos kilometros en total recorreran: "))
cantidad_tanques = km_total / (km_1litro * capacidad)
print(f"La cantidad de tanques de combustibles necesarios es {cantidad_tanques}")

















