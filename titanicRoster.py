import csv, sqlite3
import os
from pprint import pprint

os.chdir(r'/Users/dakota/Desktop/codeImmersives/mySQL')
# print(os.getcwd())

conn = sqlite3.connect('titanic_roster.db')
c = conn.cursor()

c.execute("""DROP TABLE passengers""")

c.execute(
  """CREATE TABLE passengers (
  passengerid TEXT,
  name TEXT,
  age TEXT
  )
"""
)


with open('titanic.csv', 'r') as fin:
  dr = csv.DictReader(fin)
  neededValues = []
  totalAge = 0
  averageAge = 0
  count = 0
  for entry in dr:
    allPassengers = []
    passengerAge = entry.get('Age')
    passengerID = entry.get('PassengerId')
    passengerName = entry.get('Name')
    allPassengers.append(passengerID)
    allPassengers.append(passengerName)
    allPassengers.append(passengerAge)
    # print(float(passengerAge))
    neededValues.append(tuple(allPassengers))
    print(dr.fieldnames)

  # print(neededValues)


c.executemany("""INSERT INTO passengers VALUES (?,?,?)""", neededValues)
conn.commit()

c.execute(""" UPDATE passengers SET
age = '50'
WHERE name = 'Moran, Mr. James' 
""")
conn.commit()

c.execute(""" DELETE FROM passengers WHERE name = 'Sjostedt, Mr. Ernst Adolf' 
""")
conn.commit()

# print(averageAge)


# print(c.rowcount)

conn.close