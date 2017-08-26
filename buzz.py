numero = int(input("Informe um número inteiro: "))

divisivelPorCinco = numero % 5 == 0

if divisivelPorCinco:
	print("Buzz")
else:
	print(numero)