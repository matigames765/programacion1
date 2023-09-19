def add(value):
    addition = 0
    while value!= 0:
        digit = value % 10
        addition = addition + digit
        value = int(value / 10)
    return addition