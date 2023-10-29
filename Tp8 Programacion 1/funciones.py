'''1.	Escribir una función que reciba un número positivo n y devuelva 
la cantidad de dígitos que tiene.'''

def count_digits(number,digits):
    if (number == 0):
        return digits
    else:
        digits += 1
        return count_digits(number // 10,digits)

'''2. Escribir una función que reciba 2 enteros n y b y devuelva True 
si n es potencia de b.'''

def pow(n,b):
    if (n == 1):
        return True
    elif (n < b):
        return False
    else:
        return pow(n / b, b)

'''3.	Escribir una funcion recursiva que reciba como parámetros dos 
strings a y b, y devuelva una lista con las posiciones en donde se 
encuentra b dentro de a.'''

def function_positions(a,b,positions,i,comparison_b):
    if (i == len(a)):
        return positions
    else:
        for j in range(i,len(a)):
            if (b[0] == a[i]):
                for h in range(j,j + (len(b) - 1)):
                    comparison_b += positions[h]
            if (comparison_b == b):
                positions.append(j)
        comparison_b = ""
        return(a,b,positions,i + 1,comparison_b)
                    


'''4.	Escribir dos funciones mutualmente recursivas par(n) e impar(n) 
que determinen la paridad del numero natural dado, conociendo solo 
que:
•	1 es impar.
•	Si un número es impar, su antecesor es par; y viceversa.
'''
def function_even(number):
    if (number == 1):
        return False
    else:
        return function_odd(number - 1)

def function_odd(number):
    if (number == 1):
        return True
    else:
        return function_even(number - 1)

'''5.	Escribir una función recursiva que encuentre el mayor elemento de 
una lista.'''

def greater_function(greater_list,i,greater_num):
    if (i == len(greater_list) - 1):
        if (greater_num < greater_list[i]):
            greater_num = greater_list[i]
        else:
            pass
        return greater_num
    else:
        if (greater_num < greater_list[i]):
            greater_num = greater_list[i]
        else:
            pass
        return greater_function(greater_list,i + 1,greater_num)

'''6.	Escribir una función recursiva para replicar los elementos de una 
lista una cantidad n de veces. Por ejemplo, replicar ([1, 3, 3, 7], 2) 
= ([1, 1, 3, 3, 3, 3, 7, 7])'''

def function_replicate_list(replicate_list,n,list_new,i):
    if (i == len(replicate_list)):
        return list_new
    else:
        for j in range(n):
            list_new.append(replicate_list[i])
        return function_replicate_list(replicate_list,n,list_new,i + 1)

'''7.	Implemente un algoritmo, usando una función recursiva, que resuelva la siguientesumatoria:
K(n, p) = p + 2 ∗ p + 3 ∗ p + 4 ∗ p + … + n ∗ p
● El programa debe pedir al usuario que ingrese un número n, y un número d,
● Luego debe calcular el valor de K(n, p) usando una función recursiva,
● Debe imprimir el resultado de K(n, p)'''

def K(n,p):
    if (n == 1):
        return p
    else:
        return n * p + K(n - 1,p)

#ejercicio_8
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n - 1, k - 1) + pascal(n - 1, k)
    
#ejercicio_9
def combinations(c_list, k, actual="", result=[]):
    if k == 0:
        result.append(actual)
        return

    for caracter in c_list:
        combinations(c_list, k - 1, actual + caracter, result)

#ejercicio_10

def sheet_measure(sheet_n):
    if sheet_n == 0:
        return (841, 1189)  # Hoja A0
    else:
        previous_width, previous_length = sheet_measure(sheet_n - 1)
        new_width = previous_length
        new_length = previous_width / 2
        return (new_width, new_length)






    



    
    
    