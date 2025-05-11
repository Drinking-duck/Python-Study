#!/usr/bin/env python
# coding: utf-8

# In[14]:


'''读取“学习二十大：字频统计”
任务中二十大报告的字频表，将其封装为形如“[[王,200176],[刘,149887],[了,3455668]......]”的数据结构。
不使用sort()函数，对这个列表根据频次多寡，从大到小进行排序，并将排序好的列表，
以和之前任务相同的格式输出为chs_sort_20Report.txt'''
def char_type(s):
    chs=[]
    for c in s:
        if c not in chs:
            chs.append(c)
    return chs

def char_num(s,chs):
    num=[]
    for c in chs:
        num.append([c,s.count(c)])
    return num

def char_sort(s):
    for j in range(len(s)):
        for i in range(len(s)-1-j):
            if s[i][1]<s[i+1][1]:
                s[i],s[i+1]=s[i+1],s[i]
    return s
            
f=open(r'd:20Report.txt',encoding='utf-8')
txt=f.read()
f.close()
chs=char_type(txt)
num=char_num(txt,chs)
s=str(char_sort(num))


S=open(r'd:sort20Reoort.txt','w')
S.write(s)
S.close()

