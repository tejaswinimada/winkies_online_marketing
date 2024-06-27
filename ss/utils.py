from django.core.mail import send_mail
from django.conf import settings

def send_email_client():
    subject="check this oppurtunity Mr.Kuruva"
    message="hey,Mr.kuruva Bhanu Prakash,her is the attachment you have appiled for the role as Mr.sir garu,congratulations you have been selected meet you soon.dont talk to me by the way."

    from_email=settings.EMAIL_HOST_USER
    recipient_list=["tejaswini.mada16@gmail.com"]
    send_mail(subject,message,from_email,recipient_list)