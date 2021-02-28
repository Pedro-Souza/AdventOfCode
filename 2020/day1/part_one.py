numbers = open('numbers.txt', 'r').readlines()

def check(number1, number2):
  return int(number1) + int(number2) == 2020

for number1 in numbers:
  for number2 in numbers:
    if (check(number1, number2)):
      print(number1)
      print(number2)

