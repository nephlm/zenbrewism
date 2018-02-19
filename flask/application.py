import os

import pymysql

import flask
from flask import Flask, send_from_directory, request
from flask_htpasswd import HtPasswdAuth

app = Flask(__name__, static_folder='../react/build')
app.config.from_object('config')
app.config['FLASK_HTPASSWD_PATH'] = '.htpasswd'
app.config['FLASK_SECRET'] = 'U0B!sqOBaK6!@xf^HL2Et69c'

htpasswd = HtPasswdAuth(app)

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """
    dev static serving
    """
    print(path)
    if path == "":
        return send_from_directory('../react/build', 'index.html')
    elif path.startswith('edit/'):
        return serve_admin(path)
    else:
        if(os.path.exists("../react/build/" + path)):
            return send_from_directory('../react/build', path)
        else:
            return send_from_directory('../react/build', 'index.html')

@htpasswd.required
def serve_admin(path, user):
    return "no"

def get_conn():
    host = app.config['HOST']
    port = app.config['PORT']
    username = app.config['USERNAME']
    password = app.config['PASSWORD']
    conn = pymysql.connect(host=host, 
                        port=port, 
                        user=username, 
                        passwd=password,
                        db=app.config['SCHEMA'])
    return conn

def get_cursor(conn=None):
    if conn is None:
        conn = get_conn()
    return conn.cursor(pymysql.cursors.DictCursor)

def execute(cursor, sql, params):
    if cursor is None:
        cursor = get_cursor()
    cursor.execute(sql, params)
    return cursor

@app.route('/api/home')
def home():
    slug = '/'
    cur = execute(None, "select * from cms where slug=%s", [slug])
    if cur:
        print(cur)
        row = cur.fetchone()
        if row:
            content = str(row['content'], 'utf8')
        else:
            content = ''
        return flask.json.jsonify({'text': content})

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)