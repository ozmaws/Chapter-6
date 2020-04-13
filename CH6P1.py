def newton(number):
  tolerance = 0.000001
  estimate = 1.0
  while True:
    estimate = (estimate + number / estimate) / 2
    difference = abs(number - estimate ** 2)
    if difference <= tolerance:
      break
  print(estimate)
def main():
  num = input("Enter number: ")
  while num != "":
    newton(float(num))
    num = input("Enter number: ")
if __name__ == "__main__":
  main()
