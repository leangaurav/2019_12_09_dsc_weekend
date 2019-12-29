with open('squares.txt', 'w') as f1:# context handlers
    print(f1.closed)
    for i in range(1,11):
       # f1.write( str(i) + "=" + str(i*i) + '\n')
        
        f1.write( "i=%d = %f\n" %(i, i*i))
    
    
print("Outside")
print(f1.closed)