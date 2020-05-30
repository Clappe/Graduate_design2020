#此程序用于获取高校url

import requests
import pymysql
from bs4 import BeautifulSoup
import urllib
from urllib.parse import quote

url = 'https://yz.chsi.com.cn/sch/'             
school_name = []                                 #学校名称列表
school_urls = []
conn = pymysql.connect(host = 'localhost', user = 'root', passwd = 'Lin_1772815', db = 'biyesheji', port = 3306, charset = 'utf8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}
cursor = conn.cursor()


def get_school_names(url):
    try:
        res = requests.get(url, headers = headers)
        soup = BeautifulSoup(res.text, 'lxml')
        names = soup.select('body > div.main-wrapper > div.container > div.yxk-table > table > tbody > tr > td:nth-child(1) > a')
        for item in names:
            name = item.get_text().strip()
            print(name)
            cursor.execute("insert into school_name(name) values (%s)", name)
            conn.commit()
       
    except:
        pass

if __name__ == "__main__":
    urls = ['https://yz.chsi.com.cn/sch/?start={}'.format(str(i)) for i in range(0,840,20)] #研招网网址
    for url in urls:
        get_school_names(url)
    

   
    
    


