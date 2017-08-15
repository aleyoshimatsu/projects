numero = int(input("Digite o valor de n: "))

aux = 1
imprimiuN = 1

while imprimiuN <= numero:
    if aux % 2 != 0:
        print(aux)
        imprimiuN += 1
    aux += 1
