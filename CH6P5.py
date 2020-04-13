def isSorted(aList):
  if aList == []:
    return True
  else:
    count = 1
    for word in aList:
      if count != len(aList):
        if word > aList[count]:
          return False
        count += 1
    return True
def main():
  wordList = ["egg", "cheese", "milk"]
  if isSorted(wordList):
    print("List is sorted.")
  else:
    print("List is not sorted.")
if __name__ == "__main__":
  main()
