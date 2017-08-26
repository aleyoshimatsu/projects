n = int(input("Digite um número: "))
lista = []
if n != 0:
    lista.append(n)

while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        lista.append(n)

lista_inversa = lista[::-1]

for i in lista_inversa:
    print(i)
