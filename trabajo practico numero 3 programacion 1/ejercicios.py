'''1-	Escribir un programa que pida al usuario una palabra y la muestre 
por pantalla 10 veces.'''
word = input("Ingrese una palabra: ")
for i in range(10):
    print(word)

'''2-	Escribir un programa que pregunte al usuario su edad y muestre por 
pantalla todos los años que ha cumplido (desde 1 hasta su edad).'''
age = int(input("Ingrese su edad: "))
print("Los años que ha cumplido hasta el actual son: ")
for i in range(1,age + 1):
    print(f"años: {i}")

'''3-	Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla todos los números impares desde 1 hasta ese número 
separados por comas.'''
number = int(input("Ingrese un numero entero positivo: "))
print("Mostraremos los impares hasta ese numero:")
for i in range(number + 1):
    if (i % 2 != 0):
        if (i == number - 1 or i == number):
            print(i,end = "")
        else:
           print(f"{i},",end = "")

'''4-	Escribir un programa que pida al usuario un número entero positivo 
y muestre por pantalla la cuenta atrás desde ese número hasta cero 
separados por comas.'''
number = int(input("Ingrese un entero positivo: "))
print("Mostraremos la cuenta hacia atras hasta 0 desde es numero:")
for i in range(number,-1,-1):
    if (i == 0):
        print(i, end = "")
    else:
        print(f"{i},", end = "")

'''5-	Escribir un programa que pregunte al usuario una 
cantidad a invertir,
el interés anual y el número de años, y muestre por pantalla el capital 
obtenido en la inversión cada año que dura la inversión.'''
invest_amount = float(input("Ingrese una cantidad a invertir: "))
annual_interest = float(input("Ingrese el interes anual: "))
years = int(input("Ingrese la cantidad de años: "))
capital_obtained = invest_amount
for i in range(1,years + 1):
    capital_obtained = capital_obtained + (invest_amount * (annual_interest / 100))
    print(f"El capital obtenido en el/hasta el año {i}, es de ${capital_obtained}")
    invest_amount = capital_obtained

'''6-	Escribir un programa que pida al usuario un número entero y muestre
por pantalla un triángulo rectángulo como el de más abajo, de altura 
el número introducido.
'''
number = int(input("Ingrese un numero entero positivo: "))
print("Vera un triangulo rectangulo de esa altura")
for i in range(1,number + 1):
    print("*" * i)

''' 7-	Escribir un programa que muestre por pantalla las tablas de 
multiplicar del 1 al 10.
'''
print("Vera las tablas de multiplicar del 1 al 10")
for i in range(10):
    for j in range(10):
        print(f"{i + 1} x {j + 1} = {(i + 1) * (j + 1)}")

'''8-	Escribir un programa que pida al usuario un número entero y muestre 
por pantalla un triángulo rectángulo como el de más abajo.'''
number = int(input("Introduce un numero entero positivo: "))
print("Veras un triangulo rectangulo con esa altura y con numeros impares")
for i in range(1,number * 2,2):
    for j in range(i,0,-2):
        print(j,end = " ")
    print("")

'''9-	Escribir un programa que almacene la cadena de caracteres contraseña 
en una variable, pregunte al usuario por la contraseña hasta 
que introduzca la contraseña correcta.'''
password = input("Introduzca su nueva contraseña, debe contener mas de 4 caracteres: ")
enter_password = "ugu"
while password != enter_password:
    enter_password = input("Ingrese su contraseña: ")
print("Contraseña correcta!")

'''10-	Escribir un programa que pida al usuario un número entero y muestre
por pantalla si es un número primo o no.'''
number = int(input("Ingrese un numero entero para saber si es o no primo: "))
dividers_counter = 0
for i in range(number + 1):
    if (number % (i+1)) == 0:
        dividers_counter += 1
if (dividers_counter == 2):
    print(f"El numero {number} es un numero primo")
else:
    print(f"El numero {number} no es primo")


'''11-	Escribir un programa que pida al usuario una palabra y luego 
muestre por pantalla una a una las letras de la palabra introducida 
empezando por la última.'''
word = input("Ingrese una palabra: ")
large = len(word)
print("Las letras de la palabra empezando por la ultima son")
for i in range(len(word) - 1,-1,-1):
    print(word[i], end = " ")


