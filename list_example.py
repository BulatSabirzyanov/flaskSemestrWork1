from itertools import groupby
from app import get_db_connection

conn = get_db_connection()
todos = conn.execute('SELECT i.name, l.title FROM products i JOIN orders l \
                        ON i.order_id = l.id ORDER BY l.title;').fetchall()

orders = {}

for k, g in groupby(todos, key=lambda t: t['title']):
    orders[k] = list(g)

for list_, items in orders.items():
    print(list_)
    for item in items:
        print('    ', item['name'])