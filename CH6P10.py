def myRange(end, start = 0, step = 1):
  rangeList = []
  currentValue = start
  while currentValue < end:
    rangeList.append(currentValue)
    currentValue += step
  return rangeList
def main():
  firstRange = myRange(8)
  print(firstRange)
  secondRange = myRange(10,5)
  print(secondRange)
  thirdRange = myRange(100,10,10)
  print(thirdRange)
if __name__ == "__main__":
  main()
