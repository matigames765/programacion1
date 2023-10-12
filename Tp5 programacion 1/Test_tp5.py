import pytest
from funciones import *

'''Escribir una función que, dado un número de DNI, retorne True si 
el número es válido y False si no lo es. Para que un número de DNI sea 
válido debe tener entre 7 y 8 dígitos.'''
@pytest.mark.parametrize("dni, res",[("1234567",True),("123456",False),("12345678",True),])
def test_dni_valido(dni, res):
    assert dni_valido(dni) == res

'''Escribir una función que, dado un string, retorne la longitud de 
la última palabra. Se considera que las palabras están separadas por uno 
o más espacios. También podría haber espacios al principio o al final 
del string pasado por parámetro.'''

@pytest.mark.parametrize("string, res",[("hola mati",4),("buenos diass",5),("hola wey ",3)])
def test_calculate_lenght(string, res):
    assert calculate_lenght(string) == res

'''3.	Escribir un programa que permita al usuario obtener un 
identificador para cada uno de los socios de un club. Para eso 
ingresará nombre completo y número de DNI de cada socio, 
indicando que finalizará el procesamiento mediante el ingreso 
de un nombre vacio.
Precondición: el formato del nombre de los socios será: nombre 
apellido. Podría ingresarse más de un nombre, en cuyo caso será: 
nombre1, nombre2, apellido. Si un socio tuviera más de un apellido, 
el usuario solo ingresará uno.
Se debe validar que el número de DNI tenga 7 u 8 dígitos. En caso 
contrario, el programa debe dejar al usuario en un bucle hasta que 
ingrese un DNI correcto.
Por cada socio se debe imprimir su identificador único, el cual estará 
formado por: el primer nombre, la cantidad de letras del apellido y los 
3 primeros dígitos de su DNI. Ejemplo:
Nombre: María Ines Rosales
DNI: 25469648
ID -> Maria7254'''

@pytest.mark.parametrize("name, dni, res",[("Matias Games", "43684089", "Matias5436"),("Matias Gabriel Gamess", "12345678", "Matias6123")])
def test_identifier(name, dni, res):
   assert identifier(name, dni) == res

'''4.	Crea un programa que pida dos número enteros al usuario y diga si 
alguno de ellos es múltiplo del otro. Crea una función que reciba los dos 
números, y devuelve si el primero es múltiplo del segundo.'''

@pytest.mark.parametrize("number1, number2, res",[(6,3,True),(6,5,False)])
def test_multiples(number1, number2, res):
    assert multiples(number1, number2) == res

'''5.	Crear una función que calcule la temperatura media de un día a 
partir de la temperatura máxima y mínima. Crear un programa principal, 
que utilizando la función anterior, vaya pidiendo la temperatura máxima y 
mínima de cada día y vaya mostrando la media. El programa pedirá el 
número de días que se van a introducir.'''

@pytest.mark.parametrize("max_temp, min_temp, res",[(40,20,30.0),(25.5,14.5,20.0)])
def test_half_temp(max_temp, min_temp, res):
    assert half_temp(max_temp, min_temp) == res

'''6.	Crea una función que reciba como parámetro un texto y devuelve una
cadena con un espacio adicional tras cada letra. Por ejemplo, “Hola, tú” 
devolverá “H o l a , t ú “. Crea un programa principal donde se use dicha
función.'''

@pytest.mark.parametrize("text, res",[("Hola, Matias","H o l a , M a t i a s "),("Soy Joaquin","S o y  J o a q u i n ")])
def test_space_text(text, res):
    assert space_text(text) == res

'''7.	Crea una función que recibe una lista con valores numéricos y 
devuelve el valor máximo y el mínimo. Crea un programa que pida números 
por teclado y muestre el máximo y el mínimo, utilizando la función 
anterior.'''

@pytest.mark.parametrize("number_list, res",[([1,2,4,5,3],(5,1)),([40,50,35,60,20],(60,20))])
def test_max_min(number_list, res):
    assert max_min(number_list) == res

'''8.	Diseñar una función que calcule el área y el perímetro de una 
circunferencia. Utiliza dicha función en un programa principal que lea 
el radio de una circunferencia y muestre su área y perímetro.'''

tolerance = 1.0e-2
@pytest.mark.parametrize("radio, res",[(20,(1256.63,125.66)),(35,(3848.45,219.91))])
def test_area_perimeter(radio, res):
    assert area_perimeter(radio) == pytest.approx(res, abs = tolerance)

