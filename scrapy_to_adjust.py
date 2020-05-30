import requests
from bs4 import BeautifulSoup
import pymysql
import time

headers = {
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}

con = pymysql.connect(host = 'localhost', user = 'root', passwd = 'Lin_1772815', db = 'biyesheji', port = 3306, charset = 'utf8')
cursor = con.cursor()

def get_infos(url):
    try:
        res = requests.get(url, headers = headers)
        soup = BeautifulSoup(res.text, 'lxml')
        colleges = soup.select('.forum_body_manage > tr > td:nth-child(2)')
        majors = soup.select('.forum_body_manage > tr > td:nth-child(3)')
        nums = soup.select('.forum_body_manage > tr > td:nth-child(4)')
        for college, major, num in zip(colleges, majors, nums):
            college = college.get_text().strip()
            major = major.get_text().strip()
            num = num.get_text().strip()
            cursor.execute("insert into to_adjust(college,major,num) values (%s,%s,%s)",(college, major,num))
            print('执行成功！')
    except:
        pass

if __name__ == "__main__":
    urls = ['http://muchong.com/bbs/kaoyan.php?&page={}'.format(str(i)) for i in range(1,472)]
    for url in urls:
        print(url)
        get_infos(url)
        time.sleep(1)
    con.commit()
    con.close()
