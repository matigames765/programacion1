class motocicleta:

    # Atributo de la clase
    estado = 'nueva'
    motor = False

    
    def __init__(self, color = "", matricula = "", combustible_litro = 0,
                numero_de_rueda = 0, marca = "", modelo = "", fecha_fabricacion = "",
                velocidad_punta = 0, peso = 0):
        
        self.color = color
        self.matricula = matricula
        self.combustible_litro = combustible_litro
        self.numero_de_rueda = numero_de_rueda
        self.marca = marca
        self.modelo = modelo
        self.fecha_fabricacion = fecha_fabricacion
        self.velocidad_punta = velocidad_punta
        self.peso = peso
   
    
    
    # Metodo para arrancar la moto
    def arrancar(self):
        if (self.motor == False):
            print("EL motor esta apagado, ahora se esta encendiendo.")
            self.motor = True
        elif (self.motor == True):
            print("El motor esta encendido.")

        

    # Metodo para detener la moto
    def detener(self):
        if (self.motor == True):
            print("EL motor esta encendido, ahora se esta apagando.")
            self.motor = False
        elif (self.motor == False):
            print("El motor esta apagado.")

    # Mostramos el precio de la moto 
    def precio(self):
        print(f"El precio de la motocicleta 1, {self.marca} {self.modelo} es de {self.price}$.")

    
    