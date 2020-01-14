#!/usr/bin/env python
# coding: utf-8

# In[1]:


#WAp to input 2 strings and swap the strings

s1=input('enter the string s1 ')
s2=input('enter the string s2 ')
temp=0

temp=s1
s1=s2
s2=temp

print('string s1 is :',s1 )
print('string s2 is :',s2 )
 


# In[36]:


#WAP generate 4 random numbers in the range 0-26 and print their average

import random
r1=random.randint(0,26)
r2=random.randint(0,26)
r3=random.randint(0,26)
r4=random.randint(0,26)

print('the random numbers are',r1,r2,r3,r4)
average = (r1+r2+r3+r4)//4
    
print(average)

r=[]
i=1
print('enter the number of random numbers')
n=int(input())

while i<=n:
    r.append(random.randint(0,26))
    i+=1
print(r)
ave=(sum(r)/n)
print(ave)

import random as r
res=r.sample(range(0,26),4)
print(res)
print(sum(res)//4)


# In[3]:


##WAP to generate and print a random uppercase or lowercase alphabet.
##create a string containing all alphabets and then 
#select a random alphabet.
#check the module string

import string

dir(string)


# In[4]:


import random
print(string.ascii_letters)
print(string.ascii_letters[random.randrange(len(string.ascii_letters))])
print([random.choice(string.ascii_letters)])


# In[5]:


#WAP to get_si that takes principle,rate and time as arguments 
#and returns the simple interest

p=int(input('enter the priciple amount'))
r=float(input('enter the rate of interest'))
t=int(input('enter the time period'))

def get_si(p,r,t):
    si=(p*r*t)/100
    return si
get_si(p,r,t)


# In[6]:


#WAP to get_amount() that takes principle,rate and time as arguments and 
#return the total amount using the get_si function from the above to 
#calculate the si .
# also  provide rate =10 and time = 1 as default arguments

r=10
t=1
def get_amount(p,r,t):
        amount=p+get_si(p,r,t)
        return amount
    
get_amount(p,r,t)


# In[7]:


#WAP to get_ci that takes the principle ,rate and time as arguements and 
#returns the compound interest
#ci= p*(1+(r/100))**n-p

p=int(input('enter the principle amount'))
r= float(input('enter the rate of interest'))
t=int(input('enter the time period'))

def get_ci(p,r,t):
    ci=p*(1+(r/100))**t-p
    return ci
get_ci(p,r,t)


# In[8]:


##WAP get_q_r()taking 2 numbers as parameters and returns the quotient 
#and remainder in the from of a tuple

n1 =int(input('enter the first number'))
n2 =int(input('enter the second number'))

def get_q_r(n1,n2):
    q= n1/n2
    r=n1%n2
    return q,r
get_q_r(n1,n2)


# In[13]:


#WAP to find the length of hypotenuse of a right angled traingle , 
#input the height and base from the user

#hypotenuse=sqrt(b**2+h**2)

import math
dir(math)

b = int(input('enter the base value of a triangle'))
h = int(input('enter the height of the right angled traingle'))

def get_hypot(b,h):
    hypo=math.sqrt(b**2+h**2)
    return hypo
get_hypot(b,h)


# In[19]:


#WAP to input number of seconds and print in days ,hours,minuts
#and seconds 
# ex:input =10000
#  output= 0 days 2 hours 46 min 40n seconds

time = float(input("enter the time in seconds"))
day = time//(24*3600)
time = time%(24*3600)
hour=time//3600
time= time% 3600
minutes=time/60
time=time%60
seconds = time
print('{} days {} hours {} minutes {} seconds'.format(day,hour,minutes,seconds))


# In[25]:


##WAP to check your version of python interpreter without 
# opening the interpreter 
# (which command needs to be used on the command line)

import sys
print(sys.version)


# In[27]:


#find the output
x=2
x*=3
x=x%4
y= -x
print(x,y)


# In[28]:


#find output

def funct():
    pass
print(funct())


# In[ ]:


## read and complete till part -3:(part -4 after OOPs)

#https://medium.com/the-python-diary/getting-around-complex-numbers-77308982178d

