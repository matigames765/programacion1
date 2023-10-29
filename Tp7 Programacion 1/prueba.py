mixed_list = [30,"cadena",56,"jorgito",20,"matias",89,"santiago"]
number_list = []
string_list = []
for i in mixed_list:
    if isinstance(i,int):
        number_list.append(i)
    else:
        string_list.append(i)

mixed_list_new = []

length = len(number_list) - 1

for i in range(len(number_list) - 1):
    for j in range(length):
        if (number_list[j] > number_list[j + 1]):
            auxiliar_variable = number_list[j]
            number_list[j] = number_list[j + 1]
            number_list[j + 1] = auxiliar_variable
        else:
            pass
    length -= 1

for i in number_list:
    mixed_list_new.append(i)


length = len(string_list) - 1

for i in range(len(string_list) - 1):
    for j in range(length):
        if (string_list[j][0] > string_list[j + 1][0]):
            auxiliar_variable = string_list[j]
            string_list[j] = string_list[j + 1]
            string_list[j + 1] = auxiliar_variable
        else:
            pass
    length -= 1

print("Los elementos de la lista ordenados de forma ascendente quedan:")

for i in string_list:
    mixed_list_new.append(i)

for i in range(len(mixed_list_new)):
    if (i == len(mixed_list_new) - 1):
        print(mixed_list_new[i])
    else:
        print(f"{mixed_list_new[i]},", end = " ")


