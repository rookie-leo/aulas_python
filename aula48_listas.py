lista = [1, 2, 3, 4]    #C
print(lista)            #R
lista[3] = 5            #U
del lista[0]            #D

for x in range(6, 20):
    lista.append(x)

print(lista)

lista.pop()
print(lista)

item_removido = lista.pop()
print(f"O item removido da lista foi {item_removido}")

item_removido = lista.pop(2)
print(f"O item removido da lista foi {item_removido}")

lista.insert(0, "Fulano")
print(lista)

lista.clear()
print(lista)

print((10*"*")+"Concatenando e Estendendo listas em Python!"+(10*"*"))
l_a = [1, 2, 3]
l_b = [4, 5, 6]
l_c = l_a + l_b
print(l_c)

l_d = []
l_d.extend(l_b)
print(l_d)

l_e = l_c.copy()
l_c[3] = 30
print(l_e)
print(l_c)