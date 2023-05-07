var = input("Que horas são? ")

try:
    hr = int(var)

    if hr >= 0 and hr <= 11:
        print("Obrigado e bom dia!")

    elif hr >= 12 and hr <= 17:
        print("Obrigado e boa tarde!")

    elif hr >= 18 and hr <= 23:
        print("Obrigado e boa noite!")
    else:
        print("Desculpa, mas não sei que horas você quis dizer!")
except:
    print("O horario que você me informou não está correto!")