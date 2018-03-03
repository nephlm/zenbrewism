import os

import pymysql

from toddkaye import app
from toddkaye import htpasswd
import toddkaye.models as models

from flask import Flask, send_from_directory, request
import flask

REACT = '../../react/'
BUILD = os.path.join(REACT, 'build')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """
    dev static serving
    """
    print(f'~{path}')
    if path == "":
        print('return react/index')
        return send_from_directory(BUILD, 'index.html')
    elif path.startswith('edit'):
        print('return edit')
        return serve_admin(path)
    else:
        return send_from_directory(BUILD, path)
    # else:
    #     for react_app in ('react', 'edit'):
    #         file_path = os.path.join('../{react_app}/build/{path}'
    #         if(os.path.exists(file_path)):
    #             print(file_path)
    #             return send_from_directory(f'../{react_app}/build', path)
            
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

@htpasswd.required
@app.route('/api/cms/', defaults={'slug': ''})
@app.route('/api/cms', defaults={'slug': ''})
@app.route('/api/cms/<slug>')
def get_cms(slug):
    if not slug:
        slug = ''
    print(f'[[{slug}]]')
    cms = models.CMS.get_by_slug(slug)
    return cms.text

@app.route('/api/home')
def home():
    slug = ''
    cms = models.CMS.get_by_slug(slug)
    if cms:
        return flask.json.jsonify({'text': cms.text})
    return flask.json.jsonify({'text': ''})
    # cur = execute(None, "select * from cms where slug=%s", [slug])
    # if cur:
    #     print(cur)
    #     row = cur.fetchone()
    #     if row:
    #         content = str(row['content'], 'utf8')
    #     else:
    #         content = ''
    #     return flask.json.jsonify({'text': content})

# def get_conn():
#     host = app.config['HOST']
#     port = app.config['PORT']
#     username = app.config['USERNAME']
#     password = app.config['PASSWORD']
#     conn = pymysql.connect(host=host, 
#                         port=port, 
#                         user=username, 
#                         passwd=password,
#                         db=app.config['SCHEMA'])
#     return conn

# def get_cursor(conn=None):
#     if conn is None:
#         conn = get_conn()
#         conn.encoding = 'utf8'
#     return conn.cursor(pymysql.cursors.DictCursor)

# def execute(cursor, sql, params):
#     if cursor is None:
#         cursor = get_cursor()
#     cursor.execute(sql, params)
#     return cursor


# @app.route('/api/blog')
# def blog():
#     entries = models.CMS.all()
#     #cur = execute(None, "select * from cms order by slug", [])
#     ret = {}
#     if entries:
#         for row in entries:
#             row['content'] = row.text
#             ret[row['id']] = dict(row)
#         return flask.json.jsonify(ret)




