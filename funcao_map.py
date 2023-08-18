lista = [1, 2, 3, 4, 5]


def duplica(num):
    return num * 2


print(duplica(2))

lista_mapeada = map(duplica, lista)

print(list(lista_mapeada))

# soma entre elementos de duas istas diferentes
lista2 = [5, 6, 7, 8]

print(list(map(lambda num1, num2: num1 + num2, lista, lista2)))

# Passando para upper case
lista_strings = ["lista", "de", "strings"]

print(list(map(str.upper, lista_strings)))

