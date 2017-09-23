import time
from TencentQuestionnaireReminder import analyze as funcs
from TencentQuestionnaireReminder import sendmail as mail

last_no = "0"

if __name__ == "__main__":
    while(True):
        now_no = funcs.getNo()
        if now_no is not last_no:
            mail.send()(funcs.ana())
            time.sleep(60)