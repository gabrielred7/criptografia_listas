from random import getrandbits, randrange

def __init__(n, p, q):
    n.numero_primo = n.gerar_primos()
    n.p = p
    n.q = q
    
def gerar_primos(n):
    while not n.miller_rabin(n.numero_primo, 10):
        n.numero_primo = randrange(1, 1000)
        if verifica_primo(n.numero_primo) == True:
            return n.numero_primo

def verifica_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def miller_rabin(n, quant=10):
    if n < 6:
        return [False, False, True, True, False, True][n]
    if n <= 1 or n % 2 == 0:
        return False
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    for _ in range(quant):
        b = randrange(2, n - 1)
        x = pow(b, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True