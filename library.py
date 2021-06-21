import sqlite3

conn = sqlite3.connect("library.db")
c = conn.cursor()

c.execute("""DROP TABLE books""")

c.executescript('''
  create table books(
    id,
    title,
    author  
  );

  insert into books(id, title, author)
  values (
    '001',
    'Outliers',
    'Malcolm Gladwell'
  ),
  (
    '002',
    'Humble Pie',
    'Matt Parker'
  ),
  (
    '003',
    '52 Small Changes',
    'Brett Blumenthal'
  ),
  (
    '004',
    'Blink',
    'Malcolm Gladwell'
  ),
  (
    '005',
    'The Tipping Point',
    'Malcolm Gladwell'
  ),
  (
    '006',
    'All the Powers of Earth',
    'Sidney Blumenthal'
  )
''')

conn.commit()
# conn.close()

# c.execute('SELECT * FROM books')
# books = c.fetchall()
# for book in books:
#   print(book)
#   print('=' * 60)

c.execute('ALTER TABLE books ADD COLUMN price TEXT')
conn.commit()

# c.execute('SELECT * FROM books')
# books = c.fetchall()
# for book in books:
#   print(book)
#   print('=' * 60)

c.execute(""" UPDATE books SET
  price = '9.99'
  WHERE author LIKE '%Blumenthal'
""")
conn.commit()

c.execute(""" UPDATE books SET
  price = '12.99'
  WHERE author = 'Malcolm Gladwell'
""")
conn.commit()

c.execute(""" UPDATE books SET
  price = '7.99'
  WHERE author = 'Matt Parker'
""")
conn.commit()

c.execute('SELECT MIN(CAST(price as REAL)) FROM books')
booksMin = c.fetchall()
for bookMin in booksMin:
  print(bookMin)
  print('=' * 50)

conn.close()