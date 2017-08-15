def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n-1)

def binomial (n, k):
    return fatorial(n) / (fatorial(k) * fatorial(n-k))
