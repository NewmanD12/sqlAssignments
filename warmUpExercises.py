from pprint import pprint

str1 = "P@#yn26at^&i5ve"

def countCharsAndSymbols(str):
  digitCount = 0
  charCount = 0
  symbolCount = 0
  for x in range(len(str)):
    if(str[x].isnumeric()):
      digitCount += 1
    elif(str[x].isalpha()):
      charCount += 1
    else:
      symbolCount += 1
  print(digitCount)
  print(charCount)
  print(symbolCount)

# countCharsAndSymbols(str1)


text="""
Computer programming is the process of designing and building an executable computer program to accomplish a specific computing result or to perform a specific task. Programming involves tasks such as: analysis, generating algorithms, profiling algorithms' accuracy and resource consumption, and the implementation of algorithms in a chosen programming language (commonly referred to as coding).[1][2] The source code of a program is written in one or more languages that are intelligible to programmers, rather than machine code, which is directly executed by the central processing unit. The purpose of programming is to find a sequence of instructions that will automate the performance of a task (which can be as complex as an operating system) on a computer, often for solving a given problem. Proficient programming thus often requires expertise in several different subjects, including knowledge of the application domain, specialized algorithms, and formal logic.
Tasks accompanying and related to programming include: testing, debugging, source code maintenance, implementation of build systems, and management of derived artifacts, such as the machine code of computer programs. These might be considered part of the programming process, but often the term software development is used for this larger process with the term programming, implementation, or coding reserved for the actual writing of code. Software engineering combines engineering techniques with software development practices. Reverse engineering is a related process used by designers, analysts and programmers to understand and re-create/re-implement
"""

def findMostCommonLetter(str):
  str = str.lower()
  
  dictOfLetters = {}
  for x in range(len(str)):
    if(str[x] not in dictOfLetters and str[x].isalpha()):
      dictOfLetters[str[x]] = 1
    elif(str[x] in dictOfLetters and str[x].isalpha()):
      dictOfLetters[str[x]] += 1

  countOfMostUsedLetter = 0
  mostUsedLetter = ''
  for key, value in dictOfLetters.items():
    if(value > countOfMostUsedLetter):
      countOfMostUsedLetter = value
      mostUsedLetter = key
  
  print(mostUsedLetter)
  # print(countOfMostUsedLetter)
  return mostUsedLetter

# findMostCommonLetter(text)


ignoredWords = []

with open('function_words.txt', 'r') as fin:
  for line in fin.readlines(): 
    line = line.strip()   
    ignoredWords.append(line)

# print(ignoredWords)

dictOfWords = {}
textWords = text.lower().split()

for word in textWords:
  # print(word)
  if(word not in ignoredWords and word not in dictOfWords):
    dictOfWords[word] = 1
  elif(word not in ignoredWords and word in dictOfWords):
    dictOfWords[word] += 1

# print(dictOfWords)

##########################################################################################################################################################################################################################################
text2 = 'THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'


def ceasersCipher(str):
  alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  crypticString = ''

  str = str.lower()
  for x in range(len(str)):
    # print(str[x])
    if(str[x] in alphabetList):
      for j in range(len(alphabetList)):
        if(alphabetList[j] == str[x]):
          crypticString += alphabetList[j - 3]
    elif(str[x] == " "):
      crypticString += str[x]



  print(crypticString)

# ceasersCipher(text2)


def ceasersCipher2(num, shift, str):

  alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  crypticString = ''

  shift = shift.lower()
  shift = shift[:1]
    

  str = str.lower()
  for x in range(len(str)):
    if(str[x] in alphabetList):
      for j in range(len(alphabetList)):
        if(alphabetList[j] == str[x] and shift == 'l'):
          crypticString += alphabetList[j - num]
        elif(alphabetList[j] == str[x] and shift == 'r' and j + x > len(alphabetList)):
          remainder = j + x - len(alphabetList)
          print(remainder)

          # crypticString += alphabetList[j + num]
        elif(alphabetList[j] == str[x] and shift == 'r' and j + x <= len(alphabetList)):
          crypticString += alphabetList[j + num]
    elif(str[x] == ' '):
      crypticString += str[x]

  # print(crypticString)
      
      

ceasersCipher2(4, 'right', text2)