numero1 = int(input("Informe um número inteiro: "))
numero2 = int(input("Informe um número inteiro: "))
numero3 = int(input("Informe um número inteiro: "))

ordenacaoCrescente = numero1 < numero2 and numero2 < numero3

if ordenacaoCrescente:
	print("crescente")
else:
	print("não está em ordem crescente")
