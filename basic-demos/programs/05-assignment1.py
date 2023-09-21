
total=int(input("total values?"))

count=0
max=None

while count<total:
    count+=1
    value=int(input(f"number#{count}? "))
    if max==None or value>max:
        max=value

print(f'highest is {max}')

