import mysql.connector
from pprint import pprint
from dotenv import dotenv_values

config = dotenv_values("sqlToPython.env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

mydb = mysql.connector.connect(
  host=config['HOST'],
  user=config['USER'],
  password=config['PASSWORD'],
  database=config['DATABASE']
)


mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM album")

# for x in mycursor:
#   print(x)

# mycursor.execute('''
# SELECT BillingCountry ,
# CASE
#     WHEN total > 0  and total <= 7  THEN '0 - 10'
#     WHEN total > 7  and total <= 15 THEN '10 - 15'
#     WHEN total > 15 and total <= 26 THEN '15 - 26'
#     ELSE 'NONE'
# END AS Total
# FROM invoice
# ''')

# for x in mycursor:
#   print(x)
# mydb.close()

##############################################################################################
# Left Join

# mycursor.execute('''
# SELECT a.trackid, a.name, a.composer, b.invoicelineid, b.invoiceid
# FROM track AS a
# LEFT JOIN invoiceline AS b
# ON a.trackid = b.trackid
# LIMIT 10;
# ''')
# for x in mycursor:
#     print(x)

##############################################################################################
# Right Join

# mycursor.execute('''
# SELECT a.trackid, a.name, a.composer, b.invoicelineid, b.invoiceid
# FROM track AS a
# RIGHT JOIN invoiceline AS b
# ON a.trackid = b.trackid
# LIMIT 10;
# ''')
# for x in mycursor:
#     print(x)

##############################################################################################
# 1) Provide a query showing Customers (just their full names, customer ID and country) who are not in the US.

# mycursor.execute('''  
#   SELECT lastname, firstname, customerid, country
#   FROM customer
#   WHERE country != 'USA'
# ''')

# for x in mycursor:
#   print('Name:', x[1], x[0], ', Customer ID:', x[2], 'Country:', x[3])


##############################################################################################
# 2) Provide a query only showing the Customers from Brazil.
# mycursor.execute('''  
#   SELECT *
#   FROM customer
#   WHERE country = 'Brazil'
# ''')

# for x in mycursor:
#   pprint(x)

##############################################################################################
# 3) Provide a query showing the Invoices of customers who are from Brazil. The resultant table should show the customer's full name, Invoice ID, Date of the invoice and billing country.
# mycursor.execute(''' 
#   SELECT a.lastname, a.firstname, b.invoiceid, b.invoicedate, b.billingcountry
#   FROM customer AS a
#   INNER JOIN invoice AS b
#   ON a.customerid = b.customerid
#   WHERE b.billingcountry = 'Brazil'
#   LIMIT 10
# ''')

# for x in mycursor:
#   pprint(x)


##############################################################################################
# 4) Provide a query showing only the Employees who are Sales Support Agents.
# mycursor.execute(''' SELECT lastname, firstname
#   FROM employee 
#   WHERE title = 'Sales Support Agent';
#  ''')

# for x in mycursor:
#   pprint(x)

##############################################################################################
# 5) Provide a query showing a unique list of billing countries from the Invoice table.
# mycursor.execute(''' SELECT DISTINCT billingcountry
#   FROM invoice
#  ''')

# for x in mycursor:
#   pprint(x)

##############################################################################################
# 6) Provide a query showing the invoices of customers who are from Brazil.
# mycursor.execute(''' SELECT invoiceid
#   FROM invoice
#   WHERE billingcountry = 'BRAZIL'
#  ''')
# for x in mycursor:
#   pprint(x)
##############################################################################################
# 7) Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.




##############################################################################################
# 8) Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.
# mycursor.execute(''' SELECT a.total, b.lastname, b.firstname, b.country
#   FROM invoice AS a
#   INNER JOIN customer AS b
#   ON a.customerid = b.customerid
#   ''')
# for x in mycursor:
#   pprint(x)

##############################################################################################
# 9) How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?
# total2009 = 0
# total2011 = 0
# count = 0

# mycursor.execute(''' SELECT total, invoicedate, 
#   CASE
#     WHEN invoicedate LIKE '2009%' THEN '2009'
#     WHEN invoicedate LIKE '2011%' THEN '2011'
#   END AS  Year
#   FROM invoice
#   ''')

# for x in mycursor:
#   count += 1
#   if(x[2] == '2009'):
#     total2009 += x[0]
#   if(x[2] == '2011'):
#     total2011 += x[0]
# print('Total invoice count is:', count)
# print('The total sales for 2009 was:', total2009)
# print('The total sales for 2011 was:', total2011)

##############################################################################################
# 10) Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.
# mycursor.execute(''' SELECT COUNT(invoicelineid)
# FROM  invoiceline
# WHERE invoiceid = '37'
# ''')
# for x in mycursor:
#   print(x[0])

##############################################################################################
# 11) Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY
# mycursor.execute(''' SELECT COUNT(invoicelineid), invoiceid
# FROM invoiceline
# GROUP BY invoiceid
# ''')
# for x in mycursor:
#   print('There are', x[0], 'line items on invoice ID', x[1])

##############################################################################################
# 12) Provide a query that includes the track name with each invoice line item.
# mycursor.execute(''' SELECT a.invoicelineid, b.name
#   FROM invoiceline AS a
#   INNER JOIN track AS b
#   ON a.trackid = b.trackid
#  ''')

# for x in mycursor:
#   print(x)

##############################################################################################
# *************13) Provide a query that includes the purchased track name AND artist name with each invoice line item.
# mycursor.execute(''' SELECT a.invoicelineid, b.name
#   FROM invoiceline AS 
#   INNER JOIN track as b
#   ON a.trackid = b.trackid
#  ''')

# for x in mycursor:
#   print(x)


##############################################################################################
# 14) Provide a query that shows the # of invoices per country. HINT: GROUP BY
# mycursor.execute(''' SELECT count(invoiceid), billingcountry
#   FROM invoice
#   GROUP BY billingcountry
#  ''')


# for x in mycursor:
#   print(x)

##############################################################################################
# 15) Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resultant table.

# mycursor.execute(''' SELECT a.name, b.trackid
#   FROM playlist AS a
#   INNER JOIN playlisttrack AS b
#   ON a.playlistid = b.playlistid
#  ''')

# onTheGoCount = 0
# heavyMetalCount = 0
# musicCount = 0
# tvShowsCount = 0
# musicFrom90s = 0
# musicVideosCount = 0
# brazilianMusic = 0
# classical = 0
# classical101DeepCutsCount = 0
# classical101NextStepsCount = 0
# classical101TheBasicsCount = 0
# grungeCount = 0


# for x in mycursor:
#   if(x[0] == 'Heavy Metal Classic'):
#     heavyMetalCount += 1
#   elif(x[0] == 'Music'):
#     musicCount += 1
#   elif(x[0] == 'TV Shows'):
#     tvShowsCount += 1
#   elif(x[0] == '90’s Music'):
#     musicFrom90s += 1
#   elif(x[0] == 'Music Videos'):
#     musicFrom90s += 1
#   elif(x[0] == 'Brazilian Music'):
#     brazilianMusic += 1
#   elif(x[0] == 'Classical'):
#     classical += 1
#   elif(x[0] == 'Classical 101 - Deep Cuts'):
#     classical101DeepCutsCount += 1
#   elif(x[0] == 'Classical 101 - Next Steps'):
#     classical101NextStepsCount += 1
#   elif(x[0] == 'Classical 101 - The Basics'):
#     classical101TheBasicsCount += 1
#   elif(x[0] == 'Grunge'):
#     classical += 1
#   elif(x[0] == 'On-The-Go 1'):
#     onTheGoCount += 1  




##############################################################################################
# 16) Provide a query that shows all the Tracks, but displays no IDs. The resultant table should include the Album name, Media type and Genre.

# mycursor.execute(''' SELECT a.name, b.name, c.name, d.title
#   FROM track AS a
#   RIGHT JOIN genre AS b
#   ON a.genreid = b.genreid
#   RIGHT JOIN mediatype AS c
#   ON a.mediatypeid = c.mediatypeid
#   RIGHT JOIN album AS d
#   ON a.albumid = d.albumid   
# ''')

# for x in mycursor:
#   print(x)

##############################################################################################
# 17) Provide a query that shows all Invoices but includes the # of invoice line items.

# mycursor.execute(''' SELECT a.*, b.invoicelineid
#   FROM invoice AS a
#   INNER JOIN invoiceline AS b
#   ON a.invoiceid = b.invoiceid
#   LIMIT 10
# ''')

# for x in mycursor:
#   print(x)

##############################################################################################
# 18) Provide a query that shows total sales made by each sales agent.
# How? nothing connects the sales agents to the invoices?

##############################################################################################
# 19) Which sales agent made the most in sales in 2009?
# How? nothing connects the sales agents to the invoices?

##############################################################################################
# 20) Which sales agent made the most in sales in 2010?
# How? nothing connects the sales agents to the invoices?

##############################################################################################
# 21) Which sales agent made the most in sales over all?
# How? nothing connects the sales agents to the invoices?

##############################################################################################
# 22) Provide a query that shows the # of customers assigned to each sales agent.

##############################################################################################
# 23) Provide a query that shows the total sales per country. Which country's customers spent the most?
# mycursor.execute(''' SELECT count(invoiceid), billingcountry, sum(total)
#   FROM invoice
#   GROUP BY billingcountry
#  ''')

# biggestSpender = ''
# listOfTotalSpent = []
# biggestSpent = 0  

# for x in mycursor:
#   listOfTotalSpent.append(float(x[2]))
#   listOfTotalSpent.append(x[1])

# for x in range(0,len(listOfTotalSpent),2):
#   if(listOfTotalSpent[x] > biggestSpent):
#     biggestSpent = listOfTotalSpent[x]
#     biggestSpender = listOfTotalSpent[x + 1]

# print(listOfTotalSpent)
# print(biggestSpent)
# print(biggestSpender)

##############################################################################################
# 24) Provide a query that shows the most purchased track of 2013.

##############################################################################################
# 25) Provide a query that shows the top 5 most purchased tracks over all.

##############################################################################################
# 26) Provide a query that shows the top 3 best selling artists.

##############################################################################################
# 27) Provide a query that shows the most purchased Media Type.
