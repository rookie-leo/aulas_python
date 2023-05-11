class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    @classmethod
    def criar_com_50_anos(cls, nome, sobrenome):
        return cls(nome, sobrenome, 50)


p = Pessoa("Fulano", "Silva", 15)
p1 = Pessoa("Sicrano", "Soares", 26)
p2 = Pessoa.criar_com_50_anos("Beltrano", "Roncoso")

print(F"{p.nome} {p.sobrenome} {p.idade}")
print(F"{p1.nome} {p1.sobrenome} {p1.idade}")
print(f"{p2.nome} {p2.sobrenome} {p2.idade}")
