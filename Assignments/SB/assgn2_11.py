x=input('Enter String:').split(' ')
n=len(x)
i=0

#print(*x, sep = '\n')
for i in range(n):
    print(len(x[i]), x[i].upper())
    i+=1
