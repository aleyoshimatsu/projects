numero = int(input("Informe um número inteiro: "))

divisivelPorTres = numero % 3 == 0

if divisivelPorTres:
	print("Fizz")
else:
	print(numero)