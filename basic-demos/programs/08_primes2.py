
def is_prime(number):
    if number<2:
        return False
    test=2
    while test<number:
        if number%test==0:
            return False
        test+=1

    return True

def find_primes(min,max):
    count=min
    while count<max:
        if is_prime(count):
            print(count,end='\t')
        count+=1

    print()


find_primes(0,50)