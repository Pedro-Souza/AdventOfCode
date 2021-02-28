text = open('input.txt', 'r').readlines()
count = 0

def check(rangeQty, letter, text):
  global count
  letra = letter.replace(':', '')
  texto = text.replace('\n', '')
  rangee = rangeQty.split('-')
  minimun = int(rangee[0]) - 1
  maximun = int(rangee[1]) - 1

  if ((texto[minimun] == letra and texto[maximun] != letra) or (texto[minimun] != letra and texto[maximun] == letra)):
    count += 1

for line in text:
  array = line.split(' ')
  check(array[0], array[1], array[2])

print(count)
