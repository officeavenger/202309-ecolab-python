import maths.primes as p



def main():
    for prime in p.find_primes(2,100):
        print(prime,end=' ')

main()