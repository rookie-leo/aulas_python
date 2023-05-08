def soma(a, b):
    return a + b


def par_impar(num):
    if num % 2 == 0:
        return "par"

    return "impar"


result = soma(5, 5)

print(result)
print(par_impar(result))
