lista = [1, 2, 3, 4, 5]


def duplica(num):
    return num * 2


print(duplica(2))

lista_mapeada = map(duplica, lista)

print(list(lista_mapeada))
