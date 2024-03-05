#Sort list without using sort keyword.
list1 =[12,56,78,98,2,48]
l = len(list1)

for i in range(l):
    for j in range (i+1,l):
        if list1[i]>list1[j]:
            list1[i],list1[j]=list1[j],list1[i]

print(list1)
