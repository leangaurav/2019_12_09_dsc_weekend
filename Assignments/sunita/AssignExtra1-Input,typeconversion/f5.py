##write simple interest calculator

# formula : PRT/100
# where , 
# p = principle amount 
# R = rate ofinterest
# T = time period

P = int(input('enter the priciple amount in rupees '))
R = int(input('enter the rate of interest in percentage '))
T = int(input('enter Time period in years '))

SI = (P*R*T) /100

print('simple Interest is:{}'.format(SI))