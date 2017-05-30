from random import randint
from math import gcd
from invert import *

q = 7674101289
phi_q = q-1

for _ in range(1000000):
    private = randint(2, phi_q)
    while gcd(private, phi_q) > 1:
        private = randint(2, phi_q)

    inv_private = modinv(private, phi_q)
    r = (private * inv_private) % phi_q

    if r != 1:
        raise Exception("WRONG FOR PRIVATE=", private)

print("All righty!")
