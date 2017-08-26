def fizzbuzz (numero):
    if numero % 3 == 0 and numero % 5 != 0:
        return "Fizz"
    elif numero % 5 == 0 and numero % 3 != 0:
        return "Buzz"
    elif numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    else:
        return numero

def test_fizzbuzz_3():
    assert fizzbuzz(3) == "Fizz"

def test_fizzbuzz_5():
    assert fizzbuzz(5) == "Buzz"

def test_fizzbuzz_15():
    assert fizzbuzz(15) == "FizzBuzz"

def test_fizzbuzz_4():
    assert fizzbuzz(4) == 4
