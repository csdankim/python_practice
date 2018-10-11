import sys

numbers = sys.argv[1:] # only takes numbers. not include file name as the first arg

sum = 0
for i in numbers:
    sum += int(i)

print(sum)

