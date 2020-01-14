#!/usr/bin/env python
# coding: utf-8

# #WAP to print first n natural numbers (input n from the user)

# In[3]:



n = int(input('enter n upto which natural numbers will be printed '))
for i in range(1,n+1):
    print(i)

n = int(input('enter the number n '))
i=1
while i<=n :
    print(i)
    i=i+1


# #WAP to find sum of first n natural numbers.
# # sum = n(n+1)/2

# In[4]:


n = int(input(' enter the value for n '))
sum = (n*(n+1))/2
print('sum of the natural numbers',sum)


# In[5]:


##WAP to print first n natural numbers in reverse order

n=int(input('enter value of n '))
for i in range(n,0,-1):
     print(i)
        


# # WAP to input a number and print its factorial

# In[6]:


n = int(input('enter number n '))
fact =1
for i  in range(1,n+1):
    fact=fact*i
print('factorial of a number is {} '.format(fact))

import math
n = int(input('enter the number '))
print('factorial of a number is ',math.factorial(n))


# #WAP to print Fibonacci sequence till n.

# In[7]:


# 0,1,1,2,3,5,8,13....
nterms = int(input('how many terms ? '))
n1,n2 = 0,1
count = 0

if nterms <= 0:
    print('Please enter the positive sequence.')
elif nterms ==1:
    print(n1)
else :
    print('Fibonacci sequence :')
    while count < nterms :
        print(n1)
        nth = n1+n2
        n1 = n2
        n2 = nth
        count = count +1


# #WAP to print all digits of a number input from user.

# In[8]:


def get_digits(n):
    s = str(n)
    num = []
    for i in s:
        num.append(int(i))
    return num

s = input('Enter a number: ')
for digit in get_digits(s):
    print(digit)
    


# ##WAP to find sum of all digits of a number.

# In[9]:



num = int(input('enter the number'))
sum = 0
while num>0:
    d= num%10
    num = num//10
    sum= sum+d
print('The sum of the digits of a number is',sum)


# In[11]:


#WAP to find of the following series given n as input from the user.
# 1+2!+3!+4!+5!+....n!
# where n! denotes the factorial of number n 
n = int(input('enter value of n '))
sum=0
fact=1
for i in range(1,n+1):
    fact=fact*i
    sum=sum+fact
print('sum of factorial of n numbers is :',sum)


# # WAP to input base and exponent and print result without using inbuilt 
# # function pow(use for or while loop)

# In[12]:


base = int(input('enter base value '))
exponent = int(input('enter exponent value '))
power = 1
for i in range(1,exponent+1):
    power=power*base
print(power)

##using while loop
base = int(input('enter base value '))
exponent = int(input('enter exponent value '))
power = 1
i=1
while i<=exponent:
    power=power *base
    i=i+1
print(power)


# #Print the following patterns:

# In[13]:



for i in range(0,5):
    for j in range(0,i+1):
        print('*',end=' ')
    print('\r')


# In[14]:


for i in range(5,0,-1):
    for j in range(1,i+1):
        print('*',end=' ')
    print('\r')


#  # Function to demonstrate printing pattern 

# In[15]:



def pypart2(n): 
      
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 2
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
pypart2(n) 


# # Function to demonstrate printing pattern triangle 

# In[16]:



def triangle(n): 
      
    # number of spaces 
    k = 2*n - 2
  
    # outer loop to handle number of rows 
    for i in range(0, n): 
      
        # inner loop to handle number spaces 
        # values changing acc. to requirement 
        for j in range(0, k): 
            print(end=" ") 
      
        # decrementing k after each loop 
        k = k - 1
      
        # inner loop to handle number of columns 
        # values changing acc. to outer loop 
        for j in range(0, i+1): 
          
            # printing stars 
            print("* ", end="") 
      
        # ending line after each row 
        print("\r") 
  
# Driver Code 
n = 5
triangle(n) 


# #Print the following number patterns

# In[17]:


n= int(input('enter number'))
for i in range(1,n+1):
    print(str(i)*i)


# In[18]:


n = int(input('enter number '))
for i in range(1,n+1):
    line= ' '
    for j in range(1,i+1):
        line=line+str(j)
    print(line)


# In[19]:


n = int(input('enter a number '))
i = 1
while(n):
    print(str(n)*i)
    i+=1
    n-=1


# In[22]:


n = int(input('enter number : '))
height = int(input('enter the height '))
for i in range (1,height+1):
    print(' '*(height-1)+str(i)*i)


# In[ ]:


# Print the following character patterns:


# In[27]:


alp = ord('A')
n = 5
for i in range (1,n+1):
    line= ' '
    for j in range(1,i+1):
        line =line+chr(alp)
        alp+=1
    print(line)


# In[26]:


alp= ord('A')
n=5
for i in range(1,i+1):
    line=' '
    for j in range(1,i+1):
        line=line+chr(alp)
        alp+=1
    print(line)


# In[39]:


alp = ord('A')
n=5
for i in range(1,n+1):
    s = ''
    for j in range(0,i):
        s += chr(alp+j)
    s = s + s[-2::-1]
    print(' '*(n-i),s)


# In[ ]:




