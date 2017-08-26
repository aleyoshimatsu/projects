def maximo(x, y, z):
    max = x
    if y > max:
        max = y
    if z > max:
        max = z

    return max

def test_maximo():
    assert maximo(3,4,0) == 4

def test_maximo_neg():
    assert maximo(0,-1,-2) == 0

def test_maximo_30():
    assert maximo(30,14,10) == 30

def test_maximo_1():
    assert maximo(0,-1,1) == 1
    

