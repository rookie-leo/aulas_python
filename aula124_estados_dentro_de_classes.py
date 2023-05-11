class Camera:
    def __init__(self, nome: str, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self) -> None:
        if self.filmando:
            print(f"{self.nome} já está filmando!")
            return
        print(f"{self.nome} está filmando...")
        self.filmando = True

    def para_de_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando!")
            return
        print(f"{self.nome} está parando de filmar!")
        self.filmando = False


c1 = Camera("Canon")
c2 = Camera("Sony")
c1.filmar()
c1.filmar()

print(c1.filmando)
print(c2.filmando)

c1.para_de_filmar()
c2.para_de_filmar()

print(c1.filmando)
print(c2.filmando)
