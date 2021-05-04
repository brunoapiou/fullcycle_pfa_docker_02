import time
import os

from flask import Flask
import mysql.connector

modulos = [('Docker',), ('Padrões e técnicas avançadas com Git e Github',), ('Integração contínua',), ('Kubernetes',)]

class DBManager:
    def __init__(self, database='desafio', host="mysql", user="root", password="1234"):        
        self.connection = mysql.connector.connect(
            user=user, 
            password=password,
            host=host, # name of the mysql service as set in the docker-compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        
        self.cursor = self.connection.cursor()
    
    def populate_db(self):
        global modulos
        self.cursor.execute('DROP TABLE IF EXISTS tab_modulos;')
        self.cursor.execute('CREATE TABLE tab_modulos (id INT AUTO_INCREMENT PRIMARY KEY, modulo VARCHAR(255));')
        self.cursor.executemany('INSERT INTO tab_modulos (modulo) VALUES (%s);', modulos)
        self.connection.commit()
    
    def query_titles(self):
        self.cursor.execute('SELECT modulo FROM tab_modulos')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec


server = Flask(__name__)
conn = None

@server.route('/')
def listModulos():
    global conn
    if not conn:
        conn = DBManager()        
    rec = conn.query_titles()

    response = '<h1>Full Cycle</h1>'
    for c in rec:
        response = response  + '<div>' + c + '</div>'
    return response

@server.route('/populate')
def populate():
    global conn
    if not conn:
        conn = DBManager()
    conn.populate_db()

    return '<p>Database populated</p>'
        

#if __name__ == '__main__':
#    server.run()