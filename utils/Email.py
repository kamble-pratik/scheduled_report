import smtplib
import ssl
from tasks import read_yaml,zipping
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
cfg = read_yaml('secretes.yaml')

zipfile = "D:\\maza karbhar\\Schedular_Project\\data\\Load\\Load.zip"


class Email:

    def __init__(self):
        self.sender = cfg['sender']
        self.receiver = cfg['receiver']
        self.host = cfg['host']
        self.port = cfg['port']
        self.password = cfg['password']

    def template(self):
        self.em = MIMEMultipart()
        self.em['From'] = self.sender
        self.em['To'] = self.receiver
        self.em['subject'] = 'mail from python'

        if zipping():

            self.em.attach(MIMEText('body of the mail'))

            with open (zipfile,'rb') as attachment:
                self.em.attach(MIMEApplication(attachment.read(), Name="Load.zip"))
            print('\nattachment done')

        else:
            self.em.attach(MIMEText('no new files'))


    def send_mail(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(self.host,self.port,context = context) as smtp:
            smtp.login(self.sender,self.password)
            print('logged in')
            smtp.sendmail(self.sender,self.receiver,self.em.as_string())
            print('mail sent')



if __name__ == "__main__":
    pass
