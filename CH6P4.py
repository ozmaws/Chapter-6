def newton(number, estimate = 1.0):
  estimate = improveEstimate(number, estimate)
  if limitReached(number, estimate) != True:
    newton(number, estimate)
  print(estimate)
def limitReached(number, estimate, tolerance = 0.000001):
  difference = abs(number - estimate ** 2)
  if difference <= tolerance:
    return True
  else:
    return False
def improveEstimate(number, estimate):
  estimate = (estimate + number / estimate) / 2
  return estimate
def main():
  num = input("Enter number: ")
  while num != "":
    newton(float(num))
    num = input("Enter number: ")
if __name__ == "__main__":
  main()
