def nao_aceita_zero(n):
    if n == 0:
        raise ZeroDivisionError("Valores não podem ser divididos por ZERO")


def verifica_int_float(n):
    if not isinstance(n, (float, int)):
        raise TypeError(f"{n} deve ser int ou float")


def divide(x, y):
    nao_aceita_zero(x)
    nao_aceita_zero(y)
    verifica_int_float(x)
    verifica_int_float(y)

    return x / y


print(divide(10, 2))
print(divide(10, 0))
