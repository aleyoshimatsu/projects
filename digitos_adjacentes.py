numero_str = input("Digite um número inteiro: ")
numero = int(numero_str)

i = 0
digitoAnterior = -1
nDigitos = len(numero_str)
digito = 0
temAdjacenteIgual = False

while i < nDigitos and not temAdjacenteIgual:
	digito = numero % 10
	numero = numero // 10
	
	if digitoAnterior == digito:
		temAdjacenteIgual = True
	
	digitoAnterior = digito
	i = i + 1
	
if temAdjacenteIgual:
	print ("sim")
else:
	print ("não")
