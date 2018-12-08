#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#minim
import numpy as np

def mini(a):
    minim = a.min()
    if minim > 0:
        minim = 0
    else: 
        minim = 1 + (-1)*minim
    return minim

