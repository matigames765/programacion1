'''1- Crear un programa que reciba el número de años que tiene nuestra computadora 
y muestre en la consola que el computador es nuevo si es menor o igual a 2 años y que
 el computador es viejo si es mayor a 2 años.'''
numeros_anios = int(input("Ingrese el numero de años que tiene la computadora: "))
if (numeros_anios <= 2):
    print("El computador es nuevo")
else:
    print("El computador es viejo")

'''2-	Hacer que el programa anterior muestre un mensaje de error si el usuario digita un 
número negativo.'''
numeros_anios = int(input("Ingrese los años que tiene el computador: "))
if (numeros_anios <= 2 and numeros_anios >= 0):
    print("El computador es nuevo")
elif (numeros_anios < 0):
    print("Error, no puede ingresar numeros negativos")
else:
    print("El computador es viejo")

'''3-	Solicitar al usuario que ingrese los nombres de dos personas, los cuales se 
almacenarán en dos variables. A continuación. Imprimir ‘coincidencia’ si ambos 
nombres comienzan con la misma letra. Si no es así, imprimir ‘no hay coincidencia’.'''
persona1 = input("Ingrese el nombre de la primera persona: ")
persona2 = input("Ingrese el nombre de la segunda persona: ")
persona1 = persona1.lower()
persona2 = persona2.lower()
if (persona1[0] == persona2[0]):
    print("coincidencia")
else:
    print("no hay coincidendia")

'''4-	Crear un programa que permita al usuario elegir un candidato por el cual votar. 
Las posibilidades son: candidato A por el partido rojo, candidato B por el partido verdad, 
candidato C por el partido azul.
Según el candidato elegido (A, B o C) se debe imprimir el mensaje: ‘Usted ha votado 
por el partido [color del candidato elegido].
Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos 
disponibles, indicar ‘Opción errónea.’
'''
candidato = input("Ingrese A para votar al partido rojo, B para el verdad, C para el azul: ")
candidato = candidato.lower()
if (candidato == "a"):
    print("Usted ha votado por el partido rojo")
elif (candidato == "b"):
    print("Usted ha votado por el partido verdad")
elif (candidato == "c"):
    print("Usted ha votado por el partido azul")
else:
    print("Opción errónea")

