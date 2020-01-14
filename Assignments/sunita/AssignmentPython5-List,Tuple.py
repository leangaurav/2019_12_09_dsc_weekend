#!/usr/bin/env python
# coding: utf-8

# In[1]:


#convert a tupple t =(1,2,3,4,5) to a list

t=list('12345')
print(type(t),t)


# In[2]:


#WAP to join a list and a tupple
L=['1,3,5,7']
T=(8,6,4,2)
t=list("8642")
LS=L+t
print(LS)


# In[3]:


#What is the difference between list and tupple
#The main difference between lists and a tuples is the fact that 
# lists are mutable whereas 
# tuples are immutable


# In[4]:


#Print the list in reverse order
L=['a','b','c','A','C']
l= L[::-1]
print(l)


# In[5]:


# print Elements at odd indexes from a list (Do not use loop)
l=[10,11,20,21,30,31,40,41]
L=l[1:8:2]
print('odd index elements are',L)


# In[6]:


#how many ways you can copy a list 
#1. Slicing -->ex .
a=[1,2,3,4]
b=a[:]
print(b) ##the item in list a are same as b.. a and b are 
#different object as their id's are different
id(a),id(b)

#2.Copying using list() function , it is used to create list 
#object from any iterables
a=[1,2,3,4]
b=list(a)
print(b)
id(a),id(b)

#3.copying using copy() method.this exactly copies list to to another lis
a=[10,20,30,40]
b=a.copy()
id(a),id(b)


# In[7]:


# Predict output
n_list =["Happy",[2,0,1,5]]
print(n_list[0][1])
print(n_list[1][3])


# In[8]:


#predict output
odd = [2,4,6,8]
odd[0] = 1
print(odd)
odd[1:4]=[3,5,7]
print(odd)


# In[12]:


# predict output
odd =[1,3,5]
odd.append([7,9])
odd
odd.extend([11,13])
odd


# In[18]:


# note predict output
x = 1,2,3 ;print(type(x))
x = (1) ;print(type(x))
x = 1 ;print(type(x))
x = 1, ;print(type(x))


# In[26]:


#try to represent a matrix with following data in python
# 1  2  3
# 4  5  6
# 7  8  9
l= [1, 2, 3]
print(l)
s= [4 ,5, 6]
print(s)
m= [7, 8, 9]
print(m)


# In[35]:


#predict output
t=tuple('string')
print(t)
print(60 in t)
print('60' in t)
print(t.count(10))
print(t.index(40))


# In[43]:


#WAP to input a string and print if it is palindrome or not
s = input('enter the string ').lower()
m=list(s)
if m==m[::-1]:
    print ('the string is palindrome')
else:
    print('the string is not palindrome')


# In[56]:


#Use the range method and create a tupple containing the following values:
#(20,15,10,5)

for i in range(20,4,-5):
    print(i)
        
        


# In[3]:


#WAP to convert string to list characters.
import string
s = input('enter any string ')
m=list(s)
print(m)


# In[5]:


#what is the return type of:
print(type( '1 2'.split()))
print(type( [1,3,2].sort()))
print(type('abc'.upper()))
print(type( 1 in [1,2]))


# In[ ]:




