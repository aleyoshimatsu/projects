numero = int(input("Digite o valor de n: "))

fatorial = 1

while numero > 0:
    fatorial = fatorial * numero
    numero = numero - 1

print(fatorial)
