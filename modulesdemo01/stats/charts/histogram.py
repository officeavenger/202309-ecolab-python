def plot_histogram( frequency_table):
    design='==='
    for (item,frequency) in frequency_table.items():
        print(f'{item}|{design*frequency} {frequency}')