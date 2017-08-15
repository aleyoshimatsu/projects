def vogal (caracter):
    EhVogal = False

    if caracter == "a" or caracter == "e" or caracter == "i" or caracter == "o" or caracter == "u" or caracter == "A" or caracter == "E" or caracter == "I" or caracter == "O" or caracter == "U":
        EhVogal = True

    return EhVogal

def test_vogal_a():
    assert vogal("a")
    assert vogal("A")

def test_vogal_e():
    assert vogal("e")
    assert vogal("E")

def test_vogal_i():
    assert vogal("i")
    assert vogal("I")

def test_vogal_o():
    assert vogal("o")
    assert vogal("O")

def test_vogal_u():
    assert vogal("u")
    assert vogal("U")

def test_vogal_b():
    assert not vogal("b")
    assert not vogal("B") 
