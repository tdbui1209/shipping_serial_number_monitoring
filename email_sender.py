import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class EmailSender:
    def __init__(self, sender_email, receiver_email, subject, message, host, port, password):
        self.sender_email = sender_email
        self.receiver_email = receiver_email
        self.subject = subject
        self.message = message
        self.host = host
        self.port = port
        self.password = password

    def send_email(self):
        # Create the email message
        message = MIMEMultipart()
        message['From'] = self.sender_email
        message['To'] = self.receiver_email
        message['Subject'] = self.subject
        message.attach(MIMEText(self.message, 'html'))

        # Send the email
        with smtplib.SMTP(host=self.host, port=self.port) as server:
            server.login(self.sender_email, self.password)
            server.send_message(message)
