
"""
Es soll eine einfache Veranstaltungsdatenbank entwickelt werden. Die Datenbank
speichert für eine Veranstaltung einen Namen, einen Ort und das Datum. Die
Verwaltung läuft über einen Web-Server mit der Bibliothek Flask [1, 2]. Für die
Datenhaltung wird eine MariaDB-Datenbank [3] benötigt.

Der Webserver enthält drei Endpunkte zur Verwaltung der Veranstaltungen:
 * /list - Ausgabe einer Liste aller Veranstaltungen
 * /add - Hinzufügen einer neuen Veranstaltung
 * /clear - Löschen aller gespeicherten Veranstaltungen

Hilfen:
 * Handbuch des Pakets Flask [1]
 * Einführender Artikel zu Flask [2]

Bibliotheken:
 * Flask - Leichtgewichtiges Web Application Framework
    pip install flask
 * MariaDB - MariaDB Connector/Python
    pip install mariadb

Quellen:
[1] https://flask.palletsprojects.com/en/2.1.x/
[2] https://www.heise.de/ratgeber/Python-Framework-fuer-Webentwicklung-Einfacher-Einstieg-mit-Flask-6340642.html
[3] https://mariadb.com/resources/blog/how-to-connect-python-programs-to-mariadb/

"""


import os
import sys
import webbrowser
from datetime import datetime

import mariadb
from flask import Flask
from flask import request


# initialisiere HTTP-Server
app = Flask(__name__)


# initialisiere Datenbank im selben Thread wie HTTP-Server und erzeuge Tabellen
try:
    db_user = os.getenv('VERANDB_USER', 'veranstaltungsdatenbank')
    db_password = os.getenv('VERANDB_PASSWORD', '12345678')
    db_name = os.getenv('VERANDB_DATABASE', 'veranstaltungsdatenbank')
    db_root_password = os.getenv('VERANDB_ROOT_PASSWORD', '12345678')
    connection = mariadb.connect(
        user=db_user,
        password=db_password,
        host='verandb-db',
        port=3306,
        database=db_name
    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS veranstaltungen (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT, place TEXT, date DATE)""")
cursor.execute("""INSERT INTO veranstaltungen VALUES (NULL, 'Konzert', 'Bühne 1', '2018-01-05')""")
cursor.execute("""INSERT INTO veranstaltungen VALUES (NULL, 'Weinprobe', 'Wein Müller GmbH', '2018-08-12')""")
cursor.execute("""INSERT INTO veranstaltungen VALUES (NULL, 'Infoveranstaltung', 'Stadthaus', '2018-07-22')""")
connection.commit()


# erzeuge Vorlage für alle Webseiten
html_template = """<html>
                     <head><title>{title}</title></head>
                     <style>
                       div a {{
                           background-color: #4CAF50;
                           color: white;
                           padding: 10px 32px;
                           margin: 4px 10px;
                           text-align: center;
                           text-decoration: none;
                           display: inline-block;
                           font-size: 14px;
                       }}
                       div {{
                           background-color: lightblue;
                           padding: 5px 5px;
                       }}
                     </style>
                     <body>
                       <div> Menü <a href="list">Veranstaltungen auflisten</a><a href="add">Veranstaltung hinzufügen</a><a href="clear">Veranstaltungen löschen</a></div>
                       <h1>{heading}</h1>
                       {content}
                     </body>
                   </html>"""


@app.route('/')
def info():
    text = 'VerAnDB - Veranstaltungsdatenbank!'
    content = '<p>Mögliche Funktionen:</p><ul><li>/list</li><li>/add</li></ul>'
    return html_template.format(title=text, heading=text, content=content)


@app.route('/list')
def list():
    title = 'Liste aller Veranstaltungen'
    heading = 'Liste aller Veranstaltungen'
    content = ''
    event_template = '<p>{name} am Ort {place} am {date}</p>'
    # hole alle Veranstaltungen aus der Datenbank
    cursor = connection.cursor()
    cursor.execute('SELECT name, place, date FROM veranstaltungen')
    for row in cursor.fetchall():
        # erzeuge HTML-Elemente für jede Veranstaltung aus der Datenbank
        name, place, date = row
        content += event_template.format(name=name, place=place, date=date)
    return html_template.format(title=title, heading=heading, content=content)


@app.route('/add', methods=['GET', 'POST'])
def add():
    title = 'Veranstaltung hinzufügen'
    heading = 'Veranstaltung hinzufügen'
    content = """<form action="/add" method="POST">
                   <p>Name: <input type="text" name="name" /></p>
                   <p>Ort: <input type="text" name="place" /></p>
                   <p>Datum (z.B. 24.02.2021): <input type="date" name="date" /></p>
                   <input type="submit" value="Absenden" />
                 </form>"""
    if request.method == 'POST':
        # hole Parameter aus POST-Request und schreibe Veranstaltung in Datenbank
        name = request.form.get('name')
        place = request.form.get('place')
        try:
            date = datetime.strptime(request.form.get('date'), '%Y-%m-%d')
        except ValueError:
            date = datetime.now()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO veranstaltungen VALUES (NULL, ?, ?, ?)',
                       (name, place, date.date().isoformat()))
        connection.commit()
    return html_template.format(title=title, heading=heading, content=content)


@app.route('/clear')
def clear():
    title = 'Datenbank gelöscht'
    heading = 'Datenbank gelöscht'
    content = 'Alle Veranstaltungen wurden aus der Datenbank gelöscht.'
    cursor = connection.cursor()
    cursor.execute('DELETE FROM veranstaltungen')
    connection.commit()
    return html_template.format(title=title, heading=heading, content=content)


if __name__ == '__main__':
    # webbrowser.open_new_tab('http://localhost:5000')
    app.run(host='0.0.0.0', debug=True)
