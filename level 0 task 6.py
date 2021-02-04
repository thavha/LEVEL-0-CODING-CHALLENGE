#!/usr/bin/env python
# coding: utf-8

# In[1]:


def maximum_number(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

