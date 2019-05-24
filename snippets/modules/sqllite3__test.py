
# %%
# need need to install sqlite3. It's part of python

import sqlite3

# create a database in memory
conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute('''
    create table stocks
    (date text, trans text, symbol text, qty real, price real)
''')

c.execute('''
    insert into stocks values ('2006-01-05', 'BUY', 'RHAT', 100, 35.15)
''')

conn.commit()

t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

conn.close()
# %%
# 1. Create a database
conn = sqlite3.connect('example.db')

c = conn.cursor()

c.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)
            ''')

# Insert a row of data
c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()

# %%
# 2. Get data
conn = sqlite3.connect('example.db')

c = conn.cursor()

t = ('RHAT',)
c.execute('SELECT * FROM stocks WHERE symbol=?', t)
print(c.fetchone())

# Larger example that inserts many records at a time
purchases = [('2006-03-28', 'BUY', 'IBM', 1000, 45.00),
             ('2006-04-05', 'BUY', 'MSFT', 1000, 72.00),
             ('2006-04-06', 'SELL', 'IBM', 500, 53.00),
            ]
c.executemany('INSERT INTO stocks VALUES (?,?,?,?,?)', purchases)

#%%
for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

conn.commit()

conn.close()
