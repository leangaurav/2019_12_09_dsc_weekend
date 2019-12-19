# Guess output of each slice:
s=‘Python is Object Oriented’
	1. s[-1] = d #last charactr 
	2. s[::-1] = 'detneirO tcejbO si nohtyP' #string reversal
	3. s[:-1] = 'Python is Object Oriente' # start to end -1
	4. s[1:1] = ''# length of slice is zero, so no output 
	5. s[4:10] = 'on is '

2. What error do you see for following statements: 
s= ‘’
print(s[1])
	string out of range, since length of string itslef is 0

3. Do you get any error for the following code, if not give the output: S=‘Gaurav’
print(s[1])
	'a' #second char of string 0,1

4. Find output of the following:
a) s=‘a b cd’ print(len(s))
	6
print(s[::2]) print(len(s[::2]))
	abc #step size 2, so omits inbetween blank
b) s=‘a#b#c#d#’ print(s.split())
	[‘a#b#c#d#’] #delimeter is space and there is no space inbetween to split

print(s.split(‘#’)) l=s.split(‘#’) s=‘$’.join(l) print(s)
	‘a$b$c$d$’
c) S=‘Gaurav’ S=S[::-2][::-2]
print(S)
	'av'
d) print(1>2)
	False
e) print(4%2, 5%2, 2%5, sep=‘, ’)
	0,1,2
f) s=‘abcba’ s.upper()
	ABCBA
print(s)
print(s.count(‘A’), end = ‘ ,’) print(s.count(‘A’, 2,4) , end = ‘ ,’) print(s.count(‘a’, 2,4) , end = ‘ ,’)
	0,0,
5. WAP to input a string and remove all spaces from it.
	i = input('enter a string with spaces')
	ans = i.replace(' ','')
	print(ans)
6. What does this symbol denote:
[]
	list
7. WAP to print all methods(functions/operations) available in a string (Hint : dir())
	print(dir(str))
8. Write statement to check if rstrip method is available in the str class. (Hint : Use the find function or in)
	l = dir(str)
	if 'rstrip' in l:
		print('rstrip is present in str')
	else:
		print('rstrip is not present in str')
Gaurav Gupta
tuteur.py@gmail.com
9. WAP to store the following patterns in a string variable and then print them:
	s1 = 'Gaurav Gupta'
	s2 = 'tuteur.py@gmail.com'
	print(s1, s2)
10. WAP to input a string and replace all space with new lines (\n) and print again.
	i = input('enter a string with spaces')
	ans = i.replace(' ','\n')
	print(ans)
11. WAP to input complete name(first and last name separated by space) and print first and last
name separately along with their length in upper case.
	name = input('enter your complete name')
	names = name.split(',')
	print(names[0].upper() , len(names[0]) )
	print(names[1].upper() , len(names[1]) )
12. WAP to input a string and split it into 2 halves. The string can be of any length
Ex-1: Input = “String”
S1 = Str S2 = ing
Ex-2: Input = “words”
S1 = wo S2 = ds
	word = input('enter a word')
	l = len(word)
	first = word[:int(l/2)]
	second = word[int(l/2):]
	print(first)
	print(second)