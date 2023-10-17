import funcionEjercicio2
'''2. Suponer una lista con datos de las compras hechas por clientes de 
una empresa a lo largo de un mes, la cual
contiene tuplas con información de cada venta: (cliente, día del mes, 
monto, domicilio del cliente). Ejemplo:
*(‘Nuria Costa’, 5, 1234.5,’Calle 1 – 456’), (‘Jorge Russo’, 7, 3999, 
‘Calle 2 – 741’)+
Escribir una función que reciba como parámetro una lista con el 
formato mencionado anteriormente y
retorne los domicilios de cada cliente al cual se le debe enviar 
una factura de compra. Notar que cada cliente
puede haber hecho más de una compra en el mes, por lo que la función 
debe retornar una estructura que
contenga cada domicilio una sola vez.'''
buy_list = [("Nuria Costa",5,1234.5,"Calle 1 - 456"),("Jorge Russo",7,3999,"Calle 2 - 741"),("Nuria Costa",10,345,"Calle 1 - 456"),("Matias Games",23,3678,"Calle 3 - 678")]
home_list = funcionEjercicio2.home(buy_list)
print("Los domicilios de las personas que se les debe enviar una factura de compra son: ")
for i in home_list:
    print(i)


