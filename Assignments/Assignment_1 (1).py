#!/usr/bin/env python
# coding: utf-8

# In[1]:


#input temparature in fahrenheit and print in celsius 

#formula : C =((F-32)/(1.800) )  

f = int(input("Enter the temperture in Fahrenheit "))
C = ((f-32)/1.800)

print('temperture in celsius is: {}'.format(C))


# In[2]:


#WAP to input a number and print its squre and cube.

num = int(input('enter the number'))

sqare = num**2
cube = num**3

print('Squre of the is:{} and cube of the nuber is:{}'.format(sqare,cube))


# In[3]:


#WAP to input a number n and number m and 
#print the result of the following.

#n^2+m^2

n = int(input('enter the number n '))
m = int (input('enter the number m '))

res = n**2+m**2

print('result is :{}'.format(res))


# In[4]:


##WAP  to input a number M and N print result of M^N. 
#(use both ** and pow)

##using POW

M = int(input('enter number M '))
N = int(input('enter number N '))

result = M^N

print('result is:{}'.format(result))

##using **

M = int(input('enter number M '))
N = int(input('enter number N '))

result = M**N

print('result is:{}'.format(result))


# In[5]:


##write simple interest calculator

# formula : PRT/100
# where , 
# p = principle amount 
# R = rate ofinterest
# T = time period

P = int(input('enter the priciple amount in rupees '))
R = int(input('enter the rate of interest in percentage '))
T = int(input('enter Time period in years '))

SI = (P*R*T) /100

print('simple Interest is:{}'.format(SI))
       


# In[6]:


##input principle, rate,time and print compound interest and amount

##formula:

# cI = p*(1+(r/100))**n)-p

# Amount = p+CI
#where,

# CI is compound interest
# p is principle amount
# r is rate of interest 
# n is compounding time period 

p = float(input('enter the principal amount '))
r = float(input('enter the rate of interest inpercentage '))
n = float(input('enter the compounding time perion in years '))

CI = (p*(1+(r/100))**n)- p

print('compound intest for the given principle is: {}'.format(CI))

Amount = p+CI

print('total amount payable :{}'.format(Amount))


# In[7]:


# WAP to print sum of first n natural numbers.
#(n needs to be taken as input )

# using arthematic progression sum of n natural numbers is 
# defined by formula

# sum = n(n+1) / 2

n = int(input('enter the natural number n '))

s = (n*(n+1))/2

print('sum of the first n natural number is: {}'.format(s))


# In[8]:


# WAP to input two numbers and swap them 
# write using both temp variable and also pythonic way

#using temp

first = int(input('enter the first number '))
second = int(input(' enter the second the number '))
temp = 0

temp = first 
first = second 
second = temp

print("first number after swapping {}".format(first))
print("second number after swapping {}".format(second))

# using pythonic way
# a=a-b
# b=a+b
# a=b-a

first = int(input('enter the first number '))
second = int(input(' enter the second the number '))

first = first - second
second = first + second
first = second - first
    
print("first number after swapping {}".format(first))
print("second number after swapping {}".format(second))


# In[9]:


import string


# In[10]:



print(dir(string))


# In[11]:


print(dir(string.whitespace))


# In[12]:


print("hello")
#whitespace character
result=string.whitespace
print(result)


# In[13]:


#WAP to input single character and print its ascii values.

C = input('enter the character ')
print('Ascii value of entered character is: {}'.format(ord(C)))


# In[14]:


#WAP that takes area of a circle and gives back radius and circumference.

# Area = (pi)r^2                       
# circumference = 2(pi)r               ## pi = (22/7)or 3.14
# r = circumference /(2*pi)

import math 

Area = float(input('Enter area of a circle '))
radius = math.sqrt(Area/3.14)
print('radius of the circle is :{}'.format(radius))

circumference = 2*(math.pi)*radius

print('circumference of the circle is : {}'.format(circumference))


# In[15]:


# WAP where need to input marks in 5 subjects out of 100 and
# print percentage

sub1 = float(input('enter marks of sub1 out of hundred  '))
sub2 = float(input('enter marks of sub2 out of hundred  '))
sub3 = float(input('enter marks of sub3 out of hundred  '))
sub4 = float(input('enter marks of sub4 out of hundred  '))
sub5 = float(input('enter marks of sub5 out of hundred  '))

totalmarks = sub1+sub2+sub3+sub4+sub5
percentage = (totalmarks /500)*100

print('percentage is :{}'.format(percentage))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




