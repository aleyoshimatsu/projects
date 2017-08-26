def remove_repetidos(lista):
    lista_nova = []

    for n in lista:
        if n not in lista_nova:
            lista_nova.append(n)

    lista_nova.sort()
    return lista_nova

def main():
    lista = [12,22,3,3,41,5,6,777,7,7,8,9,10,11]

    lista_nova = remove_repetidos(lista)

    print(lista)
    print(lista_nova)

    print(sorted(lista))
    print(lista)
    lista.sort()
    print(lista)
    
main()