'''9.	Crear una subrutina llamada “login”, que recibe un nombre de 
usuario y una contraseña y te devuelve Verdadero si el nombre de usuario 
es “usuario1” y la contraseña es “asdasd”. Además recibe el número de 
intentos que se ha intentado hacer login y si no se ha podido hacer login 
incremente este valor.
Crear un programa principal donde se pida un nombre de usuario y una 
contraseña y se intente hacer login, solamente tenemos tres oportunidades 
para intentarlo.'''

@pytest.mark.parametrize("user_name, password, attempts, res",[("usuario1","sfss",1,(False,2)),("dasjd","asdasd",2,(False,3)),("usuario1","asdasd",0,(True,1))])
def test_login(user_name, password, attempts, res):
    assert login(user_name, password, attempts) == res

'''10.	Escribir una función que aplique un descuento a un precio. Esta 
función tiene que recibir un diccionario con los precios y porcentajes 
del carrito de compra, aplicar los descuentos a los productos del carrito
y devolver el precio final de la compra.'''

@pytest.mark.parametrize("prize, discountt, res",[(400,50,200.0),(100,80,20.0)])
def test_discount(prize, discountt, res):
    assert discount(prize, discountt) == pytest.approx(res, abs = tolerance)

'''11.	Escribir una función que reciba otra función y una lista, y 
devuelva otra lista con el resultado de aplicar la función dada a cada 
uno de los elementos de la lista.'''

@pytest.mark.parametrize("listtt, res",[([4,5,7,4,6],[5,6,8,5,7]),([8,7,90,45,7],[9,8,91,46,8])])
def test_list_new(listtt, res):
    assert list_new(listtt) == res

'''12.	Escribir una función que reciba una frase y devuelva un diccionario
con las palabras que contiene y su longitud.'''

@pytest.mark.parametrize("phrase, res",[("hola soy mati",{"hola":4,"soy":3,"mati":4}),("jugar al pacman bien",{"jugar":5,"al":2,"pacman":6,"bien":4})])
def test_lenght_dictionarie(phrase, res):
    assert lenght_dictionarie(phrase) == res

'''13.	Escribir una función que calcule el módulo de un vector.'''
@pytest.mark.parametrize("vector, res",[(6 + 8j,10.0),(5 + 12j,13.0)])
def test_module(vector, res):
    assert module(vector) == res

'''14.	Requerir al usuario que ingrese un número entero e informar si es 
primo o no, utilizando una función booleana que lo decida.'''

@pytest.mark.parametrize("number, res",[(5,True),(4,False),(3,True),(9,False)])
def test_prime_number(number, res):
    assert prime_number(number) == res

'''15.	Escribir un programa que pida números al usuario, motrar el 
factorial de cada uno y, al finalizar, la cantidad total de números 
leídos en total. Utilizar una o más funciones, según sea necesario.'''

@pytest.mark.parametrize("go_on, res",[("0",True),("s",False),("2",False)])
def test_function_go_on(go_on, res):
    assert function_go_on(go_on) == res

@pytest.mark.parametrize("total_numbers, res",[(0,1),(4,5),(80,81)])
def test_function_total_numbers(total_numbers, res):
    assert function_total_numbers(total_numbers) == res

@pytest.mark.parametrize("number, res",[(3,6),(5,120),(6,720),(2,2)])
def test_factorial_function(number, res):
    assert factorial_function(number) == res

'''16.	Solicitar al usuario un número entero y luego un dígito. Informar 
la cantidad de ocurrencias del dígito en el número, utilizando para ello 
una función que calcule la frecuencia.'''

@pytest.mark.parametrize("int_number, digit, res",[(567855,5,3),(345668966,6,4),(2345,9,0)])
def test_function_occurrences(int_number, digit, res):
    assert function_occurrences(int_number, digit) == res

'''17.	Solicitar al usuario el ingreso de números primos. La lectura 
finalizará cuando ingrese un número que no sea primo. Por cada número, 
mostrar la suma de sus dígitos. También solicitar al usuario un dígito 
e informar la cantidad de veces que aparece en el número (frecuencia). 
Al finalizar el programa, mostrar el factorial del mayor número ingresado.'''

@pytest.mark.parametrize("number, res",[(367,True),(107,True),(100,False),(40,False)])
def test_function_prime_number(number, res):
    assert function_prime_number(number) == res

@pytest.mark.parametrize("number, res",[(367,16),(107,8),(435,12)])
def test_function_digit_addition(number, res):
    assert function_digit_addition(number) == res

@pytest.mark.parametrize("digit, number, res",[(4,4344,3),(5,678,0),(7,987,1)])
def test_digit_in_number(digit, number, res):
    assert digit_in_number(digit, number) == res

@pytest.mark.parametrize("big_number, res",[(7,5040),(5,120),(8,40320)])
def test_function_big_factorial(big_number, res):
    assert function_big_factorial(big_number) == res