#!/usr/bin/env python
# coding: utf-8

# In[22]:


'''
写函数，针对字符串s，回答以下问题：
字符串有几个单词？
字符串中每个单词各出现了多少次？采用成员为元组的列表返回结果，如[(love,3),(never,1)]这样
如果不使用count函数怎么做？
s=r'love never fails no matter you believe it or not but someone always asks why you have to go into love 
because love is forever is everlasting like the mountain shining far away after the long long  everlasting 
journey it is good it is always good for you and for me and for everyone someone and having no end no earth 
no answer least'
'''
#202211580999 刘杨杨 计科一班
s="love never fails no matter you believe it or not but someone always asks why you have to go into love because love is forever is everlasting like the mountain shining far away after the long long everlasting journey it is good it is always good for you and for me and for everyone someone and having no end no earth no answer least"

def Strusing(s:str):
    res=[]
    w_str=[]
    w_num=[]
    
    words=s.split()
    
    for i in words:
        flag=1
        for j in range(len(w_str)):
            if i==w_str[j]:
                flag=0
                w_num[j]+=1
                break
        if flag==1:
            w_str.append(i)
            w_num.append(1)
            
    for i in range(len(w_str)):
        res.append((w_str[i],w_num[i]))
    
    print(len(w_str))
    print(res)

print(Strusing(s))


