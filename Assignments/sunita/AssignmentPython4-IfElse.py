#!/usr/bin/env python
# coding: utf-8

# In[2]:


#WAP to input 2 numbers and check whether the first is devisible by 
# the second and print true or false depending on the devisibility

num1 = int(input('enter the first number '))
num2 = int(input('enter the second number '))

if num1%num2==0:
    print('TRUE')
else:
    print('False')


# In[3]:


#In the palindrome example, make the code sensitive.
# i.e,Naman should also be treated as a palindrome 
# (HINT :first convert to either upper or lower case )

import string

s = input('please enter a string ').lower()

if s == s[::-1]:
    print('The string is palindrome')
else:
    print('The string is not palindrome')


# In[4]:


##WAP to input the sides of a trinagle and print wheather 
# equilateral(all sides equal),
# isosceles(2sides equal),
# scalene(no sides are equal)

s1 = int(input('enter the side s1 of a traingle'))
s2 = int(input('enter the side s2 of a traingle'))
s3 = int(input('enter the side s3 of a traingle'))

if s1==s2==s3:
    print("Equilateral Traingle")
elif s1==s2:
    print("Isosceles Traingle")
elif s1==s3:
    print("Isosceles Traingle")
elif s2==s3:
    print("Isosceles Traingle")
else:
    print('scalene Traingle')


# In[5]:


#WAP to input a number and print if it is even or odd

num1=int(input('Please enter the number ' ))

if num1%2==0:
    print('The number is even')
else:
    print('The number is odd')


# In[6]:


# WAP to input age and print the respective text depending
# on the age ranges as present in the table
# 0 <= age <=12 ,child
# 13<= age <=17 ,Teen
# 18<= age <=50 ,Adult
# 51<= age <=100, senior citizen
# age > 100   , congratualations

age = int(input('enter the age of a person '))

if 0<= age <=12:
    print('Child')
elif 13<= age <=17:
    print('Teen')
elif 18<= age <=50:
    print('Adult')
elif 51<= age <=100:
    print('Senior citizen')
else:
    print('Congratulations')


# In[7]:


#WAP to input year (check if the user enters a valid year.
# should be 4-didgit number and should not be negative)and 
# print wheather leaf year or not .
# (if really interested in why you also check the devisibility by 400 just 
#  google the exct time it takes to revolve around the sun)

import math

year = int(input("Enter a year: "))  

if (year % 4==0): 
   
   if (year % 100==0): 
       
       if (year % 400==0):  
           print("{0} is a leap year".format(year))  
       else:  
           print("{0} is not a leap year".format(year))  
   else:  
       print("{0} is a leap year".format(year))  
else:  
   print("{0} is not a leap year".format(year))  


# In[8]:


# WAP to input a string and convert it to upper case if the number of 
# characters is odd and convert to lower case otherwise

import string
s = input('Please enter the string ')

if (len(s)%2)==0:
    
    s1=s.upper()
    
    print('number of characters in {} is even'.format(s1))
     
else:
    s2=s.lower()
    print('number of characters in {} is odd'.format(s2))


# In[9]:


#WAP to input a string and print veg if the string doesnt contain the word
# egg.otherwise print Non-veg. As usual eggs can be both big and small

s =input('please enter the food menu ').lower()
if "egg" in s :
    print ('Non-veg')
else :
    print('Veg')


# In[10]:


# give output of:
if not 1:
    print('False')
else:
    print('True')
    
## second programm to find the output

if 1:
    print('True')
else:
    print('False')


# In[11]:


#Give output of

if 'a'> 'A':
    print('weird!!')
else:
    print('Make sense')
    
##second program

a=[1,2,3,4]

if 1>1:
    a=a[::-1]
else:
    a=a[-1::-1]
print(a)


# In[22]:


#WAP to input marks in 5 subjects and 
# print the grade as per following logic
# Percentage between 90-100 'GRADE A'
# Percentage between 80-89 'GRADE B'
# Percentage between 60-79 'GRADE C'
# Percentage less than 60 'GRADE F'

