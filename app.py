import datetime
from itertools import groupby

from flask import Flask, request, make_response, render_template, url_for, redirect, flash
import random
import time
import sqlite3
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this should be a secret random string'


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_product(pid):
    conn = get_db_connection()
    product = conn.execute('SELECT * FROM products WHERE id = ?',
                           (pid,)).fetchone()
    conn.close()
    if product is None:
        abort(404)
    return product


@app.route('/')
@app.route('/product')
def product_list():
    conn = get_db_connection()
    todos = conn.execute('SELECT i.name, l.title FROM products i JOIN orders l \
                          ON i.order_id = l.id ORDER BY l.title;').fetchall()

    lists = {}

    for k, g in groupby(todos, key=lambda t: t['title']):
        lists[k] = list(g)

    conn.close()
    return render_template('list.html', lists=lists)

@app.route('/product/create', methods=('GET', 'POST'))
def create():
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        order_title = request.form['list']

        if not name:
            flash('Name is required!')
            return redirect(url_for('product_list'))

        order_id = conn.execute('SELECT id FROM orders WHERE title = (?);',
                               (order_title,)).fetchone()['id']
        conn.execute('INSERT INTO products (name, order_id, description, price) VALUES (?, ?)',
                     (name, order_id, description, price))
        conn.commit()
        conn.close()
        return redirect(url_for('product_list'))

    lists = conn.execute('SELECT title FROM orders;').fetchall()

    conn.close()
    return render_template('create.html', lists=lists)


@app.route('/product/<int:pid>/edit', methods=('GET', 'POST'))
def edit(pid):
    product = get_product(pid)

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        if not name:
            flash("Name is required!")
        else:
            conn = get_db_connection()
            conn.execute('UPDATE products SET name = ?, price = ?, description = ?'
                         ' WHERE id = ?',
                         (name, price, description, product['id']))
            conn.commit()
            conn.close()
            return redirect(url_for('product_list'))
    return render_template("edit.html", product=product)

@app.route("/product/<int:pid>/delete", methods=('GET', 'POST'))
def delete(pid):
    conn = get_db_connection()
    product = get_product(pid)
    if request.method == 'GET':
        return render_template('delete.html', product=product)
    if request.method == 'POST':
        conn.execute("DELETE FROM products WHERE id=?", (product['id'],))
        conn.commit()
        conn.close()
        return redirect(url_for('product_list'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
