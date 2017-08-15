def n_primos(n):
    if n < 2:
        return 0

    q = 0
    aux = 2

    while aux >= 2 and aux <= n:
        if EhPrimo(aux):
            q += 1
        aux += 1
            
    return q

def EhPrimo(n):
    EhPrimo = True
    d = 2

    if n <= 1:
        EhPrimo = False

    while EhPrimo and d <= n / 2:
        if n % d == 0:
            EhPrimo = False
        d = d + 1

    return EhPrimo

n_primos(55)
