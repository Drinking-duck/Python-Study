#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''哈沙德数（Harshad number）是数论中的一个概念，指的是那些能够被自己的数字和整除的正整数集合。
因为自己的数字就是自己本身，显然1到9全是哈沙德数。
比如42的数字和是4 + 2 =6，42能被6整除，是一个哈沙德数，并且它是第20个哈沙德数。
（你记得42的梗吗？）'''
#202211580999 刘杨杨 计科一班
def harshad():
    for i in range(10,1000):
        if i<100:
            a=i//10
            b=i-a*10
            if i%(a+b)==0:
                print(i,' ',end='')
        if i>100:
            a=i//100
            b=(i-a*100)//10
            c=i-a*100-b*10
            if i%(a+b+c)==0:
                print(i,' ',end='')
harshad()

