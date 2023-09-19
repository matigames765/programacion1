import funciones
'''El siguiente programa debería imprimir el número 2 si se le ingresan 
como valores x=5,
y=1 pero en su lugar imprime 5. ¿Qué hay que corregir?'''

#Lo que hay que corregir es cambiar las variables x e y globales usadas 
# en las
#funciones por las variables locales de la funcion a y b ya que es mala 
#practica

#PROGRAMA PRINCIPAL

x = int(input("Un numero: "))
y = int(input("Otro numero: "))

print(funciones.most(x - 3, funciones.least(x + 2, y - 5)))



