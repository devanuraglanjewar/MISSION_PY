# find output
# input : "the sky is blue"
# output: "blue is sky the"

s = "the sky is blue"
l = s.split()
l = l[::-1]
l = ' '.join(l)
print(l)