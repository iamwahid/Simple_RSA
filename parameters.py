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


def format_byte(val):
    return '{0:016b}'.format(val)

# get prime number until 100
# the bigger the number, the more time it takes
prime_list = get_prime_numbers(0, 100)

q = random.choice(prime_list)

# remove q from prime_list
prime_list = [x for x in prime_list if x != q]

p = random.choice(prime_list)


def computegcd(e, Phi_N):
    if Phi_N == 0:
        return e
    else:
        return computegcd(Phi_N, e % Phi_N)

def get_e(Phi_N):
    e = random.randint(1, Phi_N)
    gcd = computegcd(e, Phi_N)
    while gcd != 1:
        e = random.randint(1, Phi_N)
        gcd = computegcd(e, Phi_N)
    
    return e


def get_d(e, Phi_N):
    d = 1
    while d * e % Phi_N != 1:
        d += 1
    return d

N = p * q
Phi_N = (p - 1) * (q - 1)

e = get_e(Phi_N)
d = get_d(e, Phi_N)

# print all the parameters
def show_parameters():
    print("p: {}, {}".format( p, format_byte(p) ))
    print("q: {}, {}".format( q, format_byte(q) ))
    print("N: {}, {}".format( N, format_byte(N) ))
    print("Phi(N): {}, {}".format( Phi_N, format_byte(Phi_N) ))
    print("public key e: {}, {}".format( e, format_byte(e) ))
    print("private key d: {}, {}".format( d, format_byte(d) ))
    print("N, e: {} ({}), {} ({})".format( N, format_byte(N), e, format_byte(e) ))