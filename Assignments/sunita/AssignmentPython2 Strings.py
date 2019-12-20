#!/usr/bin/env python
# coding: utf-8

# In[1]:


##Guess output of each slice:

s ="Python is Object Oriented"
print(s[-1])
print(s[::-1])
print(s[:-1])
print(s[1:1])
print(s[4:10])
print(s[::2])
print(s[2:-5])


# In[2]:


##what error do you see for following statements:
s=''
print(s[1])

#error : string index out of range


# In[5]:


# Do you get any error for the following code, if not give the output

s='Gaurav'
print(s[1])  #output : a


# In[6]:


# find the output of the following 
s = 'a b cd'
print(len(s))
print(s[::2])
print(len(s[::2]))


# In[7]:


s="a#b#c#d#"
print(s.split())
print(s.split('#'))
l=s.split('#')
s='$'.join(l)
print(s)


# In[8]:


s =' Gaurav'
s=s[::-2][::-2]
print(s)


# In[9]:


print(1>2)


# In[10]:


print(4%2, 5%2, 2%5, sep=',')


# In[11]:


s='abcba'
s.upper()
print(s)
print(s.count('A'),end=',')
print(s.count('A',2,4),end=',')
print(s.count('a',2,4),end=',')


# In[12]:


##WAp to input a string and remove all spaces from it
s = 'a b cd'
print(s[::2])


# In[13]:


#what does this symbol denote:
import string
print(string.whitespace)


# In[14]:


# #WAP to print all methods(functions/operators)
# available in a string(Hint:dir())
print(dir(string))


# In[15]:


#write statements to check if rstrip method is available in the str class.
#(Hint:use the find function or in)
import string

print('python'.find('rstrip'))


# In[16]:


s=print('*****')

print('  *\n'*4)


# In[19]:


#WAP to input string and spit into two halves.

s= input('enter any string')
res_first= s[:len(s)//2]
print(res_first)
res_second= s[len(s)//2:]
print(res_second)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




