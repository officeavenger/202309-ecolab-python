
def print_calendar_horizontal(month,year):
    startDay=date_to_week_day(1,month,year)
    days=days_in_month(month,year)
    week=['Sun','Mon','Tue','wed','thu','fri','Sat']
    for i in week:
        print(i.upper(),end="\t")
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
    
