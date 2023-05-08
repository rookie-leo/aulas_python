salas = [
    ["Maria", "João"],
    ["Ana", "Claudio", "Fulano",],
    ["Sicrano", "Beltrano", (0, 1, 2, 3, 4)]
]

print(salas[0][1])
print(salas[2][1])
print(salas[2][2][2])

for i,sala in enumerate(salas):
    print(sala)

for sala in salas:
    for aluno in sala:
        print(aluno)
