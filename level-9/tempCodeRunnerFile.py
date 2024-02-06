with open('D:\Programing Code\python\MISSION_PY\level-9\data\sample2.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)
with open('D:\Programing Code\python\MISSION_PY\level-9\data\sample2.txt', 'r') as f:
  print(f.read())