with open('test.csv', 'r') as f1:# context handlers
    with open('test_copy.csv', 'w') as f2:
        f2.write(f1.read())
        
    
print("Outside")
print(f1.closed)