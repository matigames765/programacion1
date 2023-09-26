import random
#funcion para elegir palabra
def word_choose(hanged_list):
    return hanged_list[random.randint(0,len(hanged_list) - 1)]
#funcion para generar los espacios de la palabra a adivinar
def generate_spaces(choose_word):
    guess = ""
    for i in range(len(choose_word)):
        guess += "_"
    return guess
#Funcion para comprobar si la letra esta en la palabra
def letter_in_word(letter,choose_word):
    if (letter in choose_word):
        return True
    else:
        return False
#Funcion para rellenar los espacios con la letra adivinada
def update_guess_word(letter_guess,choose_word,guess_wordd):
    print("La letra se encuentra en la palabra!")
    word_guess = ""
    for i in range(len(choose_word)):
        if (letter_guess == choose_word[i]):
            word_guess += letter_guess
        else:
            word_guess += guess_wordd[i]
    return word_guess
#Funcion para validar la letra a adivinar ingresada
def validation_letter():
    letter = "aa"
    while len(letter) != 1:
        letter = input("Introduzca la letra a adivinar: ")
        if (len(letter) != 1):
            print("No esta ingresando solo una letra, vuelva a ingresar")
        else:
            pass
    return letter
