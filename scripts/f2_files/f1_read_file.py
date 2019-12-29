f = open("test.csv", "r")

r = f.readline()

r = f.readline()
nums = r.split(',')
print(nums)
nums = list(map(int, nums))
print(nums)