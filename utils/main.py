from Email import Email
from tasks import Timer,flush
from datetime import datetime


def job():
    flush()
    mail_obj = Email()
    mail_obj.template()
    mail_obj.send_mail()
    now = datetime.now().time()
    print(now)

if __name__ == "__main__":
    Timer(job,10)