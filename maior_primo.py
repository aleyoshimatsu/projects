def maior_primo(n):
    if n < 1:
        return 0
    elif n == 1:
        return 1

    maior_primo = -1

    while n >= 2 and maior_primo == -1:
        if EhPrimo(n):
            maior_primo = n
        else:
            n = n - 1
            
    return maior_primo

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

def test_EhPrimo_1():
    assert not EhPrimo(1)

def test_EhPrimo_2():
    assert EhPrimo(2)

def test_EhPrimo_3():
    assert EhPrimo(3)

def test_EhPrimo_97():
    assert EhPrimo(97)

def test_EhPrimo_4():
    assert not EhPrimo(4)

def test_EhPrimo_100():
    assert not EhPrimo(100)

def test_maior_primo_0():
    assert maior_primo(0) == 0

def test_maior_primo_1():
    assert maior_primo(1) == 1

def test_maior_primo_2():
    assert maior_primo(2) == 2

def test_maior_primo_100():
    assert maior_primo(100) == 97

def test_maior_primo_7():
    assert maior_primo(7) == 7
