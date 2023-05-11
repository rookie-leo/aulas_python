class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property  # Getter em python
    def cor(self):
        return self.cor_tinta


caneta = Caneta("preta")
print(caneta.cor)
