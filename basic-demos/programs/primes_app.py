from primes import find_primes
import sys

def main():
    args=[int(value) for value in sys.argv[1:]]
    if len(args)<2:
        print('Find All Primes in Range')
        min = int(input("min?"))
        max = int(input("max?"))
    else:
        min=args[0]
        max=args[1]

    print(f'finding primes in range {min}-{max}')    
    primes= find_primes(min,max)
    for prime in primes:
        print(prime,end="  ")
    print()


main()