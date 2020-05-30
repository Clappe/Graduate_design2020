from bs4 import BeautifulSoup
import requests
import pymysql
import urllib
from urllib.parse import quote
import time

headers = {
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36'
}

conn = pymysql.connect(host='localhost',user='root',passwd='Lin_1772815',db='biyesheji',port=3306,charset='utf8')
cursor = conn.cursor()

school_names = []
numbers = []

def get_school_url(school_name, number):                                          
    try:
        school_name = urllib.parse.quote(school_name)
        major_number = urllib.parse.quote(number)
        url = 'https://yz.chsi.com.cn/zsml/querySchAction.do?ssdm=&dwmc=' + 
        school_name + '&mldm=&mlmc=&yjxkdm=' + major_number + '&xxfs=&zymc='
        print(url)
        return url
    except:
        pass

def get_Major_Page(url):
    try:
        res = requests.get(url, headers = headers)
        soup = BeautifulSoup(res.text, 'lxml')
        zhaoshengdanwei = soup.select('body > div.main-wrapper > div.container.clearfix'\
            ' > div.zsml-left > div.zsml-wrapper > table > tbody > tr:nth-child(1) > td:nth-child(2)')
        yuanxisuo = soup.select('body > div.main-wrapper > div.container.clearfix '\
            '> div.zsml-left > div.zsml-wrapper > table > tbody > tr:nth-child(2) > td:nth-child(2)')
        zhuanye = soup.select('body > div.main-wrapper > div.container.clearfix '\
            '> div.zsml-left > div.zsml-wrapper > table > tbody > tr:nth-child(3) > td:nth-child(2)')
        xuexifangshi = soup.select('body > div.main-wrapper > div.container.clearfix '\
            '> div.zsml-left > div.zsml-wrapper > table > tbody > tr:nth-child(3) > td:nth-child(4)')
        yanjiufangxiang = soup.select('body > div.main-wrapper > div.container.clearfix '\
            '> div.zsml-left > div.zsml-wrapper > table > tbody > tr:nth-child(4) > td:nth-child(2)')
        num = soup.select('body > div.main-wrapper > div.container.clearfix > '\
            'div.zsml-left > div.zsml-wrapper > table > tbody > tr:nth-child(5) > td.zsml-summary')

        zhaoshengdanwei = str(zhaoshengdanwei).split(')')[1].split('<')[0]
        yuanxisuo = str(yuanxisuo).split(')')[1].split('<')[0]
        zhuanye = str(zhuanye).split('>')[1].split('<')[0]
        xuexifangshi = str(xuexifangshi).split('>')[1].split('<')[0]
        yanjiufangxiang = str(yanjiufangxiang).split(')')[1].split('<')[0]
        num = str(num).split('：')[1].split('(')[0]

        cursor.execute("insert into infos(zhaoshengdanwei,yuanxisuo,zhuanye,"\
            "xuexifangshi,yanjiufangxiang,num) values(%s,%s,%s,%s,%s,%s)"
            ,(zhaoshengdanwei,yuanxisuo,zhuanye,xuexifangshi,yanjiufangxiang,num))
        print('执行成功！')
    except:
        pass



if __name__ == "__main__":
    try:
        cursor.execute("select * from school_name")#从数据库查询学校名称
        name = cursor.fetchone()                   #游标提取一条记录
        while name != None:
            school_name = str(name).split('\'')[1]        #提取学校名称
            #print(school_name)
            school_names.append(school_name)
            name = cursor.fetchone()
    
        cursor.execute("select * from major_number")#获取专业代码
        number = cursor.fetchone()
        while number != None:
            number = str(number).split('\'')[1]
            #print(number)
            numbers.append(number)
            number = cursor.fetchone()

        for s_item in school_names:
            for n_item in numbers:
                try:
                    res = requests.get(get_school_url(s_item, n_item), headers = headers)
                    soup = BeautifulSoup(res.text,'lxml')
                    infos = soup.select('body > div.main-wrapper > div.container.clearfix > div > div.zsml-list-box > table > tbody > tr > td:nth-child(8) > a')
                    for info in infos:
                        new_url = 'https://yz.chsi.com.cn/' + info.get("href")
                        get_Major_Page(new_url)
                    time.sleep(1)
                except:
                    pass
            conn.commit()
            print('提交数据库成功！')
    except:
        pass
    conn.close()
      