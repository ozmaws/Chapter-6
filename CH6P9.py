from functools import reduce
aFile = open("numbers.txt")
numbers = []
for line in aFile:
  numbers.append(line)
numbers = list(map(int, numbers))
count = len(numbers)
total = reduce(lambda x, y: x + y, numbers)
average = total / count
print(average)
