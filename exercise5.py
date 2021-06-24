import math
import random
import csv, sqlite3
import os

numList1 = [88,89,90,93,84,86,88,91,88,87]

def calcMean(numList):
  sum = 0
  count = 0
  mean = 0
  for i in range(len(numList)):
    sum += numList[i]
    count += 1
  # print(sum)
  # print(count)
  mean = sum / count
  print('the mean is', mean)
  return mean
  
# calcMean(numList1)

def calcMode(list = [2,2,3,3,4]):
  listOfModes = []
  highCount = list.count(list[0])
  mode = 0
  for i in range(len(list)):
    if(highCount < list.count(list[i])):
      mode = list[i]
    elif(highCount == list.count(list[i]) and list[i] not in listOfModes):
      listOfModes.append(list[i])
  if(len(listOfModes) > 1):
    print('the modes are: ', listOfModes)
    return listOfModes
  else:
    print('The mode is: ', mode)
    return mode
    
# calcMode(numList1)
# calcMode()

def calcMedian(list):
  list.sort()
  if(len(list) % 2 == 1):
    half = int(len(list) / 2 + .5)
    middleNum = list[half]
    # print(middleNum)
    return middleNum
  else:
    half = int(len(list) / 2)
    combinedNum = list[half] + list[half - 1]
    median = combinedNum / 2
    # print(median)
    return median
    

# calcMedian(numList1)


def printPrime1000Through1100():
  listOfPrimeNumbers = []
  for i in range(1000, 1101):
    # print(i)
    if(i > 1):
      for j in range(2, i):
        if(i % j == 0):
          break
      else:
        listOfPrimeNumbers.append(i)
  # print(listOfPrimeNumbers)
  return listOfPrimeNumbers



# printPrime1000Through1100()

def isItPrime(num):
    for i in range(2, num):
      if(num % i == 0):
        # print('this num is not prime', num)
        return False
    else:
      # print('this num is prime', num)
      return True

# isItPrime(7)


def isSumPrime(list):
  for i in range(len(list)):
    string = str(list[i])
    sumOfNums = 0
    for j in range(len(string)):
      # print(string[j])
      sumOfNums += int(string[j])
    print(string, sumOfNums, isItPrime(sumOfNums))
    


# isSumPrime(printPrime1000Through1100())


students = ['Renee','Julia','Warren','Stacey','Charles','Linda','Dwight','Ann','Franklin','George','Walter','Susan']


def pickRandomStudents(list):
  voluntoldList = []
  luckyStudentsList = []
  while(len(voluntoldList) < 5):
    randomNum = random.randrange(len(list))
    if(list[randomNum] not in voluntoldList):
      voluntoldList.append(list[randomNum])
    # print('I randomly picked these students: ', voluntoldList)
  for i in range(len(list)):
    if(list[i] in list and list[i] not in voluntoldList):
      luckyStudentsList.append(list[i])

  print('I randomly picked these students: ', voluntoldList) 
  print('Remaining Students: ', luckyStudentsList)

# pickRandomStudents(students)

os.chdir(r'/Users/dakota/Desktop/codeImmersives/mySQL')

conn = sqlite3.connect('world_country_populations.db')
c = conn.cursor()

c.execute("""DROP TABLE countries""")

c.execute(
  """ CREATE TABLE countries (
    num INT, 
    country TEXT,
    population INT,
    year_change REAL,
    net_change INT,
    density INT,
    land_area_km2 INT,
    migrants INT,
    fertility_rate REAL,
    median_age INT,
    urban_pop_pct REAL,
    world_share REAL
  )  
  """
)

