#未完成！

from bs4 import BeautifulSoup
import requests

session = requests.Session()
headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}


def getNo():
    url = "https://wj.qq.com/stat_recycle.html?id=1491015"
    req = session.get(url, headers=headers)
    bs = BeautifulSoup(req.text, "lxml")

    list = bs.find("tbody",{"id":"list"}).tr.findAll("td",limit=3)
    print("The Lastest ID: " + list[2])
    return list[2]


def ana(ID):
    url = "https://wj.qq.com/stat_recycle_answer.html?id=1491015#p1&" + ID
    req = session.get(url, headers=headers)
    return req.text