pessoa1 = {
    "nome": "Fulano",
    "sobrenome": "Silva",
    "idade": 45,
    "altura": 1.69,
    "endereco": [
        {"rua": "Dos bobos", "numero": 0000},
        {"rua": "Ladrilho", "numero": 1234}
    ]
}

print(pessoa1["nome"])
print(pessoa1["idade"])

for key in pessoa1:
    print(key, pessoa1[key])

pessoa = {}
chave = "nome"
pessoa[chave] = "Sicrano"

pessoa["sobrenome"] = "Souza"

print(pessoa[chave])

pessoa[chave] = "Maria"
print(pessoa[chave])

if pessoa.get("sobrenome") is None:
    print("Não existe")
else:
    print(pessoa["sobrenome"])

