import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
# Create table
# Import Data


for row in c.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)
# Save (commit) the changes
# conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
