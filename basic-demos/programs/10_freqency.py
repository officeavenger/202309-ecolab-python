
def freq(values):
    f=dict()

    for i in range(len(values)):
        c = values.count(values[i])
        f.update({values[i]:c})
    return f

def value_count(seq,value):
    c=0
    for v in seq:
        if v==value:
            c+=1
    return c

#sameple values = [2,2,2,9,1,2,2,2,8,4 ... ] (100000 values, 15 unqiue types)
def frequency1(values):
    f=dict()

    for value in values:
        c = value_count(values,value)
        f.update({value:c})
    return f


def frequency2(values):
    keys=set()
    table=dict()

    for value in values: # n times
        keys.add(value)

    #now s is unique set of values 15
    for key in keys:  # k*n time
        f= values.count(key)
        table.update({key:f})

    
    return table


def frequency3(values):
    
    table=dict()

    for value in values:
        if value in table:
            #table.update({value:table[value]+1})
            table[value]+=1
        else:
            table[value]=1

    return table

def frequency(values):
    
    table=dict()

    for value in values:
        table[value]=table.get(value,0)+1

    return table



def main():    
    values=[2,2,3,9,2,2,1,4,1,1,2,2,3,9]
    f=frequency(values)
    print(f)

    values2=(4,4,4,1,1,1,2,2)
    f2=frequency(values2)
    print()
    print(f2)

main()