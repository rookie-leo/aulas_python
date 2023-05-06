var = input("Vou dobrar qualquer numero que vc digitar: ")

try:
    num = float(var)
    print(f"O dobro de {var} é {num * 2}")

except:
    print("Você não digitou um numero!")