numero = int(input("Informe um número inteiro: "))

divisivelPorTresECinco = numero % 3 == 0 and numero % 5 == 0

if divisivelPorTresECinco:
	print("FizzBuzz")
else:
	print(numero)
