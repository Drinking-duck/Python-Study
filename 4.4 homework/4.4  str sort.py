#!/usr/bin/env python
# coding: utf-8

# In[11]:


'''写函数，不使用python内置函数，对一个长字符串进行排序。测试样例“loveneverfailsnomatteryoubelieveitornot”
提示：字符串是可以比较大小的
提示：本题有多种做法，但可以只提交一种'''
def change(n:str):
    res=[]
    for i in n:
        res.append(i)
    return res

def sort(n:list):
    for j in range(len(n)):
        for i in range(len(n)-1-j):
            if n[i]>n[i+1]:
                n[i],n[i+1]=n[i+1],n[i]
    return n

n="loveneverfailsnomatteryoubelieveitornot"
print(''.join(sort(change(n))))    
        

