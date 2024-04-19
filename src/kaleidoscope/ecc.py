from math import sqrt
from random import randint


def eea(a, b):
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t


def inverse_of(n, p):
    gcd, x, y = eea(n, p)
    assert (n * x + p * y) % p == gcd

    if gcd != 1:
        raise ValueError("{} has no multiplicative inverse " "modulo {}".format(n, p))
    else:
        return x % p


def mod_sqrt(n):
    root = int(sqrt(n))
    if pow(root, 2) == n:
        return root
    else:
        return None


class Ecc:
    def __init__(self, a, b, p, G, n):
        self.a = a
        self.b = b
        self.p = p
        self.G = G
        self.n = n
        self.pub_key = self.mul(self.G, self.n)

    def is_at_curve(self, P):
        (x, y) = P
        if (pow(y, 2) - (pow(x, 3) + self.a * x + self.b)) % self.p == 0:
            return True
        else:
            return False

    def solve_y(self, x):
        y_square_modular = (pow(x, 3) + self.a * x + self.b) % self.p
        return mod_sqrt(y_square_modular)

    def add(self, P, Q):
        if P == None:
            return Q
        elif Q == None:
            return P

        (x1, y1) = P
        (x2, y2) = Q

        if x1 == x2 and (y1 + y2) == self.p:
            return None
        elif P == Q:
            k = (3 * pow(x1, 2) + self.a) * inverse_of(2 * y1, self.p) % self.p
        else:
            k = (y2 - y1) * inverse_of(x2 - x1, self.p) % self.p
        x = (pow(k, 2) - x1 - x2) % self.p
        y = self.p - (y2 + k * (x - x2)) % self.p
        return (x, y)

    def mul(self, P, n):
        Q = None
        (x, y) = P

        while True:
            if n % 2 == 1:
                Q = self.add(P, Q)
            P = self.add(P, P)
            n = n // 2
            if n == 0:
                return Q

    def encrypt(self, plain_text):
        pass

    def decrypt(self, ciphertext):
        pass


class Secp256k1(Ecc):
    def __init__(self):
        a = 0
        b = 7
        p = 2**256 - 2**32 - 2**9 - 2**8 - 2**7 - 2**6 - 2**4 - 1
        g_x = int("0x79BE667EF9DCBBAC55A06295CE870B07029BFCDB2DCE28D959F2815B16F81798", 16)
        g_y = int("0x483ADA7726A3C4655DA4FBFC0E1108A8FD17B448A68554199C47D08FFB10D4B8", 16)
        G = (g_x, g_y)
        n = randint(p // 2, p)
        super().__init__(a, b, p, G, n)


class Secp256r1(Ecc):
    def __init__(self):
        a = int("0xFFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFC", 16)
        b = int("0x5AC635D8AA3A93E7B3EBBD55769886BC651D06B0CC53B0F63BCE3C3E27D2604B", 16)
        p = int("FFFFFFFF00000001000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF", 16)
        g_x = int("0x6B17D1F2E12C4247F8BCE6E563A440F277037D812DEB33A0F4A13945D898C296", 16)
        g_y = int("0x4FE342E2FE1A7F9B8EE7EB4A7C0F9E162BCE33576B315ECECBB6406837BF51F5", 16)
        G = (g_x, g_y)
        n = randint(p // 2, p)
        super().__init__(a, b, p, G, n)


class TestCurve(Ecc):
    def __init__(self):
        a = 1
        b = 3
        p = 23
        g_x = 2
        g_y = 6
        G = (g_x, g_y)
        n = randint(p // 2, p)
        super().__init__(a, b, p, G, n)


tc = TestCurve()
print(tc.solve_y(16))
# s = Secp256r1()
# print(s.is_at_curve(s.mul(s.G, 12555)))
# message_1 = "大家好！P3无水印原版已上传，要看原版的请直接跳到P3。这一版《范进中举》，年代是1985年，主演是张瞳。值得一提的是，张瞳老先生也在话剧《咸亨酒店》中饰演过孔乙己。"
# message_2 = "Elliptic curves are applicable for key agreement, digital signatures, pseudo-random generators and other tasks. Indirectly, they can be used for encryption by combining the key agreement with a symmetric encryption scheme. They are also used in several integer factorization algorithms that have applications in cryptography, such as Lenstra elliptic-curve factorization."
# message_3 = "lyl"
# print(message_3.encode("utf-8").hex())
# print(message_2.encode("utf-8"))
