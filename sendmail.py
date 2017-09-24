#邮箱模块，内容使用html

import smtplib
from email.mime.text import MIMEText

def send(passage):
    print("Sending Mail...")

    mail = MIMEText(passage, "html", "utf-8")
    mail['Subject'] = "新问卷提醒"
    mail['From'] = ""
    mail['To'] = ""

    smtp = smtplib.SMTP("localhost")
    smtp.send(mail)
    smtp.quit()