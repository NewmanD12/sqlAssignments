def ascci(str):
  sum = 0
  for i in range(len(str)):
    sum += ord(str[i])
  print(sum)

# ascci('hello')


##################################################################################################################################################################################################################



"""
ASCII (American Standard Code for Information Interchange), is a character encoding standard for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices.
There is a function for finding the ascii value of a character here: https://docs.python.org/3/library/functions.html
Write a function that asks the user for input, and then computes the sum of all the ascii values of the characters.
"hello" -> 104 + 101 + 108 + 108 + 111 = 532
Part 2: Given a list of words (from user input) determine which word has the highest ascii value.
"""

def findHighestAscii(list):
  biggest = ''
  for i in range(len(list)):
    sum = 0
    for j in range(len(list[i])):
      sum += ord(list[i][j])
  print(sum)

# findHighestAscii('hello')


##################################################################################################################################################################################################################

# Analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.
# Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise.
# Sample Inputs:
# hello -> True
# nono -> False
# sunday -> False
# racecar -> False

def double_letters(str):
  for i in range(1, len(str)):
    # print(str[i - 1])
    # print(str[i])
    if(str[i - 1] == str[i]):
      print('true')
      return True
  print('false')
  return False
      

# double_letters('hello')
# double_letters('nono')
# double_letters('sunday')
# double_letters('racecar')

##################################################################################################################################################################################################################



"""
write a program that prints the following
```
*
* *
* * *
* * * *
* * * * *
* * * * * 
* * * *
* * *
* *
*
``
1) do it using a for loop 
2) do it using a list comp. 
part 2:
replace the middle of any odd numbered row with a smilie emoji 😊 in the middle
"""

def makePyramid(num):
  count = 0
  for i in range(1, num + 1):
    if(i % 2 == 0):
      result = '* ' * i
      print(result)
      count += 1
    else:
      half = int((i - 1) / 2)
      result = ('* ' * half + '😊 ' + '* ' * half)
      print(result)
      count += 1

  while count:
    if(count % 2 == 0):
      result = '* ' * count
      print(result)
      count -= 1
    else:
      half = int((count - 1) / 2)
      result = ('* ' * half + '😊 ' + '* ' * half)
      print(result)
      count -= 1


# makePyramid(11)

##################################################################################################################################################################################################################

def createDeckOfCards():
  cardTypes = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
  royals = ['Jack', 'Queen', 'King', 'Ace']
  deckOfCards = []
  for i in range(2,11):
    # print(i)
    for j in range(len(cardTypes)):
      card = str(i) + '-' + cardTypes[j]
      deckOfCards.append(card)
  
  for r in range(len(royals)):
    for j in range(len(cardTypes)):
      card = royals[r] + '-' + cardTypes[j]
      # print(card)
      deckOfCards.append(card)
      # print(royals[r], cardTypes[j])

  # print(len(deckOfCards))
  # print(deckOfCards)
  return deckOfCards

createDeckOfCards()

##################################################################################################################################################################################################################
purchases = {'2021-01-01': 
  {'item-001': 
      {'name': 'Alka Seltzer'},
  'item-002': 
      {'name': 'Rolaids'},
  'item-003': 
      {'name': 'Orange juice'}  }                
}

purchases['2021-01-01']['item-004'] = {'name' : 'Bloody Mary'}
purchases['2021-01-01']['item-005'] = {'name' : 'Pineapple Juice'}

print(purchases)
print([ v['name'] for k,v in purchases['2021-01-01'].items() if v['name'].lower().endswith('juice')])


##################################################################################################################################################################################################################
import itertools
numbers = [2,7,9,12,15,3,11,22,17,6,0,-8]

def findCombosThatAddUpTo9(list):
  listOfCombos = []
  for i in range(len(list)):  
    for j in range(i, len(list)):
      # print(list[i] + list[j])
      if(list[i] + list[j] == 9):
        combos = (list[i], list[j])
        if(combos not in listOfCombos):
          listOfCombos.append(combos)
        # print(combos)
  print(listOfCombos)
  return listOfCombos

# findCombosThatAddUpTo9(numbers)
