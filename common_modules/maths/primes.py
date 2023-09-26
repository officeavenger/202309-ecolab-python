
def is_prime(n):
    if n<2:
        return False
    for x in range(2,n):
        if n%x==0:
            return False
    return True

def find_primes(min,max):
    primes=[]
    for x in range(min,max):
        if is_prime(x):
            primes.append(x)
    return primes

