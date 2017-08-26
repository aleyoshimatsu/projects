numero = int(input("Informe um número inteiro: "))

divisivelPorDois = numero % 2 == 0

if divisivelPorDois:
	print("par")
else:
	print("impar")