from django.core.mail import EmailMessage


def sendEmail(to,sub,body):
    email = EmailMessage(sub,body,to = ['usamak552@gmail.com'])
    email.send()
    print("email send")