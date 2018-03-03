from flask import Flask
from flask_htpasswd import HtPasswdAuth

app = Flask(__name__, static_folder='../react/build')
app.config.from_object('toddkaye.config')
app.config['FLASK_HTPASSWD_PATH'] = '.htpasswd'
app.config['FLASK_SECRET'] = 'U0B!sqOB8%-~dptJhjGHaK6!@xf^HL2Et69c'
app.config['DEBUG'] = True

htpasswd = HtPasswdAuth(app)


import toddkaye.views