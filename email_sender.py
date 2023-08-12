import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_constants_from_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

constants = load_constants_from_json('constants.json')

def send_email(subject, content, to_email):
    try:
        from_email = constants['email']
        password = constants['password']

        # Set up the MIME structure
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(content, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)

        # Send the email
        server.sendmail(from_email, to_email, msg.as_string())
        server.quit()

        logger.info("Email sent successfully!")
    except Exception as e:
        logger.error("Error sending email: %s", str(e))

if __name__ == '__main__':
    subject = input("Subject: ")
    content = input("Email Content: ")
    to_email = input("To Email: ")
    send_email(subject, content, to_email)
