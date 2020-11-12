from random import randrange

def __init__(self, n, num, p, q):
    self.n = n
    self.num = num
    self.p = p
    self.q = q

def gerar_primo(num):
    while not miller_rabin_alternativo(num, 10):
        primo = randrange(1, 1000)
        if verifica_primo(primo) == True:
            return primo

def verifica_primo(p):
    if p <= 3:
        return True
    if p <= 1 or p % 2 == 0 or p % 3 == 0:
        return False
    i = 5
    while i * i <= p:
        if p % i == 0 or p % (i + 2) == 0:
            return False
        i = i + 6
    return True

def miller_rabin_alternativo(n, quant=10):
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

def gerar_chaves(self):
    self.p = gerar_primo(self.num)
    self.q = gerar_primo(self.num)
    n = self.p * self.q
    phi = (self.p - 1) * (self.q - 1)
    print("Escolhendo sua chave publica: \n")
    print(str(coprimos(phi)) + "\n")
    y = totient(self.p)
    x = totient(self.q)
    totient_n = x * y
    e = gerar_e(totient_n)
    d = inverso_modular(e, phi)
    return print("\n Chaves Públicas (e = " + str(e) + ", n = " + str(n) + ")" +
                 "\n Chaves Privadas (d = " + str(d) + ", n = " + str(n) + ") \n" +
                 " Use essas chaves nos parametros para as funções encriptar e decriptar")

def coprimos(self, a):
    lista = list()
    for x in range(2, a):
        if self.mdc(a, x) == 1 and self.invesao_modular(x, a) != None:
            lista.append(x)
    for x in lista:
        if x == self.invesao_modular(x, a):
            lista.remove(x)
    return lista

def totient(num):
    if(verifica_primo(num)):
        return num - 1
    else:
        return False

def gerar_e(num):
    while True:
        e = randrange(2, num)
        if mdc(num, e) == 1:
            return e

def mdc(a, b):
    resto = a % b
    while resto != 0:
        a = b
        b = resto
        resto = a % b
    return b

def inverso_modular(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    print('Não há inverso modular para o bloco. \n')
    return None

def encriptar(texto, n, e):
    tam = len(texto)
    i = 0
    lista = list()
    while i < tam:
        letra = texto[i]
        k = ord(letra)
        k = k ** e
        d = modulacao(k, n)
        lista.append(d)
        i = i + 1
    return lista

def decriptar(blocos, n, d):
    tam = len(blocos)
    i = 0
    lista = list()
    while i < tam:
        resultado = blocos[i] ** d
        texto = modulacao(resultado, n)
        letra = chr(texto)
        lista.append(letra)
        i = i + 1
    return lista

def modulacao(a, b):
    if a < b:
        return a
    else:
        c = a % b
        return c