sub1=int(input('Enter the marks in sub1 '))
sub2=int(input('Enter the marks in sub2 '))
sub3=int(input('Enter the marks in sub3 '))
sub4=int(input('Enter the marks in sub4 '))
sub5=int(input('Enter the marks in sub5 '))

pec = 100*((sub1+sub2+sub3+sub4+sub5)/500)

print(pec)

if ((pec<=100)&(pec>=90)):
    
    print('GRADE A')
    
elif ((pec<=89)&(pec>=80)):

     print('GRADE B')

elif ((pec<=79)&(pec>=60)):
    
    print('GRADE C')
elif (pec<60):
    print('GRADE F')
    


# In[40]:


#WAP to input age and salary and calculate Tax as per tax 
# rates of following table
# salary (0 - 250000) --> no tax
# salary (250000 - 500000) &(age<60)--> 5%
# salary (250000 - 500000) &(age>= 60)-->3%
# salary (500000 - 1000000) & (age<60)-->10% 
# salary (500000 - 1000000) & (age>=60)-->8%
# salary>10,00,001 & (age<60)--> 15%
# salary>10,00,001 & (age>=60)--> 12%

salary = int(input ('please enter the annual income'))
age = int(input('enter your age as on dec 2019  '))

if salary>10000001:
    if age>=60 :
        tax= 0.12*salary
        print('Tax is',tax)
    else:
        tax=0.15*salary
        print('Tax is {}',tax)
elif (salary>=500000)and (salary<=1000000):
    if age >= 60 :
        tax= 0.08*salary
        print('tax is',tax)
    else:
        tax= 0.10*salary
        print('tax is',tax)
elif (salary>=250000) and (salary<=500000):
    if age >= 60 :
        tax=0.03*salary
        print('tax is',tax)
    else:
        tax=0.05*salary
        print('tax is',tax)
else:
        tax=0*salary
        print('NO TAX ')


# In[48]:


#TRy each of the below statements seperately 
# (remember difference between stetaments and expression) on the python 
# interpreter and guess the output before trying.

print(20 if not 1 == 1 else 10)
print(30 if not 1 == 1 else 20 if 'a' < 'A' else 10)
print(40 if not 1 == 1 else 30 if 'a' <'A' else 20 if '' else 10)
print('No' if not 1 == 1 else ('No' if 'a' < 'A' else ('OMG' if 'oh !!'else '')))


# In[57]:


#WAP : bmi() that takes the weight in kg and height in cm of a person,
# calculate and returns the BMI.
# Write this code that calls this function after taking height and weight 
# as inputs and the prints underweight, normal,overweight or obsese 
# depending on the value of BMI.
# refer the link for the ranges:
#     https://en.wikipedia.org/wiki/body_mass_index

# BMI = Mass in kg /(height in meter)**2

meter =100
h= int(input('enter the height in centimeters'))
w= int(input('enter the weight in kg'))
def bmi(h,w):
    bmi=w/((h/100)**2)
    return bmi
bmi=bmi(h,w)
print('The BMI is',bmi)

# calling bmi function 

if (bmi<18.5):
    print('underweight')
elif (bmi>=18.5 and bmi <24.9):
    print('Healthy')
elif (bmi>=24.9 and bmi<30):
    print('Overweight')
elif (bmi >= 30):
    print('Suffering from Obesity')


# In[2]:


#Take input of age 3 people  by user and determine oldest and 
# youngest among them.
a = int(input('enter age of the first person '))
b = int(input('enter age of the second person'))
c = int(input('enter age of the third person'))

def young(a,b,c):
    
    if (a<b) and (a<c):
         print('person a is youngest')
    elif(b<a)and (b<c):
         print('person b is youngest')
    else:
         print('Person c is youngest')
def old(a,b,c):
    if (a>b) and (a>c):
         print('person a is oldest')
    elif(b>a)and (b>c):
         print('person b is oldest')
    else:
         print('Person c is oldest')
young(a,b,c)
old(a,b,c)


# In[4]:


#WAP to input a number and check if numbers is divisible by both 5 and 7
num = int(input('enter a number'))
if (num%5==0) and (num%7==0):
    print('the number {} is divisible by both 5 and 7'.format(num))
else:
    print('the number {} is not divisible by both 5 and 7'.format(num))


# In[ ]:




