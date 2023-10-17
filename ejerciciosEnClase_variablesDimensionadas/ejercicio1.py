'''1. Escribir un programa que permita procesar datos de pasajeros de 
viaje en una lista de tuplas con la siguiente
forma: (nombre, dni, destino). Por ejemplo:
*(‘Manuel Juarez’, 12345678, ‘San Juan’), (‘Silvana Paredes’, 62258472, 
‘Mendoza’)+
Además en otra lista de tuplas se almacenan los datos de cada ciudad y 
el país al que pertenecen. Ejemplo:
*(‘Buenos Aires’, ‘Argentina’), (‘Lisboa’, ‘Portugal’), (‘Mendoza’, 
‘Argentina’)+
Hacer un menú iterativo que permita al usuario realizar las siguientes 
operaciones:
- Agregar pasajeros a la lista de viajeros.
- Agregar ciudades a la lista de ciudades.
- Dado el DNI de un pasajero, ver a qué ciudad viaja.
- Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa 
ciudad.
- Dado el DNI de un pasajero, ver a qué país viaja.
- Dado un país, mostrar cuántos pasajeros viajan a ese país.
- Salir del programa.'''
passager_list = []
cities_list = []

while True:
    print("\nMenú:")
    print("1. Agregar pasajeros")
    print("2. Agregar ciudades")
    print("3. Dado el DNI de un pasajero, ver a qué ciudad viaja")
    print("4. Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad")
    print("5. Dado el DNI de un pasajero, ver a qué país viaja")
    print("6. Dado un país, mostrar cuántos pasajeros viajan a ese país")
    print("7. Salir")

    option = int(input("Ingrese la opción deseada: "))


    if option == 1:
        name = input("Nombre del pasajero: ")
        dni = int(input("DNI del pasajero: "))
        destiny = input("Destino del pasajero: ")
        passager_list.append((name, dni, destiny))

    elif option == 2:
        city = input("Ciudad: ")
        country = input("País de la ciudad: ")
        cities_list.append((city, country))

    elif option == 3:
        dni = int(input("Ingrese el DNI del pasajero: "))
        found = False
        for pasajero in passager_list:
            if pasajero[1] == dni:
                destiny_city = pasajero[2]
                found = True
                break
        if (found):
            print(f"El pasajero viaja a {destiny_city}")
        else:
            print("DNI no encontrado")

    elif option == 4:
        city = input("Ingrese una ciudad: ")
        city = city.lower()
        travelers_counter = 0
        for i in passager_list:
            if (i[2] == city):
                travelers_counter += 1
        print(f"La cantidad de pasajeros que viajan a {city} es {travelers_counter}")

    elif option == 5:
        dni = int(input("Ingrese el DNI del pasajero: "))
        found = False
        for passager in passager_list:
            if passager[1] == dni:
                destiny_city = passager[2]
                found = True
                break
        if (found):
            for city, country in cities_list:
                if city == destiny_city:
                    print(f"El pasajero va a viajar a {country}")
                    break
        else:
            print("DNI no encontrado")

    elif option == 6:
        country = input("Ingrese un país: ")
        country = country.lower()
        country_passager_counter = 0
        for i in cities_list:
            if (i[1] == country):
                country_passager_counter += 1
            else:
                pass
        print(f"La cantidad de pasajeros que viajan a {country} es {country_passager_counter}")

    elif option == 7:
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")





