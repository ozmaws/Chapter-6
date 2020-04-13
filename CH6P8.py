###This function works like it's supposed to. It works by printing the first index of the sequence,###
###then removing this value from the sequence so that way the next time the function is called,###
###the first index of the sequence that is printed is actually the second index of the original sequence.###
###This process repeats until all values have been removed from the sequence.###

def printAll(seq):
  if seq:
    print("First index: " + str(seq[0]))
    print("Removing...")
    printAll(seq[1:])
def main():
  aList = [1,2,3,4,5]
  printAll(aList)\
if __name__ == "__main__":
  main()
