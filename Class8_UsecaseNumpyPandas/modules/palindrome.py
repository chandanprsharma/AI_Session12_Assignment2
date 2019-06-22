#!/usr/bin/env python
# coding: utf-8

# In[11]:


# Fibonacci Series
def isPalindrome(inputStr):
    return (inputStr.lower() == inputStr[::-1].lower())

