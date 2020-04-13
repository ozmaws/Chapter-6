import os, os.path
def openAll(path):
  if os.path.isfile(path):
    aFile = open(path)
    for line in aFile:
      print(line)
    print()
    return 0
  lyst = os.listdir(path)
  for element in lyst:
    if os.path.isfile(element):
      aFile = open(path + os.sep + element)
      for line in aFile:
        print(line)
      print()
    else:
      os.chdir(path + os.sep + element)
      openAll(os.getcwd())
      os.chdir("..")
    print("----------------")
def main():
  openAll(os.getcwd())
if __name__ == "__main__":
  main()
