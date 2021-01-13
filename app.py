from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():

    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE increment ( icount INT NOT NULL DEFAULT 0 )''')
        cursor.execute('''INSERT INTO increment (icount) VALUES (0)''')
        conn.commit()
    except Exception as e:
        print('DB already created')

    html = "<h3>Привет!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>"
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())


@app.route("/plus")
def plus():
    import sqlite3
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''CREATE TABLE increment ( icount INT NOT NULL DEFAULT 0 )''')
        cursor.execute('''INSERT INTO increment (icount) VALUES (0)''')
        conn.commit()
    except Exception as e:
        print('DB already created')
    cursor.execute('SELECT icount FROM increment')
    current = cursor.fetchone()[0] + 1
    cursor.execute(f'UPDATE increment SET icount = {current}')
    conn.commit()
    html = f"<h3>Количество: {current}</h3>"
    return html