text = open('input.txt', 'r').readlines()

count = 0
posicao = 0
line_count = 0

for line in text:
  line = line.replace('\n', '')
  line_count += 1
  posicao += 3

  if posicao > 30:
    posicao = posicao - 31

  letter = text[line_count][posicao]

  if letter == "#":
    count += 1

    if (line_count != 2):
      print("line" + line)
      print("line_count" + str(line_count))
      print("position" + str(posicao))
      print("line_correcty" + text[line_count])
      print("letter" + text[line_count][posicao])

print(count)
