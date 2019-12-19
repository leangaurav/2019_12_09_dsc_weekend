##input principle, rate,time and print compound interest and amount

##formula:

# cI = p*(1+(r/100))**n)-p

# Amount = p+CI
#where,

# CI is compound interest
# p is principle amount
# r is rate of interest 
# n is compounding time period 

p = float(input('enter the principal amount '))
r = float(input('enter the rate of interest inpercentage '))
n = float(input('enter the compounding time perion in years '))

CI = (p*(1+(r/100))**n)- p

print('compound intest for the given principle is: {}'.format(CI))

Amount = p+CI

print('total amount payable :{}'.format(Amount))