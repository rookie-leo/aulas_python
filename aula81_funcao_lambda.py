pessoas = [
    {"nome": "Fulano", "sobrenome": "Antunes"},
    {"nome": "Alisson", "sobrenome": "Souza"},
    {"nome": "Beltrano", "sobrenome": "Belmonte"},
    {"nome": "Sicrano", "sobrenome": "Oliveira"}
]


def exibir(lista):
    for item in lista:
        print(item)
    print()


l1 = sorted(pessoas, key=lambda obj: obj["nome"])
l2 = sorted(pessoas, key=lambda item: item["sobrenome"])

exibir(l1)
exibir(l2)
