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
    result=[]
    while count<max:
        if is_prime(count):
            result.append(count)
        count+=1

    return result


def test_is_prime(show_failed_only=False):
    test_values={2:True, 1:False, 5:True, -5:False,0:True, 12:False}
    for number,expected in test_values.items():
        actual = is_prime(number)
        if actual != expected:
            print(f'FAILED\tfor {number}')
            print(f'\tExpected = {expected}\tActual={actual}')
        elif not show_failed_only:
            print(f'PASSED\tfor {number}')

def test_find_primes(show_failed_only=False):
    test_data=[[2,10,4],[0,50,15], [50,100,10],[0,100,20]]
    for min,max,expected in test_data:
        actual=len(find_primes(min,max))
        if actual==expected :
            if not show_failed_only:
                print(f'PASSED FOR {min}-{max}')
        else:
            print(f'FAILED FOR {min}-{max}')
            print(f'\texpected={expected}\tactual={actual}')


if __name__=='__main__':
    #print('module name is ',__name__)
    test_is_prime()
    test_find_primes()