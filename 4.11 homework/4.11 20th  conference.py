#!/usr/bin/env python
# coding: utf-8

# In[65]:


'''请编写程序，读取文本文件20thReport。
并将总书记在二十大报告中所有包含“中国式现代化”的句子写入文本文件ChineseMordernization中。
提示操作顺序：
1读取文件；
2按照换行和句号切分文本，形成列表；
3遍历列表并找寻包含关键词的成员；
4将这些成员写入文件中。'''

file=r'd:20thReport.txt'
f=open(file,encoding='utf-8')
txt=f.read()

t1=str(txt)
l=t1.split('\n')

t2=str(l)
m=t2.split('。')

Line=[]
for line in m:
    n=str(line)
    if n.count("中国式现代化")>0:
        print('Line    ',line)
        Line.append(line)
        
f=open(r'd:Chinese modern.txt','w')
f.writelines(Line)
        
f.close()

