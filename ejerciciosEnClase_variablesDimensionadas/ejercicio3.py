'''3. Crear un programa para gestionar datos de los socios de un club, 
permitiendo:
- Cargar información de los socios en un diccionario para acceder por 
número de socio. Los datos a almacenar
son: número, nombre y apellido, fecha de ingreso (ddmmaaaa), cuota al 
día (s/n). El programa debe iniciar
con los datos de los socios fundadores ya cargados:
o Socio n°1, Amanda Núñez, ingresó: 17/03/2009, cuota al día.
o Socio n°2, Bárbara Molina, ingresó: 17/03/2009, cuota al día.
o Socio n°3, Lautaro Campos, ingresó: 17/03/2009, cuota al día.
- Informar cantidad de socios del club.
- Solicitar al usuario el número de un socio y registrar que ha pagado 
todas las cuotas adeudadas.
- Modificar la fecha de ingreso de todos los socios ingresados el 
13/03/2018, para indicar que en realidad
ingresaron el 14/03/2018.
- Solicitar el nombre y apellido de un socio y darle de baja 
(eliminarlo del listado)
- Imprimir el listado de socios completo.'''
partner_dictionary = {1:[1,"Amanda Nùñez","17/03/2009","s"],2:[2,"Bárbara Molina","17/03/2009","s"],3:[3,"Lautaro Campos","17/03/2009","s"]}
partner_list = []
while True:
    partner_number = int(input("Ingrese el numero de socio del club: "))
    partner_list.append(partner_number)
    name = input("Ingrese el nombre: ")
    name = name.lower()
    partner_list.append(name)
    date_income = input("Ingrese la fecha de ingresa en formato dd/mm/aaaa: ")
    partner_list.append(date_income)
    share_at_day = input("Ingrese s si tiene la cuota al dia y n si no: ")
    share_at_day = share_at_day.lower()
    partner_list.append(share_at_day)
    partner_dictionary[partner_number] = partner_list
    partner_list = []
    out = input("Ingrese 0 para salir o cualquier otra tecla para continuar ingresando datos: ")
    if (out == "0"):
        break
    else:
        pass
print(f"La cantidad de socios del club es {len(partner_dictionary)}")
partner_number = int(input("Introduzca un numero de socio para saber si tiene todas las cuotas al dia: "))
for key,value in partner_dictionary.items():
    if (partner_number == key):
        if (value[3] == "s"):
            print("Tiene la cuota al dia")
        else:
            print("No tiene la cuota al dia")
    else:
        pass

for value in partner_dictionary.values():
    if (value[2] == "13/03/2018"):
        value[2] =  "14/03/2018"
    else:
        pass

name = input("Ingrese el apellido y nombre del socio que quiera darle de baja: ")
name = name.lower()

for value in partner_dictionary.values():
    if (value[1].lower() == name):
        del partner_dictionary[value[0]]
        break
    else:
        pass 


print("El listado de socios completo es:")

for values in partner_dictionary.values():
    print(f"Socio Nro {values[0]}: {values[1]}")

