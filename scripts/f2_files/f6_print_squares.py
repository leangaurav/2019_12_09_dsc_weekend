f1 = open('squares.txt', 'w')

for i in range(1,11):
    print(i,'=',i*i, file = f1)

f1.close()
    