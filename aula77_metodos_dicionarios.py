import copy

pessoa = {
    "nome": "Fulano",
    "sobrenome": "Silva",
    "endereco": [
        {"rua": "Dos bobos", "numero": 0000},
        {"rua": "Ladrilho", "numero": 1234}
    ]
}

print(pessoa.keys())
print(list(pessoa.keys()))

for chaves in pessoa.keys():
    print(chaves)

for valor in pessoa.values():
    print(valor)

p2 = pessoa.copy()  # shallow copy/copia rasa
p3 = copy.deepcopy(pessoa)  # deep copy/copia profunda

pessoa["nome"] = "Sicrano"
pessoa["endereco"][0] = "'rua':'teste'"

print(pessoa)  # {'nome': 'Sicrano', 'sobrenome': 'Silva', 'endereco': ["'rua':'teste'", {'rua': 'Ladrilho', 'numero': 1234}]}
print(p2)  # {'nome': 'Fulano', 'sobrenome': 'Silva', 'endereco': ["'rua':'teste'", {'rua': 'Ladrilho', 'numero': 1234}]}
print(p3)  # {'nome': 'Fulano', 'sobrenome': 'Silva', 'endereco': [{'rua': 'Dos bobos', 'numero': 0}, {'rua': 'Ladrilho', 'numero': 1234}]}
