import requests
from bs4 import BeautifulSoup
import pymysql

con = pymysql.connect(host = 'localhost', user = 'root', passwd = 'Lin_1772815', db = 'biyesheji', port = 3306, charset = 'utf8') 
cursor = con.cursor()

headers = {
    'User-Agent': 
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}




def get_words(url,n):
    res = requests.get(url, headers = headers)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text,'lxml')
    words = soup.select('body > div.catalog_wrap > div.abstract_body'\
        ' > div.abstract_body_content > p')
    if n == 1:
        for word in words:
            word = word.get_text().strip()
            cursor.execute("insert into instructions1(inst) values(%s)", word)
    elif n == 2:
        for word in words:
            word = word.get_text().strip()
            cursor.execute("insert into instructions2(inst) values(%s)", word)
    elif n == 3:
        for word in words:
            word = word.get_text().strip()
            cursor.execute("insert into instructions3(inst) values(%s)", word)
    elif n == 4:
        for word in words:
            word = word.get_text().strip()
            cursor.execute("insert into instructions4(inst) values(%s)", word)
    else:
        for word in words:
            word = word.get_text().strip()
            cursor.execute("insert into instructions5(inst) values(%s)", word)
def get_append(url):
    res = requests.get(url, headers = headers)
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, 'lxml')
    wds = soup.select('body > div.catalog_wrap > div.abstract_body > div.abstract_body_content > p')
    for wd in wds:
        wd = wd.get_text().strip()
        cursor.execute("insert into instructions5(inst) values(%s)", wd)

root = 'E:\Graduate_design2020\imgs\\'
def save_img(url, name):
    res = requests.get(url, headers = headers)
    path = root + name
    with open(path,'wb') as f:
        f.write(res.content)
        f.close()
        print("保存成功！")


        
def getPicture(url):
    res = requests.get(url,headers = headers)
    soup = BeautifulSoup(res.text,'lxml')
    pictures = soup.select('body > div.catalog_wrap > div.abstract_body '\
    '> div.abstract_body_content > div > img')'
    for picture in pictures:
        name = str(picture.get("src")).split('/')[1]
        print(name)
        link = 'https://www.eol.cn/e_ky/zt/report/2020/' + picture.get("src")
        print(link)
        save_img(link,name)

def get_pic_app(url):
    res = requests.get(url, headers = headers)
    soup = BeautifulSoup(res.text, 'lxml')
    pictures = soup.select('body > div.catalog_wrap > div.abstract_body > div.abstract_body_content > div > img')
    for picture in pictures:
        name = str(picture.get("src"))
        print(name)
        link = 'https://www.eol.cn/e_ky/zt/report/2020/' + picture.get("src")
        print(link)
        save_img(link,name)

    
if __name__ == "__main__":
    '''
    urls = ['https://www.eol.cn/e_ky/zt/report/2020/content0{}.html'.format(str(i)) for i in range(1,5)]
    n = 1
    for url in urls:
        get_words(url, n)
        n += 1
    
    url = 'https://www.eol.cn/e_ky/zt/report/2020/appendix.html'
    get_append(url)
    con.commit()
    con.close()
    '''

    
    urls = ['https://www.eol.cn/e_ky/zt/report/2020/content0{}.html'.format(str(i)) for i in range(1,5)]
    for url in urls:
        getPicture(url)
    
    url = 'https://www.eol.cn/e_ky/zt/report/2020/appendix.html'
    get_pic_app(url)
    