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
