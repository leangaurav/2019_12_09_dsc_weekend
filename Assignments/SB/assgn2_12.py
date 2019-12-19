x=input('Enter string:')
n=len(x)
#m=n//2
print('first part:',x[:n//2])
if n%2 ==0:
    print('Second Part:',x[n//2:])
else:
    print('Second Part:',x[n//2+1:])
