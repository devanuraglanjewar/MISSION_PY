# Methods
    # readline(): Reads a single line from the file.
    # readlines(): Reads all lines as a list of strings.
    # iter(file): Iterates over lines in the file.
    # writelines(lines): Writes a list of strings to the file.
    # tell(): Gets the current file position.
    # seek(position): Moves the file pointer to a specific position.
    # truncate(size): Truncates the file to a given size.

# Example 1
f =  open('D:\Programing Code\python\MISSION_PY\level-9\data\Twinkle.txt','r')
while True:
    lines = f.readlines()
    if not lines:
        break
    print(lines)
f.close()

# Example 2
f = open('D:\Programing Code\python\MISSION_PY\level-9\data\Marks.txt', 'r')
i = 0
while True:
  i = i + 1
  line = f.readline()
  if not line:
    break
  m1 = int(line.split(",")[0])
  m2 = int(line.split(",")[1])
  m3 = int(line.split(",")[2])
  print(f"Marks of student {i} in Maths is: {m1*2}\n")
  print(f"Marks of student {i} in English is: {m2*2}\n")
  print(f"Marks of student {i} in SST is: {m3*2}\n")


#Example 3
# program to create list
f = open('D:\Programing Code\python\MISSION_PY\level-9\data\mylist.txt', 'w')
lines = ['Item 1\n', 'Item 2\n', 'Item 3\n']
f.writelines(lines)
f.close()

# Example 4 
with open('D:\Programing Code\python\MISSION_PY\level-9\data\sample.txt', 'r') as f:
  # Move to the 10 byte in the file
    f.seek(5)
    # read next 2 byte
    data = f.read(2)
    print(data)

# Example 4
with open('D:\Programing Code\python\MISSION_PY\level-9\data\sample.txt', 'r') as f:
    f.seek(5)         # Move to the 10 byte in the file
    print("Current File Position :",f.tell())   # to get current file position
    data = f.read(2)  # read next 2 byte
    print(data) 

# Example 5 
with open('D:\Programing Code\python\MISSION_PY\level-9\data\sample2.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5) # to  remove remaining part of the file after writing Hello World!
with open('D:\Programing Code\python\MISSION_PY\level-9\data\sample2.txt', 'r') as f:
  print(f.read())