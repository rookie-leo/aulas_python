try:
    a = 18
    b = 0
    c = a / b
    print(c)
    print(d)

except ZeroDivisionError as error:
    print(f"Erro: {error.__class__.__name__}")

except NameError as ex:
    print(f"Variavel não definida: {ex}")

print("Chegou no final")
