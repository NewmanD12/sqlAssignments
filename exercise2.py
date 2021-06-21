import csv, sqlite3
import os
from pprint import pprint



print(os.getcwd())
os.chdir(r'/Users/dakota/Desktop/codeImmersives/mySQL')  
print(os.getcwd())
#=====================================================
conn = sqlite3.connect('hardware_store.db')
c = conn.cursor()


with open('inventory.csv','r') as fin:
  dr = csv.DictReader(fin)
  all_vals = []
  for entry in dr:
    all_items = list(entry.values())[:-1]
    price_extended = round(float(entry.get('price')) * int(entry.get('quantity')), 2)
    # print(all_items)
    # print(price_extended)
    # infoToPass = tuple(all_items)
    all_items.append(price_extended)
    all_vals.append(tuple(all_items))
  print(all_vals) 
    
    # print(all_items)
    # all_items += tuple(entry.values())

# print(all_items)

c.execute("""DROP TABLE items""")
  
c.execute("""CREATE TABLE IF NOT EXISTS items (
    item_id TEXT,
    itemName TEXT,
    price REAL,
    quantity INT,
    price_extended REAL)
""")

c.executemany("""INSERT INTO items VALUES (?,?,?,?,?)""", all_vals)
conn.commit()

print(c.rowcount)


conn.close()

# c.executemany("""INSERT INTO customers VALUES (?,?,?,?,?)""", all_customers)

