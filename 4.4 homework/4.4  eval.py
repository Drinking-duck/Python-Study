#!/usr/bin/env python
# coding: utf-8

# In[11]:


'''
写函数，读入一行字符串，里面是三个整数进行加减乘除的字符串如：1+2+3或1x4/5。
算式中没有括号。请将三个数字提取成整型数，赋值给x,y,z。
并计算出结果。'''

s="1+4*5"
def changestr(s:str):
    x,y,z=0,0,0
    m=0
    x=eval(s[0])
    y=eval(s[2])
    z=eval(s[4])
    m=eval(s)
    return x,y,z,m

print(changestr(s))









