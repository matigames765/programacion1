number = int(input("Ingrese un entero positivo para ver su factorial: "))
factorial = 1
if (number == 0):
    print("0! = 1")
else:
    for i in range(number,0,-1):
        factorial = factorial * i
    print(f"{number}! = {factorial}")