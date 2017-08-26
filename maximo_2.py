def maximo(x, y):
    if x > y:
        return x
    else:
        return y

def test_maximo():
    assert maximo(3,4) == 4

def test_maximo_neg():
    assert maximo(0,-1) == 0
    
