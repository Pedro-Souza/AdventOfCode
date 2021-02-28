numbers = open('numbers.txt', 'r').readlines()

def check(number1, number2, number3):
  return int(number1) + int(number2) + int(number3) == 2020

for number1 in numbers:
  for number2 in numbers:
    for number3 in numbers:
      if (check(number1, number2, number3)):
        print(number1)
        print(number2)
        print(number3)

