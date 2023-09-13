import random
'''Este ejercicio se realiza en grupo, pero la entrega es individual.

Crear un programa utilizando todo lo aprendido hasta el momento.

Condicionales
Iteraciones (for / while)
Break / Continue
'''
'''El programa consiste en adivinar un numero entre 0 y 100 que la computadora tiene y 
para entrar el usuario debera ingresar cualquier palabra que sea un
palindromo'''
#Con este while pedimos al usuario que vaya ingresando palindromos para poder ingresar al juego
while True:
    word = input("Para jugar ingrese un palindromo cualquiera o ingrese 0 para finalizar: ")
    equals_letter_counter = 0
    reverse_word = ""
    #Aca se va a validar la palabra
    if (word != "0"):
        #Con este condicional verificamos que no ingrese un solo caracter
        if (len(word) > 2):
            pass
        else:
            print("La palabra no puede tener menos de 3 caractereres")
            continue
        #Con este for generamos la palabra al revez para ver si es un palindromo
        for i in range(len(word) - 1,-1,-1):
            reverse_word += word[i]
        #Si es un palindromo entonces ingresamos al juego
        if (reverse_word == word):
            print("Muy bien la palabra es un palindromo, puedes entrar al juego!")
            random_number = random.randint(0,100)
            attemps = 0
            print("Vas a tener 5 intentos para adivinar el numero si no perderas")
            #El usuario ingresara numeros entre 0 y 100 hasta adivinar
            while True:
                if (attemps < 5):
                    user_number = int(input("Ingrese un numero entre 0 y 100 para adivinar: "))
                    attemps += 1
                    if (random_number > user_number):
                        print("El numero es mayor!")
                    elif (random_number < user_number):
                        print("El numero es menor!")
                    else:
                        print("Felicitaciones, adivinaste el numero!")
                        break
                else:
                    print("Se acabaron los intentos, perdiste :(")
                    break
        else:
            print("La palabra no es un palindromo, deberas volver a ingresar otra")
    else:
        #Si el usuario ingresa un 0 salimos del bucle
        print("Finalizando...")
        break

           
        
    