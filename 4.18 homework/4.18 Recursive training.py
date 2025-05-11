#!/usr/bin/env python
# coding: utf-8

# In[20]:


'''写函数，以递归思想完成以下任务：
1.写递归函数my_rec_sum(a,b)完成累加操作，并测试从1累加到100
2.写递归函数DigitSum(n)，输入一个非负整数，返回组成它的数字之和例如，调用DigitSum(1729)，
则应该返回1+7+2+9，它的和是19。输入：1729，输出：19
3.刘院士爬楼上课需要走n阶台阶，因为他打中锋并且罚篮神准，所以他每次可以选择走一阶或者走两阶，
那么他一共有多少种走法？LiuStep(n)，以10为例进行测试。
填写答案'''

#n=n+(n-1)
def my_rec_sum(a:int,b:int):
    if b==a:
        return b
    else:
        return b+my_rec_sum(a,b-1)   
print(my_rec_sum(2,5))


# In[9]:


def DigitSum(n:int):
    if n/10==0:
        return n
    else:
        return n%10+DigitSum(int(n/10))
print(DigitSum(1729))


# In[16]:


def LiuStep(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return LiuStep(n-1)+LiuStep(n-2)
print(LiuStep(10))

