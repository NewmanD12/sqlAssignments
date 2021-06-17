# 1) In the database called pets, create a new table called dogs.
# CREATE DATABASE pets

# 2) add fields, id,name owner , birth ,type
# CREATE TABLE dogs
# (
#   id              INT unsigned NOT NULL AUTO_INCREMENT,
#   name            VARCHAR(150) NOT NULL,
#   owner           VARCHAR(150) NOT NULL,
#   birth           DATE NOT NULL,
#   breed           VARCHAR(150) NOT NULL,
#   PRIMARY KEY     (id)
# );


# 3) insert data from dog_data
# INSERT INTO dogs ( name, owner, birth, breed) VALUES
  # ('Bean', 'Lennon', '2020-01-03', 'labrador'),
  # ('Cookie', 'Casey', '2020-12-13', 'siberian-husky'),
  # ('Betsy', 'Jeff', '2021-05-21', 'chiwawa'),
  # ('Angel', 'Joe', '2021-05-21', 'great-dane'),
  # ('Bootsy', 'Jeff', '2021-05-21', 'bulldog'),
  # ('Bootsy', 'John', '2021-05-21', 'bulldog')
  # ;


# 4) retrieve all the entries of dog 
# Select * from dogs

# 5) retrieve all the names of jeffs' dogs
# Select name from dogs Where owner = 'Jeff'

# 6) remove all entries from table where the dog's name is Bootsy
# Delete from dogs where name = 'bootsy'