# WAP where need to input marks in 5 subjects out of 100 and
# print percentage

sub1 = float(input('enter marks of sub1 out of hundred  '))
sub2 = float(input('enter marks of sub2 out of hundred  '))
sub3 = float(input('enter marks of sub3 out of hundred  '))
sub4 = float(input('enter marks of sub4 out of hundred  '))
sub5 = float(input('enter marks of sub5 out of hundred  '))

totalmarks = sub1+sub2+sub3+sub4+sub5
percentage = (totalmarks /500)*100

print('percentage is :{}'.format(percentage))