from flask import Flask
import os

app3 = Flask(__name__)

@app3.route('/')
def index():
    return 'hello, world2'

@app3.route('/key1')
def key1():
    return os.environ['key1']

if __name__ == '__main__':
    app3.run()
