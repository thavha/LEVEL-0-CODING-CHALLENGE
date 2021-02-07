def number_into_hours_and_minutes(number):
   
    hours = number//60
    minutes= number%60
    
    while hours >= 1:
        if hours >1:
            a= 'hours'
            if minutes >1:
                d= 'minutes'
                return (str(hours)+" "+a+" " +str(minutes)+" "+ d)
            elif minutes ==1:
                d= 'minute'
                return (str(hours)+" "+a+" " +str(minutes)+" "+ d)
            else:
                return (str(hours)+" "+a)
        else:
            a= 'hour' 
            if minutes >1:
                d= 'minutes'
                return (str(hours)+" "+a+" " +str(minutes)+" "+ d)
            elif minutes ==1:
                d= 'minute'
                return (str(hours)+" "+a+" " +str(minutes)+" "+ d)
            else:
                return (str(hours)+" "+a)       
    else:
        if minutes >1:
            d= 'minutes'
            return (str(minutes)+" "+ d)
        elif minutes ==1:
            d= 'minute'
            return  (str(minutes)+" "+ d)
        else:
            a ='hour'
            return (str(hours)+" "+a)