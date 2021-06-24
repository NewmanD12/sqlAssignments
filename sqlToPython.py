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

##############################################################################################
# 4) Provide a query showing only the Employees who are Sales Agents.

##############################################################################################
# 5) Provide a query showing a unique list of billing countries from the Invoice table.

##############################################################################################
# 6) Provide a query showing the invoices of customers who are from Brazil.

##############################################################################################
# 7) Provide a query that shows the invoices associated with each sales agent. The resultant table should include the Sales Agent's full name.

##############################################################################################
# 8) Provide a query that shows the Invoice Total, Customer name, Country and Sale Agent name for all invoices and customers.

##############################################################################################
# 9) How many Invoices were there in 2009 and 2011? What are the respective total sales for each of those years?

##############################################################################################
# 10) Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for Invoice ID 37.

##############################################################################################
# 11) Looking at the InvoiceLine table, provide a query that COUNTs the number of line items for each Invoice. HINT: GROUP BY

##############################################################################################
# 12) Provide a query that includes the track name with each invoice line item.

##############################################################################################
# 13) Provide a query that includes the purchased track name AND artist name with each invoice line item.

##############################################################################################
# 14) Provide a query that shows the # of invoices per country. HINT: GROUP BY

##############################################################################################
# 15) Provide a query that shows the total number of tracks in each playlist. The Playlist name should be include on the resultant table.

##############################################################################################
# 16) Provide a query that shows all the Tracks, but displays no IDs. The resultant table should include the Album name, Media type and Genre.

##############################################################################################
# 17) Provide a query that shows all Invoices but includes the # of invoice line items.

##############################################################################################
# 18) Provide a query that shows total sales made by each sales agent.

##############################################################################################
# 19) Which sales agent made the most in sales in 2009?

##############################################################################################
# 20) Which sales agent made the most in sales in 2010?

##############################################################################################
# 21) Which sales agent made the most in sales over all?

##############################################################################################
# 22) Provide a query that shows the # of customers assigned to each sales agent.

##############################################################################################
# 23) Provide a query that shows the total sales per country. Which country's customers spent the most?

##############################################################################################
# 24) Provide a query that shows the most purchased track of 2013.

##############################################################################################
# 25) Provide a query that shows the top 5 most purchased tracks over all.

##############################################################################################
# 26) Provide a query that shows the top 3 best selling artists.

##############################################################################################
# 27) Provide a query that shows the most purchased Media Type.
