import os
import flask
from flask import Flask, send_from_directory, request

app = Flask(__name__, static_folder='../react/build')

# Serve React App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if(path == ""):
        return send_from_directory('../react/build', 'index.html')
    else:
        if(os.path.exists("../react/build/" + path)):
            return send_from_directory('../react/build', path)
        else:
            return send_from_directory('../react/build', 'index.html')


@app.route('/api/home')
def home():
    text = """
**The wind is a symphony in Skye’s soul and she is its conductor.**

Skye’s father, the legally insane god of storm, sea, earthquake and every 
other disaster medieval Japan could imagine, is currently dead, but he 
loves her very much.

Like many powerful esomorphs, the government came for her when her power 
first appeared.  They sent her to live apart from society, surrounded by 
U.S. Marines where she was safe and the world was safe from her.  That’s when 
her training began.

It wasn’t the life she would have chosen, but it was a life she could live 
with. Or it was until a conspiracy of Washington power brokers
forced her to run or kill.
Already stained with blood spilled in her name, she ran.
But was there any refuge
from the government now doing the conspiracy’s bidding?

If she can’t discover what the conspirators want and stop them before her 
father returns from the dead, the streets will flow red with innocent blood.
    """
    return flask.json.jsonify({'text': text})

@app.route('/api/join')
def join():
    print(request.args.get('email'))
    return flask.json.jsonify({'response': 'success'})

if __name__ == '__main__':
    app.run(use_reloader=True, port=5000, threaded=True)