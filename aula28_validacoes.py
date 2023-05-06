nome = input("Digite sue nome: ")
idade = input("Digite sua idade: ")

if len(nome) > 0  and len(idade) > 0:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido fica {nome[::-1]}")
    
    if " " in nome:
        print("Seu nome contém espaços")
    else:
        print("Seu nome não contém espaços")
    
    print(f"Seu nome contém {len(nome)} letras")
    print(f"A primeira letra do seu nome é '{nome[0]}'")
    print(f"A ultima letra do seu nome é '{nome[len(nome)-1]}'")
else:
    print("Por favor, preencha todos os campos!")