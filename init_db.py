import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO orders (title) VALUES (?)", ('Breakfast',))
cur.execute("INSERT INTO orders (title) VALUES (?)", ('Launch',))
cur.execute("INSERT INTO orders (title) VALUES (?)", ('Dinner',))

cur.execute("INSERT INTO products (order_id,name, description, price) VALUES (?, ?, ?, ?)",
            (1, 'Eggs', 'DefaultEggs for cooking breakfast', 53)
            )

cur.execute("INSERT INTO products (order_id,name, description, price) VALUES (?, ?, ?, ?)",
            (1, 'Bread', 'Some bread for doing sandwich', 40)
            )

cur.execute("INSERT INTO products (order_id,name, description, price) VALUES (?, ?, ?, ?)",
            (1, 'Bitter', 'A little bit Bitter 80 %  for doing sandwich', 40)
            )

cur.execute("INSERT INTO products (order_id,name, description, price) VALUES (?, ?, ?, ?)",
            (2, 'Potato', '1kg potato for cooking soup', 69)
            )

cur.execute("INSERT INTO products (order_id,name, description, price) VALUES (?, ?, ?, ?)",
            (2, 'HorseMeat', '0.7kg meat for cooking soup', 200)
            )

cur.execute("INSERT INTO products (order_id,name, description, price) VALUES (?, ?, ?, ?)",
            (3, 'Cheese', '0.5kg cheese for cooking pasta', 300)
            )

cur.execute("INSERT INTO products (order_id,name, description, price) VALUES (?, ?, ?, ?)",
            (3, 'Pasta', '1 Pocket', 100)
            )

connection.commit()
connection.close()
