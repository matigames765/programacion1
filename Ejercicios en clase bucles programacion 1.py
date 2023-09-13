
'''1- Un grupo de amigos decide organizar un juego de estrategia, 
para lo cual forman dos equipos de 6
integrantes cada uno, donde un integrante de cada equipo es 
el “jefe” y los otros 5 son sus “oficiales”.
La regla más importante del juego es que sólo se comunicarán 
mediante un canal común, por lo que
deben buscar la forma de ocultar el contenido de sus mensajes. 
Uno de los equipos decide utilizar un
método antiguo de encriptación llamado “la cifra del césar”, 
que consiste en correr cada letra del
mensaje –considerando la posición de cada una en el alfabeto– 
una determinada cantidad de lugares.
Ejemplo: si el corrimiento es de 2 lugares, la palabra “ATAQUE” 
se transforma en “CVCSWG”.
Cada día, el “jefe” del equipo debe enviar un mensaje a cada 
uno de sus oficiales.
Escribir un programa que permita encriptar los 5 mensajes. 
El corrimiento (cantidad de lugares que se
correrán las letras) será dado por el usuario antes de 
comenzar a encriptar. Los 5 mensajes usarán el
mismo corrimiento.
Nota: si el alfabeto termina antes de poder correr la 
cantidad de lugares necesarios, se vuelve a
comenzar desde la letra “a”.
Ejemplo: la palabra “EXTRA” corrida 3 lugares se 
convierte en “HAWUD”. Utilizando el alfabeto
español, de 27 letras, el siguiente cálculo matemático permite volver 
a comenzar por el principio una
vez que se llegó a la “z”: (índice de la letra a correr+corrimiento)%27
Sólo se encriptarán las letras de los mensajes, dejando al resto de 
caracteres sin modificación.'''
mensaje1 = input("Jefe introduzca el mensaje para el oficial 1: ")
mensaje2 = input("Jefe introduzca el mensaje para el oficial 2: ")
mensaje3 = input("Jefe introduzca el mensaje para el oficial 3: ")
mensaje4 = input("Jefe introduzca el mensaje para el oficial 4: ")
mensaje5 = input("Jefe introduzca el mensaje para el oficial 5: ")
corrimiento = int(input("Ingrese el corrimiento que desea: "))
abecedario = "abcdefghijklmnñopqrstuvwxyz"
mensaje1n = ""
mensaje2n = ""
mensaje3n = ""
mensaje4n = ""
mensaje5n = ""
mensaje1 = mensaje1.lower()
mensaje2 = mensaje2.lower()
mensaje3 = mensaje3.lower()
mensaje4 = mensaje4.lower()
mensaje5 = mensaje5.lower()

for i in range(len(mensaje1)):
    if (mensaje1[i] in abecedario):
        for j in range(len(abecedario)):
            if (mensaje1[i] == abecedario[j]):
                mensaje1n = mensaje1n + abecedario[(j + corrimiento) % 27]
            else:
                pass
    else:
        mensaje1n = mensaje1n + mensaje1[i]

print(f"El nuevo primer mensaje es {mensaje1n}")

for i in range(len(mensaje2)):
    if (mensaje2[i] in abecedario):
        for j in range(len(abecedario)):
            if (mensaje2[i] == abecedario[j]):
                mensaje2n = mensaje2n + abecedario[(j + corrimiento) % 27]
            else:
                pass
    else:
        mensaje2n = mensaje2n + mensaje2[i]

print(f"El nuevo segundo mensaje es {mensaje2n}")

for i in range(len(mensaje3)):
    if (mensaje3[i] in abecedario):
        for j in range(len(abecedario)):
            if (mensaje3[i] == abecedario[j]):
                mensaje3n = mensaje3n + abecedario[(j + corrimiento) % 27]
            else:
                pass
    else:
        mensaje3n = mensaje3n + mensaje3[i]

print(f"El nuevo tercer mensaje es {mensaje3n}")

for i in range(len(mensaje4)):
    if (mensaje4[i] in abecedario):
        for j in range(len(abecedario)):
            if (mensaje4[i] == abecedario[j]):
                mensaje4n = mensaje4n + abecedario[(j + corrimiento) % 27]
            else:
                pass
    else:
        mensaje4n = mensaje4n + mensaje4[i]

print(f"El nuevo cuarto mensaje es {mensaje4n}")

for i in range(len(mensaje5)):
    if (mensaje5[i] in abecedario):
        for j in range(len(abecedario)):
            if (mensaje5[i] == abecedario[j]):
                mensaje5n = mensaje5n + abecedario[(j + corrimiento) % 27]
            else:
                pass
    else:
        mensaje5n = mensaje5n + mensaje5[i]

print(f"El nuevo quinto mensaje {mensaje5n}")

'''2- Crear un programa que solicite el ingreso de números enteros 
positivos, hasta que el usuario ingrese el
0. Por cada número, informar cuántos dígitos pares y cuántos 
impares tiene.
Al finalizar, informar la cantidad de dígitos pares y de 
dígitos impares leídos en total.'''

num = 4
contador_pares = 0
contador_impares = 0
contador_total_pares = 0
contador_total_impares = 0
while num != 0:
    num = int(input("Ingrese un entero positivo para seguir ingresando o 0 para finalizar: "))
    while True:
        if (num > 10):
            digito = num % 10
        else:
            digito = num
        if (digito % 2 == 0):
            contador_pares += 1
        else:
            contador_impares += 1
        if (num > 10):
            num = int(num / 10)
        else:
            break
    
    contador_total_pares = contador_total_pares + contador_pares
    contador_total_impares = contador_total_impares + contador_impares
    
    print(f"El numero tiene {contador_pares} digito/s par/es, y {contador_impares} digito/s impar/es")
    contador_pares = 0
    contador_impares = 0

print(f"La cantidad de digito/s par/es leidos en total fue {contador_total_pares} y impar/es {contador_total_impares}")





