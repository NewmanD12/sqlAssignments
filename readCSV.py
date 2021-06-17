import csv
with open('dog_data.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	for row in spamreader:
	    print(f'INSERT INTO dogs ( name, owner, birth, breed) VALUES\n' +)



# INSERT INTO dogs ( name, owner, birth, breed) VALUES
  # ('Bean', 'Lennon', '2020-01-03', 'labrador'),
  # ('Cookie', 'Casey', '2020-12-13', 'siberian-husky'),
  # ('Betsy', 'Jeff', '2021-05-21', 'chiwawa'),
  # ('Angel', 'Joe', '2021-05-21', 'great-dane'),
  # ('Bootsy', 'Jeff', '2021-05-21', 'bulldog'),
  # ('Bootsy', 'John', '2021-05-21', 'bulldog')
  # ;