
# check the string is palindrom or not
s=str(input("enter the  string: "))

if s == s[::-1]:
    print("it is palindrom")
else:
    print("it is not palindrom")











#alternate
s=str(input("enter the  string: "))
n = len(s)
x = 0
for i in range (n):
    if  s[i] != s[n-i-1]:
        x = 1
        break
if x == 0:
    print("it is palindrom")
else:
    print("it is not palindrom")