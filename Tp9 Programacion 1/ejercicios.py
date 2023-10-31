#1.	Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:
    #•	Un constructor, donde los datos pueden estar vacíos.
    #•	Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    #•	mostrar(): Muestra los datos de la persona.
    #•	esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.

class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")
    def esMayorDeEdad(self):
        if (self.edad>= 18):
            print(f"{self.nombre} es mayor de edad")
        else:
            print(f"{self.nombre} NO es mayor de edad")

#MAIN
option = 0

persona1 = Persona("Jorge", 20, 44662355)
persona2 = Persona("Santiago", 21, 44308927)
persona3 = Persona("Agustin", 20, 44662090)
persona4 = Persona("Lautaro", 17, 47567209)
persona5 = Persona("Juani",15, 48679090)

while option != 1 and option != 2 and option != 3 and option != 4 and option != 5:
    option = int(input("Ingrese un numero del 1 al 5 para conocer los datos de una persona: "))
    
    if option==1:
        print(f"Datos de {persona1.nombre}")
        print(persona1.mostrar())
        print(persona1.esMayorDeEdad())
    
    if option==2:
        print(f"Datos de {persona1.nombre}")
        print(persona2.mostrar())
        print(persona2.esMayorDeEdad())
    
    if option==3:
        print(f"Datos de {persona1.nombre}")
        print(persona3.mostrar())
        print(persona3.esMayorDeEdad())
    
    if option==4:
        print(f"Datos de {persona1.nombre}")
        print(persona4.mostrar())
        print(persona4.esMayorDeEdad())

    if option==5:
        print(f"Datos de {persona1.nombre}")
        print(persona5.mostrar())
        print(persona5.esMayorDeEdad())

print("Programa terminado, muchas gracias!")

#2.	Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. Construye los siguientes métodos para la clase:
    #•	Un constructor, donde los datos pueden estar vacíos.
    #•	Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, sólo ingresando o retirando dinero.
    #•	mostrar(): Muestra los datos de la cuenta.
    #•	ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada.
    #•	retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_titular(self, titular):
        if isinstance(titular, Persona):
            self.titular = titular
        else:
            print("Titular no válido")

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        print(f"Titular: {self.titular.get_nombre()}")
        print(f"Cantidad en la cuenta: ${self.cantidad:.2f}")

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def get_nombre(self):
        return self.nombre

# Crear una cuenta
nombre = input("Ingrese el nombre del titular: ")
edad = int(input("Ingrese la edad del titular: "))
dni = input("Ingrese el DNI del titular: ")
persona = Persona(nombre, edad, dni)
cuenta = Cuenta(persona)

# Mostramos la cuenta
cuenta.mostrar()

# ingreso o retire dinero
while True:
    opcion = input("¿Desea ingresar (I) o retirar (R) dinero? (Q para salir): ").upper()
    if opcion == "Q":
        break
    elif opcion == "I":
        cantidad = float(input("Ingrese la cantidad a ingresar: "))
        cuenta.ingresar(cantidad)
    elif opcion == "R":
        cantidad = float(input("Ingrese la cantidad a retirar: "))
        cuenta.retirar(cantidad)
    cuenta.mostrar()


#3.	Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def determinar_tipo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "equilátero"
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            return "isósceles"
        else:
            return "escaleno"

    def lado_mayor(self):
        return max(self.lado1, self.lado2, self.lado3)

# Solicitar al usuario que ingrese los lados del triángulo
lado1 = float(input("Ingrese el primer lado del triángulo: "))
lado2 = float(input("Ingrese el segundo lado del triángulo: "))
lado3 = float(input("Ingrese el tercer lado del triángulo: "))

triangulo = Triangulo(lado1, lado2, lado3)

print(f"El tipo de triángulo es: {triangulo.determinar_tipo()}")
print(f"El lado con tamaño mayor es: {triangulo.lado_mayor()}")

#4.	Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones:
    #•	Añadir contacto
    #•	Lista de contactos
    #•	Buscar contacto
    #•	Editar contacto
    #•	Cerrar agenda

class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        contacto = Contacto(nombre, telefono, email)
        self.contactos.append(contacto)

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Lista de contactos:")
            for i, contacto in enumerate(self.contactos, start=1):
                print(f"{i}. Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Contacto encontrado - Nombre: {contacto.nombre}, Teléfono: {contacto.telefono}, Email: {contacto.email}")
                return
        print(f"Contacto no encontrado: {nombre}")

    def editar_contacto(self, nombre, nuevo_nombre, nuevo_telefono, nuevo_email):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.nombre = nuevo_nombre
                contacto.telefono = nuevo_telefono
                contacto.email = nuevo_email
                print(f"Contacto editado correctamente.")
                return
        print(f"Contacto no encontrado: {nombre}")

    def menu(self):
        while True:
            print("\nMenú de Agenda:")
            print("1. Añadir contacto")
            print("2. Lista de contactos")
            print("3. Buscar contacto")
            print("4. Editar contacto")
            print("5. Cerrar agenda")

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                self.agregar_contacto(nombre, telefono, email)
            elif opcion == "2":
                self.mostrar_contactos()
            elif opcion == "3":
                nombre = input("Nombre a buscar: ")
                self.buscar_contacto(nombre)
            elif opcion == "4":
                nombre = input("Nombre a editar: ")
                nuevo_nombre = input("Nuevo nombre: ")
                nuevo_telefono = input("Nuevo teléfono: ")
                nuevo_email = input("Nuevo email: ")
                self.editar_contacto(nombre, nuevo_nombre, nuevo_telefono, nuevo_email)
            elif opcion == "5":
                print("Agenda cerrada.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    agenda = Agenda()
    agenda.menu()



    