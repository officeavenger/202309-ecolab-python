import utils.console_input as console
from stats.alogrithms.frequency import generate_frequency
from stats.charts.histogram import plot_histogram

def main():
    numbers = console.input_multiple('numbers? ')    
    table = generate_frequency(numbers)
    plot_histogram(table)
    
    


main()