# this is a script
f = open(r"E:\LINKS\Desktop\workspace\2019_12_09_dsc_weekend\scripts\f2_files\test.csv", 'r')

s = f.readline()

while len(s) > 0:
    print(s, end = '')
    s = f.readline()