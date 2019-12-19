#!/usr/bin/env python
# coding: utf-8

# In[1]:


# predict output 

s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
print(len(s1),len(s2))


# In[2]:


# WAP to input a string and print its length

strg = input('enter the string  ')
print('lenth of the string is :{}'.format(len(strg)))


# In[3]:


#WAP to input 2 numbers and print their sum and difference

num1 = int(input('enter num1 '))
num2 = int(input('enter num2 '))

addresult = num1 + num2
diffresult = num1 - num2

print('sum of the two numbers is:{}'.format(addresult))
print('difference of the result is:{}'.format(diffresult))


# In[4]:


# predict output

s1 = 'ab'
s2 = 'de'
s3 = s1+s2
print(s3)


# In[5]:


# predict output

s1 = 'ab'*4
print(s1)


# In[6]:


# predict output

s1 = 'ab\n'*4
print(s1)


# In[13]:


# WAP to input a string s and a number n . 
#print the string n times on the screen each should appear in seperate line 
#(do not use any kind of loops, use the multiplication operator)

s = input('enter any string ')
n = int(input('enter the number n '))
s1 = (s+'\n')*n 
print(s1)


# In[1]:


#predict output 
res = print('gaurav')
print(res)


# In[2]:


#predict output

res = len('tuteur.py@gmail.com')
print(type(res))


# In[5]:


#predict output

s1 = 'Gaurav'
s2 = 'tuteur.py@gmail.com'
s3 = s1+'\n'+s2
print(type (s3))
print(len(s3))
print(s3)


# In[19]:


# find the name of the function to find the square root.
# (see all the options available in dir()of math)

import math

dir(math)
dir(math.sqrt)


# In[21]:


s = math.sqrt(98)
print(s)


# In[22]:


#WAP to input a number and printits square root

num1 = int(input('enter the number'))

res = math.sqrt(num1)

print('square root of num1 is :{}'.format(res))


# In[23]:


#WAP to input 4 numbers from the user and print their average

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())

Average = (num1+num2+num3+num4)/4

print('Average of the 4 numbers is:{}'.format(Average))


# In[32]:


#use the help function to check what the abs fuction in python does

help(abs)
dir(abs)
x = 67/7
abs(x)


# In[35]:


# What is the output of this code when run from python script

print(__name__)


# In[37]:


#does the dir of int class an attribute __name__

##NO 

dir(int)


# In[44]:


#predict the output
print(__name__)
print(__builtins__.__name__)
print(int.__name__)
    

