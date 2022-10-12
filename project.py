print('hello world')

from distutils.log import debug
from flask import Flask

app = Flask(__name__)


@app.route('/', methods = ['POST', 'GET'])

def Index():
    return 'CI/CD pipeline has been created'


if __name__ == '__main__':
    app.run()