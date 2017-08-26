numero_str = input("Digite um número inteiro: ")
numero = int(numero_str)

i = 0
somaDigitos = 0
nDigitos = len(numero_str)

digito = 0

while i < nDigitos:
	digito = numero % 10
	numero = numero // 10
	
	somaDigitos = somaDigitos + digito
	i = i + 1
	
print (somaDigitos)