'''5-	Escribir un programa que solicite al usuario una letra, si es una vocal, 
mostrar el mensaje ‘Es vocal’.
Se debe validar que el usuario ingrese sólo un carácter. Si ingresa un string 
de más de un carácter, informarle que no se puede procesar el dato.
'''
letra = input("Ingrese una letra: ")
letra = letra.lower()
if (len(letra) == 1):
    if (letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u"):
        print("Es vocal")
    else:
        print("No es una vocal")
else:
    print("No se puede procesar un dato que no sea de un caracter")

'''6-	Hacer un programa que permita saber si un año es bisiesto. 
Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible 
por 100, excepto que también sea divisible por 400.'''
anio = int(input("Ingrese un año para saber si es o no bisiesto: "))
if (anio % 4 == 0 and anio % 100 != 0 and anio % 400 != 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")

'''7-	Escribí un programa para solicitar al usuario tres números y mostrar en pantalla 
al menor de los tres.'''
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el tercer numero: "))
num3 = int(input("Ingrese el tercer numero: "))
if (num1 < num2 and num1 < num3):
    print(f"El menor numero es el {num1}")
elif (num2 < num3):
    print(f"El menor numero es {num2}")
else:
    print(f"El menor numero es el {num3}")

'''8-	Escribí un programa que solicite ingresar un nombre de usuario y una contraseña. 
Si el nombre es “Gwenevere” y la contraseña es “excalibur”, mostrar en pantalla 
“Usuario y contraseña correctos. Puede ingresar a Camelot”. Si el nombre o 
la contraseña no coinciden, mostrar “Acceso denegado”.'''
nombre_usuario = input("Ingrese el nombre de usuario: ")
contrasenia = input("Ingrese la contraseña: ")
if (nombre_usuario == "Gwenevere" and contrasenia == "excalibur"):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")


'''9-	Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y 
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y 
los hombres con un nombre posterior a la N y el grupo B por el resto. 
Escribir un programa que pregunte al usuario su nombre y sexo, y muestre 
por pantalla el grupo que le corresponde.'''
nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo hombre/mujer: ")
nombre = nombre.upper()
sexo = sexo.lower()
if ((sexo == "mujer" and nombre[0] < "M") or (sexo == "hombre" and nombre[0] > "N")):
    print("Le corresponde el grupo A")
else:
    print("Le corresponde el grupo B")

'''10-	Escribir un programa para una empresa que tiene salas de juegos para todas las edades
 y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
 El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.
 Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años 
 debe pagar $500 y si es mayor de 18 años, $1000.'''
edad = int(input("Ingrese su edad: "))
if (edad < 4):
    print("Puede entrar gratis")
elif (edad >= 4 and edad < 18):
    print("Tiene que pagar $500")
else:
    print("Tiene que pagar $1000")


'''11-	La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
•	Ingredientes vegetarianos: Pimiento y tofu.
•	Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y 
en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas 
la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o 
no y todos los ingredientes que lleva.
'''

tipo_pizza = int(input("Ingrese 1 para pizza vegetariana o 2 para no vegetariana: "))
if (tipo_pizza == 1):
    print("La mozarella y el tomate viene con todas las pizzas")
    print("Menu con ingredientes:")
    print("_Pimiento")
    print("_Tofu")
    eleccion = input("Ingrese 1/1 si quiere ambos, 1/0 si solo pimiento, 0/1 solo tofu y 0/0 si ninguno: ")
    if (eleccion == "1/1"):
        print("Ingredientes: tomate, mozarella, pimiento, tofu")
    elif (eleccion == "1/0"):
        print("Ingredientes: tomate, mozarella, pimiento")
    elif (eleccion == "0/1"):
        print("Ingredientes: tomate, mozarella, tofu")
    else:
        print("Ingredientes: tomate y mozarella")
else:
    print("La mozarella y el tomate viene con todas las pizzas")
    print("Menu con ingredientes:")
    print("_Peperoni")
    print("_Jamon")
    print("_Salmon")
    eleccion = input("Ingrese cambiando las almohadillas #/#/# con 1 o 0 segun quiera el ingrediente o no: ")
    if (eleccion == "1/1/1"):
        print("Ingredientes: tomate, mozarella, peperoni, jamon, salmon")
    elif (eleccion == "1/1/0"):
        print("Ingredientes: tomate, mozarella, pimiento,jamon")
    elif (eleccion == "1/0/0"):
        print("Ingredientes: tomate, mozarella, pimiento")
    elif (eleccion == "0/1/0"):
        print("Ingredientes: tomate, mozarella, jamon")
    elif (eleccion == "0/0/1"):
        print("Ingredientes: tomate, mozarella, salmon")
    elif (eleccion == "0/1/1"):
        print("Ingredientes: tomate, mozarella, jamon, salmon")
    elif (eleccion == "1/0/1"):
        print("Ingredientes: tomate, mozarella, peperoni, salmon")
    else:
        print("Ingredientes: tomate y mozarella")

'''12-	Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos
años han pasado desde ese año o cuántos años faltan para llegar a ese año'''
anio_actual = int(input("Ingrese el año actual: "))
anio_cualquiera = int(input("Ingrese un año cualquiera: "))
if (anio_actual > anio_cualquiera):
    print(f"Han pasado {anio_actual - anio_cualquiera} años desde el {anio_cualquiera}")
else:
    print(f"Faltan {anio_cualquiera - anio_actual} años para llegar al {anio_cualquiera}")

'''13-	Escriba un programa que pida dos números enteros y que escriba si el mayor es
múltiplo del menor. Haciendo que el programa avise cuando se escriben valores negativos 
o nulos.'''
num1 = int(input("Ingrese un numero entero: "))
num2 = int(input("Ingrese otro numero entero: "))
if (num1 <= 0 or num2 <= 0):
    print("Se ingresaron valores negativos o nulos, no permitido")
else:
    if (num2 > num1):
        if (num2 % num1 == 0):
            print(f"{num2} es multiplo del {num1}")
        else:
            print(f"{num2} no es multiplo de {num1}")
    else:
        if (num1 % num2 == 0):
            print(f"El numero {num1} es multiplo del {num2}")
        else:
            print(f"El numero {num1} no es multiplo del {num2}")

'''14-	Escriba un programa que pida los coeficientes de una ecuación de primer grado 
(a x + b = 0) y escriba la solución.
Se recuerda que una ecuación de primer grado puede no tener solución, 
tener una solución única, o que todos los números sean solución. 
Se recuerda que la fórmula de las soluciones es 
x = -b / a
'''
a = float(input("Ingrese el coeficiente de la ecuacion de primer grado: "))
b = float(input("Ingrese el termino independiente de la ecuacion de primer grado: "))
if (a == 0 and b == 0):
    print("La ecuacion tiene infinitas soluciones")
elif (a == 0 and b != 0):
    print("La ecuacion no tiene solucion")
else:
    print(f"La solucion de la ecuacion es {-b / a}")

'''15-	Escriba un programa que pregunte primero si se quiere calcular el área de un 
triángulo o la de un círculo. Si se contesta que se quiere calcular el área de 
un triángulo (escribiendo T o t), el programa tiene que pedir entonces la base 
y la altura y escribir el área. Si se contesta que se quiere calcular 
el área de un círculo (escribiendo C o c), el programa tiene que pedir 
entonces el radio y escribir el área.
'''
import math

triangulo_circulo = input("Pulse (t o T) si quiere calcular el area de un triangulo o (c o C) de un circulo: ")
triangulo_circulo = triangulo_circulo.lower()
if (triangulo_circulo == "t"):
    base = float(input("Ingrese la base del triangulo: "))
    altura = float(input("Ingrese la altura del triangulo: "))
    area = (base * altura) / 2
    print(f"El area del triangulo es {area:.2f}")
else:
    radio = float(input("Ingrese el radio del circulo: "))
    area = math.pi * (radio ** 2)
    print(f"El area del circulo es {area:.2f}")

'''16-	Haz una calculadora básica pida al usuario dos valores, a y b.
Según la opción que desean, realizar la operación:
•	Si operación es 1 entonces debemos ver el resultado de a + b
•	Si operación es 2 entonces debemos ver el resultado de a * b
•	Si operación es 3 entonces debemos ver el resultado de a - b
•	Si operación es 4 entonces debemos ver el resultado de a / b
'''
a = float(input("Ingrese el primer operando: "))
b = float(input("Ingrese el primer operando: "))
operando = int(input("Ingrese 1 para realizar la suma, 2 multiplicacion, 3 resta o 4 division: "))
if (operando == 1):
    suma = a + b
    print(f"a + b = {suma}")
elif (operando == 2):
    multiplicacion = a * b
    print(f"a * b = {multiplicacion}")
elif (operando == 3):
    resta = a - b
    print(f"a - b = {resta}")
else:
    division = a / b
    print(f"a / b = {division}")

'''17-	Requerir al usuario que ingrese un día de la semana e imprimir un mensaje si es 
lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o 
domingo. Si el día ingresado no es ninguno de esos, imprimir otro mensaje.'''
dia_semana = input("Ingrese un dia de la semana: ")
dia_semana = dia_semana.lower()
if (dia_semana == "lunes"):
    print("Falta mucho para el fin de semana")
elif (dia_semana == "viernes"):
    print("Que lindo comienza el fin de semana")
elif (dia_semana == "sabado"):
    print("El mejor dia de la semana")
elif (dia_semana == "domingo"):
    print("Buen dia para comer en familia")
else:
    print("Lamentablemente no tengo mensaje para este dia")

'''18-	Preguntar al usuario el total de horas trabajadas en el mes y el salario por hora.
La jornada de trabajo mínima es de 48 horas. Calcular, dadas las horas trabajadas, 
si trabajó horas extras y mostrar esta cantidad.
Mostrar su salario total, tomando en cuenta que las horas extras serán pagadas 
un 10% más que las horas laborales comunes.
'''
horas_mes = int(input("Ingrese el total de horas trabajadas en el mes: "))
salario_hora = int(input("Ingrese su salario por hora: "))
if (horas_mes > 48):
    horas_extra = horas_mes - 48
    print(f"Las horas extras trabajadas fueron {horas_extra}")
    salario_total = salario_hora * 48 + horas_extra * (salario_hora * 1.10)
    print(f"Su salario total contando las horas extras es de ${salario_total:.2f}")
else:
    salario_total = horas_mes * salario_hora
    print(f"No hizo horas extra, su salario total es ${salario_total}")

'''19-	Determinar cuánto se debe pagar por una cantidad de lápices considerando que si 
son 1000 o más, existe un descuento de 7% y teniendo en cuenta que el costo por lápiz 
es de $60; de lo contrario no hay descuento.'''
cantidad_lapices = int(input("Ingrese la cantidad de lapices que va a comprar: "))
if (cantidad_lapices >= 1000):
    pago = cantidad_lapices * 60
    pago_descuento = pago * 0.93
    print(f"La cantidad a pagar con descuento del 7% es ${pago_descuento:.2f}")
else:
    pago = cantidad_lapices * 60
    print(f"El monto a pagar sin descuento es de ${pago}")

'''20-	Determinar si un alumno aprueba o reprueba un curso, sabiendo que aprobara 
si su promedio de cuatro (4) notas, es mayor o igual a 6; caso contrario 
saldrá desaprobado.'''
nota1 = float(input("Ingrese la primer nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercer nota: "))
nota4 = float(input("Ingrese la cuarta nota: "))
promedio = (nota1 + nota2 + nota3 + nota4) / 4
if (promedio >= 6):
    print("Esta aprobado")
else:
    print("Esta desaprobado")