# find min & max value without using any predefine functions

l = [3,54,92,84,69,72,5,19]
max = l[0]
min = l[0]

for i in l:
    if i>max:
        max=i
    if i<min:
        min =i
print(f"the maximum number is: {max} and the minimum number is: {min}")
