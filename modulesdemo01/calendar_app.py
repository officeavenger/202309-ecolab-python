from utils.calendar import print_calendar_horizontal
import utils.console_input as console

def main():
    date=console.input_multiple("mm/yyyy? ",'/')
    print_calendar_horizontal(*date) # print_calendar_horizontal(date[0],date[1])

main()

