def generate_frequency(values):
    
    table=dict()

    for value in values:
        table[value]=table.get(value,0)+1

    return table