import math

xa = int(input("Informe um número inteiro: "))
ya = int(input("Informe um número inteiro: "))
xb = int(input("Informe um número inteiro: "))
yb = int(input("Informe um número inteiro: "))

distancia = math.sqrt((xb - xa)**2 + (yb - ya)**2)

if distancia >= 10:
	print("longe")
else:
	print("perto")
