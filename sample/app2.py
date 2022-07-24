from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello, world2'

@app.route('/key1')
def key1():
    return os.environ['key1']

if __name__ == '__main__':
    app.run()
