var = input("Digite um numero inteiro qualquer: ")

try:
    num = int(var)

    if num % 2 == 0:
        print("Você digitou um numero par")
    else:
        print("Você digitou um numero impar")
except:
    print("Você não digitou um numero inteiro!")