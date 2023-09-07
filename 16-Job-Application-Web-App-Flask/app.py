import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message


load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv('APP16_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = os.getenv('APP16_USER_EMAIL')
app.config['MAIL_PASSWORD'] = os.getenv('APP16_USER_PASSWORD')

db = SQLAlchemy(app)

mail = Mail(app)


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
        date_obj = datetime.strptime(start_date, '%Y-%m-%d')
        occupation = request.form['occupation']
        # print([first_name, last_name, email_id, start_date, occupation])

        form = Form(first_name=first_name,
                    last_name=last_name,
                    email_id=email_id,
                    start_date=date_obj,
                    occupation=occupation)

        db.session.add(form)
        db.session.commit()

        message_body = (f"Thank you for your Job Application, {first_name}.\n\n"
                        f"Here are your submitted details:\n"
                        f"Name: {first_name} {last_name}\n"
                        f"Starting Date: {start_date}\n\n"
                        f"regards,\n"
                        f"Company.")
        message = Message(subject="New form submission",
                          sender=app.config['MAIL_USERNAME'],
                          recipients=[email_id],
                          body=message_body)
        mail.send(message)

        flash(f"{first_name}, your form was submitted successfully!", 'success')

    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True, port=5001)
