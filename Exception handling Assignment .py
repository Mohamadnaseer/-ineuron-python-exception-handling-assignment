#!/usr/bin/env python
# coding: utf-8

# #  Exception handling Assignment
1. Write a function to compute 5/0 and use try/except to catch the exceptions.
# In[42]:


def divide():
    return 5/0

try:
    divide()
except ZeroDivisionError as zero:
    print("An interger/number can't be divisible by Zero")
except:
    print("Any other exception")

2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].

Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]


Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
# In[8]:


Subject=["Americans", "Indians"]
Verb=["play", "watch"]
Object=["Baseball", "Cricket"]

All_sentences=[(sub +" "+ ver +" " + obj) for sub in Subject for ver in Verb for obj in Object]
for sentence in All_sentences:
    print(sentence)

