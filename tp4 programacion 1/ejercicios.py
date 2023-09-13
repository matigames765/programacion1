'''1. Create a while loop with the following characteristics:

• The initial value of the variable x will be 0.
• The increment value will be 1.
• The exit condition of the loop will be greater than or equal to 30.
• The execution must be broken when x is equal to 15.
• You must print the following sentence each time the loop executes: 
'The value of the loop is: ' + x.
• You must skip the executions with the value of x in 4, 6 and 10.
• At each execution jump, you must display the jumped values with this 
message: 'The value ' + x ' of x was skipped'.
• When the execution of the loop is broken, you must show a message 
indicating it: 'The execution of the loop was broken when x was ' + x.
'''
x = 0
while x <= 30:
    x += 1
    if (x == 15):
        print(f"The execution of the loop was broken when x was {x}")
        break
    elif (x == 4 or x == 6 or x == 10):
        print(f"The value {x} of x was skipped")
        continue
    else:
        pass
    print(f"The value of the loop is: {x}")

'''2.	Escriba un programa que acepte una secuencia de líneas e imprima 
todas las líneas convertidas en mayúsculas. Deje una línea en blanco para 
indicar que ha finalizado la entrada de líneas.'''
lines = []
while True:
    line = input("Ingrese una linea para convertir a mayuscula o una misma vacia para finalizar: ")
    if (line != ""):
        lines.append(line)
    else:
        break
for i in range(len(lines)):
    print(f"linea {i + 1} en mayusculas: {lines[i].upper()}")
'''3.	Escriba un programa que administre una cuenta bancaria, 
usando una bitácora de operaciones.
La bitácora de operaciones tiene la siguiente forma:
D 100
R 50

D 100 significa que depositó 100 pesos
R 50 significa que retiró 50 pesos

Ejemplo de una entrada:
D 200
D 200
R 100
D 50
Introducir una línea vacía indica que ha finalizado la bitácora.
La salida de éste programa sería:
350
'''
total_money_in_account = 0
while True:
    deposit_withdrawal = input("Ingrese D $ para depositar, R $ para retirar y linea vacia para finalizar: ")
    if (deposit_withdrawal == ""):
        print("Finalizada la bitacora")
        break
    elif (deposit_withdrawal[0] == "R"):
        if (total_money_in_account == 0):
            print("No puede retirar, no tiene monto en la cuenta")
        else:
            total_money_in_account = total_money_in_account - int(deposit_withdrawal[2:])
    else:
        total_money_in_account = total_money_in_account + int(deposit_withdrawal[2:])
print(f"Dinero en la cuenta bancaria: ${total_money_in_account}")
    

'''4.	Escribir un programa que solicite el ingreso de una cantidad 
indeterminada de números mayores que 1, finalizando cuando se 
reciba un cero.
Imprimir la cantidad total de números primos ingresados.
Nota: Un número primo es un número natural mayor que 1 que tiene 
únicamente dos divisores distintos: él mismo y el 1.
'''
prime_number_counter = 0
divisor_counter = 0
while True:
    number = int(input("Ingrese numeros mayores que 1 o 0 para finalizar: "))
    if (number == 0):
        break
    elif (number != 0):
        for i in range(1,number + 1):
            if (number % i == 0):
                divisor_counter += 1
            else:
                pass
        if (divisor_counter == 2):
            prime_number_counter += 1
        else:
            pass
        divisor_counter = 0
    else:
        pass
print(f"La cantidad de numeros primos ingresados fue {prime_number_counter}")

'''5.	Escribir un programa que permita al usuario ingresar dos años y 
luego imprima todos los años en ese rango, que sean bisiestos y múltiplos 
de 10.
Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe 
ser divisible por 100, excepto que también sea divisible por 400.
'''
year1 = int(input("Ingrese el primer año: "))
year2 = int(input("Ingrese el segundo año: "))
for i in range(year1, year2 + 1):
    if (i % 10 != 0):
        continue
    elif (i % 4 != 0):
        continue
    elif (i % 100 != 0 or i % 400 == 0):
        print(f"El año {i} es bisiesto")
    else:
        pass
'''6.	Escribe un programa que imprima todos los números pares del 1 al 
20 usando un bucle for. Utiliza la declaración continue para omitir 
los números impares.'''
for i in range(1,21):
    if (i % 2 != 0):
        continue
    print(i)

'''7.	Crea una lista de números y utiliza un bucle for para encontrar 
un número específico. Cuando encuentres el número, usa break para salir 
del bucle'''
listt = []
list_numbers = int(input("Ingrese la cantidad de numeros que va a ingresar a la lista: "))
for i in range(list_numbers):
    number_list = int(input(f"Ingrese el elemento(numero) {i+1} a la lista: "))
    listt.append(number_list)

number = int(input("Ingresa el numero a encontrar: "))
for i in range(list_numbers):
    if (listt[i] == number):
        print(f"Encontre el numero!")
        break
'''8.	Crea un programa que muestre un menú de opciones 
(por ejemplo, opciones 1, 2, 3). Utiliza un bucle while para permitir 
al usuario seleccionar una opción. Si el usuario ingresa "0", 
utiliza break para salir del bucle (Mostrar un mensaje por cada 
opción elegida).'''
while True:
    print("Menu de 3 opciones:\nopcion 1\nopcion 2\nopcion 3")
    option = int(input("Ingrese 1 para opcion 1, 2 para la 2, 3 para la 3 o 0 para finalizar: "))
    if (option == 1):
        print("Eligio la opcion 1")
    elif (option == 2):
        print("Eligio la opcion 2")
    elif(option == 3):
        print("Eligio la opcion 3")
    else:
        print("Finalizando...")
        break

