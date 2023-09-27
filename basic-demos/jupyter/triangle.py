
class Triangle:
    pass

def create(s1,s2,s3):
    t=Triangle()
    t.s1=s1
    t.s2=s2
    t.s3=s3
    return t

def perimeter(t):
    #validation removed for simplicity
    return t.s1+t.s2+t.s3

# other functions not shown for simplicity
