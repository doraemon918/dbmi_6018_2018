"""
def int2bin(n):
    assert n >= 0
    if n == 0:
        return (,)
    else:
        return [n % 2] + int2bin(n//2)
"""

def bin2int(bits):
    return sum([i**2*bits[i] for i in range(0,len(bits))])

def complement(p):
    return 1-P

def select_random_int(n):
    random.choice(range(0,n))

def flip_coin():
    pass
