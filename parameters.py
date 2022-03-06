import random

def is_prime(x):
    for num in range(2, x):
        if x % num == 0:
            return False
    return True

def get_prime_numbers(x, y):
    import random
    result = []

    while len(result) < 4:
        _z = random.randint(x, y)
        if not is_prime(_z):
            continue
        else:
            result.append(_z)

    return result

# get prime number until 100
# the bigger the number, the more time it takes
prime_list = get_prime_numbers(0, 100)

q = random.choice(prime_list)

# remove q from prime_list
prime_list = [x for x in prime_list if x != q]

p = random.choice(prime_list)

# byte format of q and p, if needed
q_16b = '{0:016b}'.format(q)
p_16b = '{0:016b}'.format(p)


def compute_N(_p, _q):
    result = _p * _q
    return result, '{0:016b}'.format(result)

def compute_Phi_N(_p, _q):
    result = (_p - 1) * (_q - 1)
    return result, '{0:016b}'.format(result)

def computegcd(e, Phi_N):
    if Phi_N == 0:
        return e
    else:
        return computegcd(Phi_N, e % Phi_N)

N, N16 = compute_N(p, q)
Phi_N, Phi_N16 = compute_Phi_N(p, q)

def get_public_key(Phi_N):
    e = random.randint(1, Phi_N)
    gcd = computegcd(e, Phi_N)
    while gcd != 1:
        e = random.randint(1, Phi_N)
        gcd = computegcd(e, Phi_N)
    
    return e

e = get_public_key(Phi_N)

def get_private_key(e, Phi_N):
    d = 1
    while d * e % Phi_N != 1:
        d += 1
    return d

d = get_private_key(e, Phi_N)

# print all the parameters
def show_parameters():
    print("p: {}".format(p))
    print("q: {}".format(q))
    print("N: {}".format(N))
    print("Phi(N): {}".format(Phi_N))
    print("public key e: {}".format(e))
    print("private key d: {}".format(d))
    print("N, e: {}, {}".format(N, e))