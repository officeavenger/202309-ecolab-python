

def find_primes(min,max):
    number=min
    while number<max:
        test=2
        if number>1:
            while test<number:
                if number%test==0:
                    break
                test+=1
            else:
                print(number,end='\t')

        number+=1

print()

find_primes(0,50)