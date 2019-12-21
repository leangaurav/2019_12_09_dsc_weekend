def get_si(p,r,t):
	si=(p*r*t)/100
	return si
p=float(input("Enter the principal amount"))
r=float(input("Enter the rate of interest"))
t=float(input("enter the time in years"))

get_si(p,r,t)
print(get_si(p,r,t))

#output:
Enter the principal amount 500
Enter the rate of interest2.5
enter the time in years2
25.0