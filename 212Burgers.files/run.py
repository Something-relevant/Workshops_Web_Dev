from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

MENUDB = 'menu.db'

@app.route('/') # / = landing page
def index():
    burgers = []
    drinks = []
    sides = []

    db = sqlite3.connect(MENUDB)
    print(db)


    curB = db.execute('SELECT burger,price FROM burgers')
    #curB = db.execute('SELECT burger,price FROM burgers ?', (userinput)) This substitutes if commands exist so they can not inject code
    curD = db.execute('SELECT drinks,price FROM drinks')
    curS = db.execute('SELECT side,price FROM sides')

    for row in curB:
        burgers.append(list(row)) #list converts it to a list
    for row in curD:
        drinks.append(list(row))
    for row in curS:
        sides.append(list(row))

    db.close() #remember to always close database connection

    return render_template('index.html',
    disclaimer='may contain traces of nuts',
    burgers = burgers,
    drinks = drinks,
    sides = sides
    )

@app.route('/order')
def order():
    return render_template('order.html')
