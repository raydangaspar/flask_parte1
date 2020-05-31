from flask import Flask
from flask_mysqldb import MySQL


app = Flask(__name__)
app.config.from_pyfile('config.py')

db = MySQL(app)
# db.connection

from views import *

# Garantir que esse código não seja 
# executado quando este arquivo for importado por outro arquivo.
if __name__ == '__main__':
    app.run(debug=True)