'''12-	Escribir un programa en el que se pregunte al usuario por una frase
y una letra, y muestre por pantalla el número de veces que aparece la 
letra en la frase.
'''
phrase = input("Introduzca una frase: ")
letter = input("Introduzca una letra para saber la cantidad de veces que aparece en la frase: ")
appearances = 0
phrase = phrase.lower()
letter = letter.lower()
for i in range(len(phrase)):
    if letter == phrase[i]:
        appearances += 1
print(f"La letra {letter} aparece {appearances} veces en la frase")

'''13-	Escribir un programa que muestre el eco de todo lo que el usuario 
introduzca hasta que el usuario escriba “salir” que terminará.'''
while True:
    eco = input("Introduzca algo o salir si quiere hacerlo: ")
    if (eco.lower() == "salir"):
        break
    print(eco)

'''14-	Escriba un programa que pida dos números enteros y escriba qué 
números son pares y cuáles impares desde el primero hasta el segundo.'''
first = int(input("Introduzca el primer numero: "))
second = int(input("Introduzca el segundo numero: "))
for i in range(first,second + 1):
    if (i % 2 == 0):
        print(f"{i} es par")
    else:
        print(f"{i} es impar")

'''15-	Escriba un programa que pida un número entero mayor que cero y 
que escriba sus divisores.'''
number = int(input("Ingrese un numero entero mayor que cero: "))
print(f"Los divisores de {number} son: ")
for i in range(number + 1):
    if ((number % (i + 1) == 0)):
        print(i + 1)

'''16-	Escriba un programa que pregunte cuántos números se van a 
introducir, pida esos números y escriba cuántos negativos 
ha introducido.'''
numbers_amount = int(input("¿Cuantos numeros vas a introducir?: "))
negative_counter = 0
for i in range(numbers_amount):
    number = int(input(f"Ingrese el numero {i + 1}: "))
    if (number < 0):
        negative_counter += 1
print(f"Introdujo {negative_counter} numeros negativos")

'''17-	Solicitar al usuario que ingrese una frase y luego imprimir 
un listado de las vocales que aparecen en esa frase (sin repetirlas).
'''
phrase = input("Ingrese una frase: ")
print("Listado de vocales que aparecen en la frase:")
cont_a = 0
cont_e = 0
cont_i = 0
cont_o = 0
cont_u = 0
for i in range(len(phrase)):
    if (phrase[i].lower() == "a" and cont_a == 0):
        print("a")
        cont_a += 1
    elif (phrase[i].lower() == "e" and cont_e == 0):
        print("e")
        cont_e += 1
    elif (phrase[i].lower() == "i" and cont_i == 0):
        print("i")
        cont_i += 1
    elif (phrase[i].lower() == "o" and cont_o == 0):
        print("o")
        cont_o += 1
    elif (phrase[i].lower() == "u" and cont_u == 0):
        print("u")
        cont_u += 1
    else:
        pass

'''18-	Crear un algoritmo que muestre los primeros 10 números de la 
sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 
y, a partir de éstos, cada elemento es la suma de los dos números 
anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…'''
list_sucession = []
for i in range(10):
    if (i == 0 or i == 1):
        print(i,", ",end = "")
        list_sucession.append(i)
    elif (i == 9):
        print(f"{list_sucession[i - 1] + list_sucession[i - 2]}")
    else:
        print(f"{list_sucession[i - 1] + list_sucession[i - 2]},", end = " ")
        list_sucession.append(list_sucession[i - 1] + list_sucession[i - 2])

'''
19-	Escriba un programa que simule una alcancía. El programa solicitará 
primero una cantidad, que será la cantidad de dinero que queremos ahorrar. 
A continuación, el programa solicitará una y otra vez las cantidades 
que se irán ahorrando, hasta que el total ahorrado iguale o supere 
al objetivo. El programa deberá comprobar que las cantidades 
ingresadas sean positivas.
'''
save_amount = float(input("Ingrese la cantidad de dinero que quiere ahorrar: "))
total_amount = 0
while total_amount < save_amount:
    amount = float(input("Ingrese lo que ha ahorrado: "))
    if (amount < 0):
        print("No puede ingresar cantidades negativas")
    else:
        total_amount += amount
