

def input_type(prompt,type=int):
    return type(input(prompt))

def input_multiple(prompt,sep=' ',type=int):
    x=input(prompt)
    items=x.split(sep)
    return [type(value) for value in items if value!='' and value!=' ' ];
    