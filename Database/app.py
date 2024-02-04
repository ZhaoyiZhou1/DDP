from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db = SQLAlchemy(app)

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)
    guests = db.Column(db.Integer, nullable=False)
    phone = db.Column(db.String(10), nullable=False)
    notes = db.Column(db.String(1000), nullable=False)
    
    def __repr__(self):
        return f'<Booking {self.name}>'

# Route for sending email
@app.route('/')
def form():
    return render_template('reservation.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    date = request.form['date']
    time = request.form['time']
    guests = request.form['guests']
    phone = request.form['phone']
    notes = request.form['notes']
    try:
        new_booking = Booking(name=name, email=email, date=date, time=time, guests=guests, phone=phone, notes=notes)
        db.session.add(new_booking)
        db.session.commit()
        return 'Booking Successful'
    except Exception as e:
        return f'An error occurred: {e}'
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route for sending email
@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = 'warwick_restaurant@warwick.ac.uk' 
    msg['Subject'] = subject

    body = f"Message from {name} ({email}):\n\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    # SMTP server configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port
    smtp_username = 'your_username'  # Replace with your SMTP username
    smtp_password = 'your_password'  # Replace with your SMTP password

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        return 'Message sent successfully!'
    except Exception as e:
        return f'Error: {e}'

def send_email_confirmation(name, email, date, time):
    subject = "Booking Confirmation"
    body = f"Dear {name},\n\nYour booking for {date} at {time} has been confirmed.\n\nThank you!"
    send_email(email, subject, body)

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
    app.run(debug=True)
    
    
# Collecting the Email Data: Usually, this data comes from a form on the website where users enter details like their email, name, message, etc.
# Backend Process to Send Email: This involves setting up a Python script on the server that takes the collected data and sends an email.

#This script sets up a basic Flask application with two routes:
# "/" displays a form to the user.
# "/send_email" handles form submissions and sends an email using the provided details.