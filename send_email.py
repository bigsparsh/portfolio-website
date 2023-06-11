import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

password = 'qpualuaxrffxlgls'
username = 'pythonsample4@gmail.com'


def email_sender(message, email):
    my_context = ssl.create_default_context()
    subject = message.split(' ')[[len(i) for i in message.split(' ')].index(max([len(i) for i in message.split(' ')]))]
    greetings = f'subject:{subject.capitalize()}\nHey Sparsh,\n{message}\nBy - {email}'
    receiver = 'sparshsingh7586@gmail.com'
    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, greetings)
