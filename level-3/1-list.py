# what is list
# --a collection of items that can be accessed by an index number, it also allow different typr of data in a single list.

marks=[55,48,85,96,19,72] # it is list of marks
print(marks)
print("type =>",type(marks))
print(marks[0])
print(marks[2])
print(marks[-3])
print("Length os list =>",len(marks))
print(marks[:4:3]) # it will jump by 3


names = ['Anurag', 'Jay', 'Raj', 'Pratik', 'Om' ]
if 'rag' in 'Anurag':
    print("yes")
else:
    print("no")


# List Comprehension
# --It is use for creating new lists from other iterables like,
#   tuples,dictionaries,sets and even in array and strings.    
# example
lst = [i+i for i in range(11)]
print(lst)

lst_2 = [i*i for i in range(5) if i%2==0]
print(lst_2)


# Methods in list
l =[1,8,2,9,6]
print(l)

l.append(10) # append add element at the end of list
print("after append=> ",l)

l.sort() # use for sorting list
print("after sorting => ",l)

l.sort(reverse=True) # use for reverse sorting list
print("after reverse sorting => ",l)

l.reverse() # it used to reversed original list
print("after reverse without sort => ",l)

print(l.index(2)) # it used to get index of specifide element

print(l.count(2)) # it used to count specifide element in whole list

l.insert(1,88) # this method will insert 88 at one 1 index
print("after insertion => ",l)

m = [100, 200, 300]
l.extend(m) # this method joining list of m at the end of l list
print("now the list is extend =>", l)

k = l+m # it is concatenation of tow lists without changing any list it will print 
print("after concatenation of lists =>", k)

