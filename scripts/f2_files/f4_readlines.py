# this is a script
f = open(r"E:\LINKS\Desktop\workspace\2019_12_09_dsc_weekend\scripts\f2_files\test.csv", 'r')

print(f.tell())
print(f.readlines())
print(f.tell())
f.seek(4)
print(f.tell())

for l in f:
    print(l, end = '')