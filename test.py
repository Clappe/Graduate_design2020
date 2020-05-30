#print("This is my graduate design.")
from flask import Flask, render_template, request
import pymysql
from flask_sqlalchemy import SQLAlchemy
import time
'''
app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello World!'

if __name__ == "__main__":
    app.run(debug = True)
'''


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:'\
    'Lin_1772815@localhost:3306/biyesheji?charset=utf8'
db = SQLAlchemy(app)
db.init_app(app)
db.create_all()

class informations(db.Model):
    __tablename__ = 'infos'
    id = db.Column(db.Integer, primary_key = True)
    zhaoshengdanwei = db.Column(db.String(100))
    yuanxisuo = db.Column(db.String(100))
    zhuanye = db.Column(db.String(100))
    xuexifangshi = db.Column(db.String(100))
    yanjiufangxiang = db.Column(db.String(100))
    num = db.Column(db.String(4))
     
    def __init__(self,id,zhaoshengdanwei,yuanxisuo,zhuanye,xuexifangshi,yanjiufangxiang,num):
        self.id = id
        self.zhaoshengdanwei = zhaoshengdanwei
        self.yuanxisuo = yuanxisuo
        self.zhuanye = zhuanye
        self.yanjiufangxiang = yanjiufangxiang
        self.num = num
        self.location = location

if __name__ == "__main__":
    start = time.time()
    infs = informations.query.filter_by(zhaoshengdanwei = '北京大学').all()
    for item in infs:
        print(item)
    end = time.time()
    t = end - start
    print(t)
