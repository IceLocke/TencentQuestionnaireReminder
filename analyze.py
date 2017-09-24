#解析问卷模块

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

import time

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
main_url = "https://wj.qq.com/stat_recycle.html?id=1491015"
driver = webdriver.Safari()

def login():
    #获取界面
    driver.get(main_url)
    time.sleep(2)

    #进入登入界面
    qqLoginImg = driver.find_element_by_id("loginTabQQ")
    qqLoginImg.click()
    time.sleep(6)

    #寻找所在QQ
    accountImg = driver.find_element_by_xpath('//*[@id="img_out_"]')
    accountImg.click()


def getNo():
    driver.get(main_url)
    bs = BeautifulSoup(driver.page_source, "lxml")

    list = bs.find("tbody",{"id":"list"}).tr.findAll("td",limit=3)
    print("The Lastest ID: " + list[2])
    return list[2]


def ana(ID):
    url = "https://wj.qq.com/stat_recycle_answer.html?id=1491015#p1&" + ID

    driver.get(url)

    return driver.page_source