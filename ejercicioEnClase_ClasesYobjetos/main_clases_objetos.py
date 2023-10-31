from clases_objetos import motocicleta

my_motocicleta1 = motocicleta("Rojo", "2450_NXB", 10, 2, "Honda", "CB190R 2020", "23/7/20", 130, 200)
my_motocicleta2 = motocicleta("Azul", "6576_JDJ", 12, 4, "Yamaha", "YZF_R6", "24/2/19", 140, 220)

# moto: matricula = 6576_JDJ, marca = yamaha, modelo = YZF-R6
my_motocicleta1.price = 45200
my_motocicleta2.price = 54300

# Motocicleta 1
print("MOTOCICLETA 1:")
# llamamos al metodo arrancar
print("Metodo arrancar: ")
my_motocicleta1.arrancar()

# Llamamos al metodo detener
print("Metodo arrancar: ")
my_motocicleta1.detener()

# Mostramos el precio de la moto 1
#print("El precio de la motocicleta ", x (marca y modelo), " es de x_precio' $.")
print("--------------")
print(f"El precio de la motocicleta 1, {my_motocicleta1.marca}, {my_motocicleta1.modelo} es de {my_motocicleta1.price}$.")

#Mostramos el precio de la moto 1, pero con un metodo de la clase
print("--------------")
print("El precio de la motocicleta, con un metodo de la clase:")
my_motocicleta1.precio()


print(" ")
# Motocicleta 2
print("MOTOCICLETA 2:")
# llamamos al metodo arrancar
print("Metodo arrancar: ")
my_motocicleta2.arrancar()

# Llamamos al metodo detener
print("Metodo arrancar: ")
my_motocicleta2.detener()

# Mostramos el precio de la moto 2
print("--------------")
print(f"El precio de la motocicleta 2, {my_motocicleta2.marca}, {my_motocicleta2.modelo} es de {my_motocicleta2.price}$.")

#Mostramos el precio de la moto 1, pero con un metodo de la clase
print("--------------")
print("El precio de la motocicleta, con un metodo de la clase:")
my_motocicleta2.precio()