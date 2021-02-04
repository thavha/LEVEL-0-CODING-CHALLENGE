#!/usr/bin/env python
# coding: utf-8

# In[62]:


def number_into_hours_and_minutes(number):
    a= 'hours'
    b= 'hour'
    c= 'minute'
    d= 'minutes'
    hours = number//60
    minutes= number%60
    if hours > 1 and minutes >1:
        return (str(hours)+" "+a+" " +str(minutes)+" "+ d)
    elif hours > 1 and minutes ==1:
        return (str(hours)+" "+a+" " +str(minutes)+" "+ c)
    elif hours == 1 and minutes >1:
        return (str(hours)+" "+b+" " +str(minutes)+" "+ d)
    elif hours ==0 and minutes ==0:
        return 0
    elif hours ==0 and minutes > 1:
        return (str(minutes)+" "+ d)
    elif hours ==0 and minutes ==1:
        return(str(minutes)+" "+ c)
    elif hours >1 and minutes ==0:
        return (str(hours)+" "+a)
    elif hours ==1 and minutes ==0:
        return (str(hours)+" "+b)
    elif hours ==1 and minutes >1:
        return (str(hours)+" "+a+" " +str(minutes)+" "+ d)
    elif hours ==1 and minutes ==1:
        return (str(hours)+" "+b+" " +str(minutes)+" "+ c)