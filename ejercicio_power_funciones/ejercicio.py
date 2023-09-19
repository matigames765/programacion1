import funciones
'''Solicitar números al usuario hasta que ingrese el cero. Por cada uno, 
mostrar la suma de sus dígitos.

Al finalizar mostrar la sumatoria de todos los números ingresados y 
la suma de sus dígitos.'''
total_numbers_addition = 0
number = int(input("Ingrese un numero para ver la suma de sus digitos o 0 para finalizar: "))

while number != 0:
    print(f"Suma de los digitos: {funciones.add(number)}")
    total_numbers_addition = total_numbers_addition + number
    number = int(input("Ingrese un numero para ver la suma de sus digitos o 0 para finalizar: "))

print(f"La sumatoria de todos los numeros ingresados es {total_numbers_addition}")
print(f"Y la sumatoria de sus digitos da {funciones.add(total_numbers_addition)}")