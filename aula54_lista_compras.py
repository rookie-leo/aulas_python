condicao = True
continuar = True
lista = []
while condicao:
    print("""O que gostaria de fazer?
            [ 1 ] Adicionar item a lista
            [ 2 ] Remover item da lista
            [ 3 ] Mostrar lista completa
            [ 4 ] Editar item da lista
            [ 5 ] Sair
    """)
    opcao = input("Digite o numero da opção escolhida: ")

    if opcao == '5':
        condicao = False
    elif opcao == '1':
        item = input("Insira o nome do item: ")
        lista.append(item)

        while continuar:
            opcao = input("Gostaria de inserir mais um item? [s/n]")

            if opcao == 's':
                item = input("Insira o nome do item: ")
                lista.append(item)
            else: break

    elif opcao == '2':
        opcao = input("Digite o numero do item que voce deseja remover: ")
        try:
            num = int(opcao)
            lista.pop(num)
        except:
            print("Valor inserido, invalido")

    elif opcao == '3':
        for indice, item in enumerate(lista):
            print(indice, item)

    elif opcao == '4':
        opcao = input("Digite o numero do item que voce deseja modificar: ")
        try:
            num = int(opcao)
            item = input("Insira o nome do item: ")
            lista[num] = item
        except:
            print("Valor inserido, invalido")
    
    else: print("Opção digitada invalida!")
