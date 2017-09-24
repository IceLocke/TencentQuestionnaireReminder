#主程序

import time
from TencentQuestionnaireReminder import analyze as funcs
from TencentQuestionnaireReminder import sendmail as mail

last_no = "0"

funcs.login()

while(True):
    print("----开始搜索网页----")
    now_no = funcs.getNo()
    if now_no is not last_no:
        mail.send(funcs.ana(now_no))
        print("------搜索结束------")
        time.sleep(60)
    else:
        print("-----没有新问卷-----")