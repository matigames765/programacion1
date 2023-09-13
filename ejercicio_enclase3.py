fecha_actual = input("Ingrese la fecha actual en formato dia, DD/MM: ")
dia = fecha_actual[0:fecha_actual.find(",")]
dia = dia.lower()
dia_numero = int(fecha_actual[fecha_actual.find(" ")+1:fecha_actual.find("/")])
mes = int(fecha_actual[fecha_actual.find("/")+1:])
if (dia != "lunes" and dia != "martes" and dia != "miercoles" and dia != "jueves" and dia != "viernes"):
    print("Se produjo un error, ingreso un dia de la semana invalido")
elif (dia_numero < 1 or dia_numero > 31 or mes < 1 or mes > 12):
    print("Se produjo un error, ingreso mal el numero del dia o del mes")
else:
    if (dia == "lunes" or dia == "martes" or dia == "miercoles"):
        examen = input("Ingrese 'si/no' si se tomaron los examenes o no: ")
        examen = examen.lower()
        if (examen == "si"):
            alumnos_aprobados = int(input("Ingrese cuantos alumnos aprobaron: "))
            alumnos_desaprobados = int(input("Ingrese cuantos alumnos desaprobaron: "))
            porcentaje_aprobados = (alumnos_aprobados / (alumnos_aprobados + alumnos_desaprobados)) * 100
            print(f"El porcentaje de alumnos aprobados fue de un {porcentaje_aprobados}%")
        else:
            pass
    if (dia == "jueves"):
        porcentaje_asistencia = int(input("Ingrese el porcentaje de asistencia: "))
        if (porcentaje_asistencia > 50):
            print("Asistio la mayoria")
        else:
            print("No asistio la mayoria")
    elif (dia == "viernes" and ((dia_numero == 1 and mes == 1) or (dia_numero == 1 and mes == 7))):
        print("Comienzo de nuevo ciclo")
        alumnos_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
        arancel = int(input("Ingrese el arancel en $ por cada alumno: "))
        ingreso_total = alumnos_nuevo_ciclo * arancel
        print(f"El ingreso total es de {ingreso_total}$")
    else:
        pass