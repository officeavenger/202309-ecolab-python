#NOT RECOMMENDED
#from utils.dates import * #import everything

from utils.dates import date_to_week_day,days_in_month,day_name

def print_calendar_horizontal(month,year):
    startDay=date_to_week_day(1,month,year)
    days=days_in_month(month,year)
    
    for i in range(7):
        print(day_name(i)[0:3].upper(),end="\t")
    d=1
    i=0
    print()
    while(d<=days):
        if(i==0):
            print((startDay)*"\t",end="")
            i+=1
            
        for j in range(startDay,7):
            print(d,end="\t")
            d+=1
        print()
        startDay=0
    
