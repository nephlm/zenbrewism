import os

import pymysql

import flask
from flask import Flask, send_from_directory, request
from flask_htpasswd import HtPasswdAuth

app = Flask(__name__, static_folder='../react/build')
app.config.from_object('config')
app.config['FLASK_HTPASSWD_PATH'] = '.htpasswd'
app.config['FLASK_SECRET'] = 'U0B!sqOBaK6!@xf^HL2Et69c'
app.config['DEBUG'] = True

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
        print('return react/index')
        return send_from_directory('../react/build', 'index.html')
    elif path.startswith('edit'):
        print('return edit')
        return serve_admin(path)
    else:
        for react_app in ('react', 'edit'):
            file_path = f'../{react_app}/build/{path}'
            if(os.path.exists(file_path)):
                print(file_path)
                return send_from_directory(f'../{react_app}/build', path)
            
        # if(os.path.exists("../react/build/" + path)):
        #     print('react/something')
        #     return send_from_directory('../react/build', path)
        # if(os.path.exists("../edit/build/" + path)):
        #     print('edit/something')
        #     return send_from_directory('../edit/build', path)
        # else:
        #     print('react/index')
        #     return send_from_directory('../react/build', 'index.html')
        print('fall through')
        return send_from_directory('../react/build', 'index.html')

@htpasswd.required
def serve_admin(path, user):
    return send_from_directory('../edit/build', 'index.html')
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
        conn.encoding = 'utf8'
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

@app.route('/api/blog')
def blog():
    cur = execute(None, "select * from cms order by slug", [])
    ret = {}
    if cur:
        for row in cur:
            row['content'] = str(row['content'], 'utf8')
            ret[row['id']] = dict(row)
        return flask.json.jsonify(ret)

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)