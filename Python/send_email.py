# Translating the PHP script to Python

python_code = """
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(from_email, name, subject, number, message):
    to_email = "rockybd1995@gmail.com"
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = "You have a message from your Bitmap Photography."

    body = f"Name: {name}\\nEmail: {from_email}\\nNumber: {number}\\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # SMTP server configuration
    smtp_server = 'smtp.example.com'  # Replace with your SMTP server
    smtp_port = 587  # Replace with your SMTP port
    smtp_username = 'your_username'  # Replace with your SMTP username
    smtp_password = 'your_password'  # Replace with your SMTP password

    # Sending the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)
        server.quit()
        print("Successfully sent email")
    except Exception as e:
        print(f"Error: unable to send email. {e}")

# Example usage (you would get these values from your web form)
send_email('example@example.com', 'John Doe', 'Subject Here', '1234567890', 'Your message here')
"""

print(python_code)
