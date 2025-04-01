import random
import unittest
from math import gcd

def e_primo(n):
    """
    Essa função checa se um número 'n' é primo. 
    Se for menor que 2, Retorna False.
    Depois, testa divisores até a raiz quadrada de 'n'. 
    Se encontrar algum divisor, não é primo. Caso contrário, é primo.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def gerador_primos():
    """
    Aqui gera dois números primos aleatórios grandes (neste caso entre 100 e 1000).
    Fica num loop até encontrar dois primos válidos, porque precisamos deles para continuar.
    No final, retorna os dois primos: p e q.
    """
    while True:
        p = random.randint(100, 1000)
        if e_primo(p):
            break
    while True:
        q = random.randint(100, 1000)
        if e_primo(q):
            break
    return p, q

def mod_exp(base, exponent, modulus):
    """
    Calcula (base^exponent) % modulus de forma eficiente — a magia da Exponenciação Modular!
    
    Parâmetros:
    - base: O número base, ou seja, o "ponto de partida" do cálculo.
    - exponent: O expoente, que determina quantas vezes multiplicamos a base por ela mesma.
    - modulus: O módulo, que é o "teto" para o resultado final.

    Retorna:
    - O resultado de (base^exponent) % modulus, que é sempre um número menor que o módulo.
    """
    result = 1  # Começamos com o resultado igual a 1, pois qualquer número elevado a 0 é 1.
    base = base % modulus  # Reduzimos a base módulo 'modulus' para simplificar os cálculos.

    while exponent > 0:
        # Se o expoente for ímpar, significa que precisamos multiplicar o resultado pela base atual.
        if exponent % 2 == 1:
            result = (result * base) % modulus
        
        # Elevamos a base ao quadrado (mod modulus) para reduzir o problema à metade.
        base = (base * base) % modulus
        exponent //= 2  # Dividimos o expoente por 2 (ou seja, pegamos a parte inteira).

    return result

def simbolo_legendre(a, p):
    """
    O símbolo de Legendre (a | p) diz se 'a' é um resíduo quadrático módulo 'p'.
    Usamos a exponenciação modular para calcular isso.
    Retorna 1 se 'a' é resíduo quadrático, -1 se não for, ou 0 se 'a' ≡ 0 mod p.
    """
    return mod_exp(a, (p - 1) // 2, p)

def e_residuo_quadratico(a, p, q):
    """
    Essa função verifica se 'a' é resíduo quadrático módulo n = p * q.
    Para isso, checa se 'a' é resíduo quadrático tanto módulo 'p' quanto módulo 'q'.
    Se for nos dois, retorna True. Caso contrário, False.
    """
    return simbolo_legendre(a, p) == 1 and simbolo_legendre(a, q) == 1


def gerar_chaves():
    """
    Aqui geramos as chaves do sistema.
    - Chave pública: (n, y), onde n = p * q e 'y' é um valor que NÃO é resíduo quadrático módulo n.
    - Chave privada: (p, q), os fatores primos de n.
    A gente fica tentando valores aleatórios para 'y' até encontrar um válido.
    No final, retorna as duas chaves prontinhas para uso.
    """
    p, q = gerador_primos()
    n = p * q
    
    while True:
        y = random.randint(2, n - 1)
        if gcd(y, n) == 1 and not e_residuo_quadratico(y, p, q):
            break
    
    chave_publica = (n, y)
    chave_privada = (p, q)
    return chave_publica, chave_privada

def encriptar(chave_publica, m):
    """
    Função que encripta uma mensagem binária 'm' (0 ou 1) usando a chave pública (n, y).
    - Para m = 0, calcula c = r^2 mod n (um resíduo quadrático).
    - Para m = 1, calcula c = (r^2 * y) mod n (não necessariamente resíduo quadrático).
    Escolhe um 'r' aleatório e retorna o texto cifrado 'c'.
    """
    n, y = chave_publica
    r = random.randint(1, n - 1)  # Escolhe um número aleatório 'r'
    if m == 0:
        c = mod_exp(r, 2, n)  # Resíduo quadrático
    else:
        c = (mod_exp(r, 2, n) * y) % n  # Não necessariamente resíduo quadrático
    return c

def descriptar(chave_privada, c):
    """
    Função que descripta o texto cifrado 'c' usando a chave privada (p, q).
    - Verifica se 'c' é resíduo quadrático módulo n = p * q.
    - Se for, retorna m = 0 (mensagem original era 0).
    - Se não for, retorna m = 1 (mensagem original era 1).
    """
    p, q = chave_privada
    if e_residuo_quadratico(c, p, q):
        return 0  # Resíduo quadrático -> mensagem original era 0
    else:
        return 1  # Não resíduo quadrático -> mensagem original era 1
    
# Classe de Testes
class TestGoldwasserMicali(unittest.TestCase):

    def test_e_primo(self):
        self.assertTrue(e_primo(2))
        self.assertTrue(e_primo(3))
        self.assertTrue(e_primo(19))
        self.assertFalse(e_primo(1))
        self.assertFalse(e_primo(4))
        self.assertFalse(e_primo(100))

    def test_mod_exp(self):
        self.assertEqual(mod_exp(2, 10, 1000), 24)
        self.assertEqual(mod_exp(3, 13, 7), 3)
        self.assertEqual(mod_exp(5, 0, 7), 1)

    def test_gcd(self):
        self.assertEqual(gcd(12, 18), 6)
        self.assertEqual(gcd(101, 103), 1)
        self.assertEqual(gcd(0, 5), 5)
        self.assertEqual(gcd(17, 0), 17)

    def test_generate_primes(self):
        p, q = gerador_primos()
        self.assertTrue(e_primo(p))
        self.assertTrue(e_primo(q))
        self.assertNotEqual(p, q)

    def test_gerar_chaves(self):
        public_key, private_key = gerar_chaves()
        n, y = public_key
        p, q = private_key
        self.assertEqual(n, p * q)
        self.assertEqual(gcd(y, n), 1)
        self.assertFalse(e_residuo_quadratico(y, p, q))

    def test_encriptar_descriptar(self):
        public_key, private_key = gerar_chaves()
        
        # Testar criptografia e descriptografia para m = 0
        ciphertext_0 = encriptar(public_key, 0)
        descriptared_0 = descriptar(private_key, ciphertext_0)
        self.assertEqual(descriptared_0, 0)
        
        # Testar criptografia e descriptografia para m = 1
        ciphertext_1 = encriptar(public_key, 1)
        descriptared_1 = descriptar(private_key, ciphertext_1)
        self.assertEqual(descriptared_1, 1)

if __name__ == "__main__":
    unittest.main()