string = input("Enter string: ")
only_letters = []
sum = 0
numbers = 0
letters = 0

for symbol in string:
  if symbol.isdigit():
    sum += int(symbol)
    numbers +=1
  elif symbol.isalpha():
    only_letters += symbol
    letters += 1
if len(string) > 30 and len(string) < 50:
  print("Length: ", len(string))
  print("Numbers: ", numbers)
  print("Letters: ", letters)
elif len(string) < 30:
  print("Sum: ", sum)
  print("Without numbers: ", only_letters)
elif len(string) > 50:
  print("Ne pridumav)))")