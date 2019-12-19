# WAP to print sum of first n natural numbers.
#(n needs to be taken as input )

# using arthematic progression sum of n natural numbers is 
# defined by formula

# sum = n(n+1) / 2

n = int(input('enter the natural number n '))

s = (n*(n+1))/2

print('sum of the first n natural number is: {}'.format(s))