with open('World_country_populations.csv', 'r') as fin:
  dr = csv.DictReader(fin)
  valuesPassed = []
  for entry in dr:
    allCountries = []
    num = entry.get('num')
    country = entry.get('Country')
    population = entry.get('population')
    yearChange = entry.get('year_change')
    netChange = entry.get('net_change')
    density = entry.get('density')
    landAreaKm2 = entry.get('land_area_km2')
    migrants = entry.get('migrants')
    fertilityRate = entry.get('fertility_rate')
    medianAge =  entry.get('Median_age')
    urbanPopPct = entry.get('Urban_pop_pct')
    worldShare = entry.get('World_share')

    allCountries.append(num)
    allCountries.append(country)
    allCountries.append(population)
    allCountries.append(yearChange)
    allCountries.append(netChange)
    allCountries.append(density)
    allCountries.append(landAreaKm2)
    allCountries.append(migrants)
    allCountries.append(fertilityRate)
    allCountries.append(medianAge)
    allCountries.append(urbanPopPct)
    allCountries.append(worldShare)
    
    valuesPassed.append(tuple(allCountries))

c.executemany('''
INSERT INTO countries VALUES (?,?,?,?,?,?,?,?,?,?,?,?)  
''', valuesPassed)
conn.commit()


# 1 - Print the top 20 countries by population - Output in millions.
c.execute(''' SELECT country, population FROM countries ORDER BY population DESC''')
conn.commit()

countries = c.fetchmany(20)
# for country in countries:
  # print(country[0], '- population in mm', (country[1] / 1000000))


# 2 - What is the total world population
c.execute(''' SELECT population FROM countries ''')
conn.commit()

countries = c.fetchall()
totalPopulation = 0
for country in countries:
  totalPopulation += country[0]
# print(totalPopulation)

# 3 - Top 10 countries by median age
c.execute(''' SELECT country, median_age FROM countries
  WHERE median_age IS NOT 'N.A.'
  ORDER BY median_age DESC
 ''')
conn.commit()

countries = c.fetchmany(10)
# for country in countries:
#   # print(country)
#   print(country[0],'- median age is', country[1] )

# 4 - Top 10 countries where people left
c.execute(''' SELECT country, net_change FROM countries 
  ORDER BY net_change
 ''')
conn.commit()
countries = c.fetchmany(10)
# for country in countries:
#   print(country[0], '- people who left ', country[1])

# 5 - Top 10 countries who took in migrants
c.execute(''' SELECT country, migrants FROM countries
  WHERE migrants != ''
  ORDER BY migrants DESC
   ''')
conn.commit()
# countries = c.fetchmany(10)
# for country in countries:
#   print(country[0], '- migrants', country[1])

# 6 - Which countries with a population less than 10 million had the largest year_change pct

limit = 10000000

c.execute("SELECT country, population, year_change FROM countries WHERE CAST(population as int) < {0} ORDER BY year_change DESC".format(limit))
conn.commit()


countries = c.fetchmany(10)
# for country in countries:
#   print(country[0], '- year change', country[2], '- population', country[1])


# 1)total number of migrants from G7 nations, 2) total ratio of G7 against total intake of migrants (What percentage?)

# countriesTuple = ('Canada', 'France','Germany','Italy','Japan','United Kingdom', 'United States')
# c.execute("""SELECT migrants, country FROM countries WHERE country IN {0} AND migrants > 0""".format(str(countriesTuple)))
# conn.commit()

c.execute(""" SELECT migrants, country from countries WHERE country in ('Canada', 'France', 'Germany', 'Italy', 'Japan', 'United Kingdom', 'United States') """)
conn.commit()

g7Migrants = c.fetchone()
print(g7Migrants)





# Find the position of the 2 character string '20' in the following:
stringOfNumbers = '32040230213340205020112'

def find20s(str):
  listOfPositions = []
  countOf20s = 0
  for i in range(len(str)):
    if(i != 0 and int(str[i]) == 0 and int(str[i - 1]) == 2):
      countOf20s += 1
      listOfPositions.append(i-1)
    else:
      continue
  print('There are', countOf20s, "- 20's in the following positions", listOfPositions)

# find20s(stringOfNumbers)