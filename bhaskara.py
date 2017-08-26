import math

def calcularDelta(a, b, c):
        return b ** 2 - 4 * a * c

def calcularRaizes(a, b, c):
        delta = calcularDelta(a, b, c)

        if delta == 0:
                x = -b / (2 * a)
                print("a raiz desta equação é", x)
        else:
                if delta < 0:
                        print("esta equação não possui raízes reais")
                else:
                        x1 = (-b + math.sqrt(delta)) / (2 * a)
                        x2 = (-b - math.sqrt(delta)) / (2 * a)
		
                        if x1 < x2:
                                print("as raízes da equação são", x1, "e", x2)
                        else:
                                print("as raízes da equação são", x2, "e", x1)


#a = float(input("Entre com o valor de a: "))
#b = float(input("Entre com o valor de b: "))
#c = float(input("Entre com o valor de c: "))

#calcularRaizes(a, b, c)



