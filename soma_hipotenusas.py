import math

def soma_hipotenusas(n):
    hipotenusas = []
    
    for i in range(1, n+1):
        if é_hipotenusa(i):
            if not contains(hipotenusas, i):
                hipotenusas.append(i)

    return soma(hipotenusas)

def contains(hipotenusas, n):
    for i in hipotenusas:
        if i == n:
            return True

    return False

def é_hipotenusa(n):
    for a in range(1, n+1):
        for b in range(1, n+1):
            if n == math.sqrt(a**2 + b**2):
                return True

    return False

def soma(hipotenusas):
    s = 0
    for i in hipotenusas:
        s += i

    return s


soma_hipotenusas(25)
