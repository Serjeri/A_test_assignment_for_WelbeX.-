from flask import Flask, render_template, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# подключение к базе

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@localhost:8080/Single Page Application'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class valuem(db.Model):
    tablNane = 'valuem'
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(40))


@app.route('/')
def form():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def wallet_refresh(pageNumber, columnName, condition, value):
    pageNumber = 1
    #columnName = filter data 
    #condition = 
    #value

if __name__ == '__main__':
    app.run(debug=True)
 