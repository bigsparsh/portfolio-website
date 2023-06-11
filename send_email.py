import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

password = 'qpualuaxrffxlgls'
username = 'pythonsample4@gmail.com'


def email_sender(receiver, message):
    my_context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
