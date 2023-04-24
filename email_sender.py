import smtplib
from email.message import EmailMessage

"""
creating an instance of an email 
when the instance is created, password is required and the email is logged in.
the instance should terminate once the email sending processes are complete
terminate by calling the finish() method
"""


class EmailSender:
    my_email = "wanambisijoe@gmail.com"
    smtpObj = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    def __init__(self):
        EmailSender.smtpObj.login(EmailSender.my_email, input("enter password\n"))

    @staticmethod
    def send_email(receiver_email, subject, body):
        em = EmailMessage()

        em['From'] = EmailSender.my_email
        em['To'] = receiver_email
        em['Subject'] = subject
        em.set_content(body)
        em = em.as_string()

        EmailSender.smtpObj.sendmail(EmailSender.my_email, receiver_email, em)

    @staticmethod
    def finish():
        EmailSender.smtpObj.quit()


emObj = EmailSender()
emObj.send_email("johannezwatulo@outlook.com", "TRY", "Hello master")
emObj.finish()
