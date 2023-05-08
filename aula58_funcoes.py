def multiplo_de(numero, multiplo):
    result = numero % multiplo == 0
    print(f"{numero} é multiplo de {multiplo}", end=" ")
    print(result)


multiplo_de(16, 8)
multiplo_de(15, 3)
multiplo_de(10, 2)
