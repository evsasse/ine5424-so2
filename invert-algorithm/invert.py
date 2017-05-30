def invert(private, q):
    old_t = 0
    old_r = q
    new_t = 1
    new_r = private

    while new_r != 0:
        print(old_r, new_r)
        qq = old_r // new_r

        aux_t = new_t
        new_t = old_t - qq * new_t
        old_t = aux_t

        aux_r = new_r
        new_r = old_r - qq * new_r
        old_r = aux_r

    if old_r > 1: raise Exception("NOT INVERTIBLE")
    if old_t < 0: return -(old_t + q)

    return old_t

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
