with open("Hello.txt", "r") as file: # it use for reading lines
  for line in reversed(file.readlines()):
    print(line.strip()[::-1])

file.close()