text = open('input.txt', 'r').readlines()
count = 0

def check(rangeQty, letter, text):
  global count
  rangee = rangeQty.split('-')
  quantity = text.replace('\n', '').count(letter.replace(':', ''))
  minimun = rangee[0]
  maximun = rangee[1]

  print(minimun, maximun, quantity)
  if (int(quantity) >= int(minimun) and int(quantity) <= int(maximun)):
    count += 1

for line in text:
  array = line.split(' ')
  check(array[0], array[1], array[2])


print(count)