print(f"Objetivo alcanzado!, ahorro ${total_amount}")

'''20-	Leer números enteros de teclado, hasta que el usuario ingrese el 0. 
Finalmente, mostrar la sumatoria de todos los números ingresados.'''
addition = 0
number = 4
while number != 0:
    number = int(input("Ingrese numeros enteros para sumar y 0 para finalizar: "))
    addition += number
print(f"La suma dio {addition}")

'''21-	Leer números enteros positivos de teclado, hasta que el usuario 
ingrese el 0. Informar cuál fue el mayor número ingresado.'''
number = 6
print("Ingresaras numeros enteros positivos para ver cual es el mayor")
counter_iterations = 0
while number != 0:
    number = int(input("Ingrese enteros positivos o 0 para finalizar: "))
    counter_iterations += 1
    if (number == 0):
        break
    elif (counter_iterations == 1):
        elderly = number
    else:
        if (number > elderly):
            elderly = number
print(f"El mayor numero ingresado fue {elderly}")

'''22-	Solicitar al usuario que ingrese números enteros positivos y, 
por cada uno, imprimir la suma de los dígitos que lo componen. 
La condición de corte es que se ingrese el número -1. Al finalizar,
mostrar cuántos de los números ingresados por el usuario fueron 
números pares.'''
even_number_counter = 0
while True:
    addition = 0
    number = int(input("Ingrese enteros positivos o -1 para finalizar: "))
    if (number % 2 == 0):
        even_number_counter += 1
    else:
        pass
    if (number == -1):
        print("Finalizando...")
        break
    else:
        while number > 0:
            if (number < 10):
                digit = number
                addition += digit
                number = int(number / 10)
            else:
                digit = number % 10
                addition += digit
                number = int(number / 10)
        print(f"La suma de los digitos del numero {number} es {addition}")
print(f"Ingreso {even_number_counter} numeros pares")

'''23-	Crear un programa que permita al usuario ingresar los montos de las
compras de un cliente (se desconoce la cantidad de datos que cargará, 
la cual puede cambiar en cada ejecución), cortando el ingreso de datos 
cuando el usuario ingrese el monto 0.'''
buys = 0
total_amount = 0
while True:
    buys += 1
    amount = float(input(f"Ingrese el monto de la compra {buys}, ingrese 0 para finalizar: "))
    if (amount == 0):
        print("Finalizando...")
        break
    else:
        total_amount += amount
print(f"El monto total de la compra fue de ${total_amount}")

'''24-	Si ingresa un monto negativo, no se debe procesar y se debe pedir 
que ingrese un nuevo monto. Al finalizar, informar el total a pagar 
teniendo que cuenta que, si las ventas superan el total de $1000, 
se le debe aplicar un 10% de descuento.
'''
buys = 0
total_amount = 0
while True:
    buys += 1
    amount = float(input(f"Ingrese el monto de la compra {buys}, ingrese 0 para finalizar: "))
    if (amount == 0):
        print("Finalizando...")
        break
    elif (amount < 0):
        print("No puede ingresar montos negativos")
    else:
        total_amount += amount
if (total_amount > 1000):
    print("Por superar el monto de $1000 se la aplicara un 10% de descuento")
    total_amount = total_amount * 0.90
    print(f"Monto total a pagar: ${total_amount}")
else:
    print(f"El monto total de la compra fue de ${total_amount}")

'''25-	Dado un número entero positivo, mostrar su factorial. 
El factorial de un número se obtiene multiplicando todos los números 
enteros positivos que hay entre el 1 y ese número. El factorial de 0 es 1.'''
number = int(input("Ingrese un entero positivo para ver su factorial: "))
factorial = 1
if (number == 0):
    print("0! = 1")
else:
    for i in range(number,0,-1):
        factorial = factorial * i
    print(f"{number}! = {factorial}")











