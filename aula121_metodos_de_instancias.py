class Carro:
    def __init__(self, nome: str):
        self.nome = nome

    def acelerar(self) -> None:
        print(f"{self.nome} está acelerando")


fusca = Carro("Fusca")
print(fusca.nome)
fusca.acelerar()

celta = Carro("Celta")
print(celta.nome)
celta.acelerar()
