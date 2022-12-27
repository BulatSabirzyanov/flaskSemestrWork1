DROP TABLE IF EXISTS orders;

CREATE TABLE orders(
id INTEGER PRIMARY KEY AUTOINCREMENT ,
created TIMESTAMP default CURRENT_TIMESTAMP not null,
title TEXT NOT NULL
);

DROP TABLE  IF EXISTS products;

CREATE TABLE products(
    id          INTEGER primary key autoincrement,
    order_id     INTEGER NOT NULL,
    uploaded    TIMESTAMP default CURRENT_TIMESTAMP not null,
    name        TEXT                                not null,
    description TEXT                                not null,
    price       INTEGER                             not null,
    FOREIGN KEY (order_id) REFERENCES orders (id)
);