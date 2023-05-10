nums = [num for num in range(10)]
print(nums)

print()

nums_multiplicados = [num * 2 for num in range(10)]
print(nums_multiplicados)

prods = [
    {"nome": "mouse", "preco": 85.99},
    {"nome": "teclado", "preco": 100.50},
    {"nome": "monitor", "preco": 850.99}
]

novos_precos = [
    {**produto, "preco": produto["preco"] * 1.05}
    if produto["preco"] < 100.00 else {**produto}
    for produto in prods
]

print(prods)
print(*novos_precos, sep="\n")

num_par = [num for num in range(1, 10) if num % 2 == 0]
print(num_par)
