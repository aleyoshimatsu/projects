def soma_elementos(lista):
    s = 0
    for n in lista:
        s += n

    return s

def main():
    lista = [12,22,3,3,41,5,6,777,7,7,8,9,10,11]

    s = soma_elementos(lista)
    print(s)
