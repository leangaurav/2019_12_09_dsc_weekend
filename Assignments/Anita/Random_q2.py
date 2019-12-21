import random
l=[]

for x in range(4):
	y=random.randrange(26)
l.append(y)
sum=0
for sum in l:
    sum+=x
    Avg=sum/4
print("Sum is",sum)
print("Averae is",Avg)

#output:
Sum is 24
Averae is 6.0

