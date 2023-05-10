def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplica(num):
        return num * multiplicador
    return multiplica


print(executa(lambda x, y: x + y, 2, 3))
print(executa(soma, 2, 3))
print(soma(2, 3))
print()

duplica = cria_multiplicador(6)
duplica_v2 = executa(lambda m: lambda n: n * m, 6)
print(duplica)
print(duplica_v2)

print()
print(executa(lambda *args: sum(args), 1, 2, 3, 4, 5))
