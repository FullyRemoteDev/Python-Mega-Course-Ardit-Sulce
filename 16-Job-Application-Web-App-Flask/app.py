from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('APP16_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80))
    last_name = db.Column(db.String(80))
    email_id = db.Column(db.String(80))
    start_date = db.Column(db.Date)
    occupation = db.Column(db.String(80))


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email_id = request.form['email_id']
        start_date = request.form['date']
        occupation = request.form['occupation']
        # print([first_name, last_name, email_id, start_date, occupation])

    elif request.method == 'GET':
        pass

    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
