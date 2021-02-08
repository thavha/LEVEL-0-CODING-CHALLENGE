def number_into_hours_and_minutes(number):
    
    hours = number//60
    minutes= number%60
    
    if hours > 1:
        hour = "hours"
        if minutes > 1:
            minute= "minutes"
        else:
            minute = "minute"
    else:
        hour = "hour"
        if minutes > 1:
            minute= "minutes"
        else:
            minute = "minute"
    time = (str(hours)+" "+hour+" " +str(minutes)+" "+ minute) 
    return time