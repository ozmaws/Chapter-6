def newton(number, estimate):
  tolerance = 0.000001
  estimate = (estimate + number / estimate) / 2
  difference = abs(number - estimate ** 2)
  if difference > tolerance:
    newton(number, estimate)
  print(estimate)
def main():
  estimate = 1.0
  num = input("Enter number: ")
  while num != "":
    newton(float(num), estimate)
    num = input("Enter number: ")
if __name__ == "__main__":
  main()
