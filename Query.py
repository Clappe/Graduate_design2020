from flask import Flask, render_template, request
import pymysql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from sqlalchemy.sql import func


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

class adjust(db.Model):
    __tablename__ = 'to_adjust'
    college = db.Column(db.String(50))
    major = db.Column(db.String(50))
    num = db.Column(db.String(3))
    id = db.Column(db.Integer, primary_key = True)
    def __init__(self, college, major, num):
        self.college = college
        self.major = major
        self.num = num

class instructs1(db.Model):
    __tablename__ = 'instructions1'
    id = db.Column(db.Integer, primary_key = True)
    inst = db.Column(db.String(300))
    def __init__(self,id,inst):
        self.id = id
        self.inst = inst

class instructs2(db.Model):
    __tablename__ = 'instructions2'
    id = db.Column(db.Integer, primary_key = True)
    inst = db.Column(db.String(300))
    def __init__(self,id,inst):
        self.id = id
        self.inst = inst

class instructs3(db.Model):
    __tablename__ = 'instructions3'
    id = db.Column(db.Integer, primary_key = True)
    inst = db.Column(db.String(300))
    def __init__(self,id,inst):
        self.id = id
        self.inst = inst

class instructs4(db.Model):
    __tablename__ = 'instructions4'
    id = db.Column(db.Integer, primary_key = True)
    inst = db.Column(db.String(300))
    def __init__(self,id,inst):
        self.id = id
        self.inst = inst
class instructs5(db.Model):
    __tablename__ = 'instructions5'
    id = db.Column(db.Integer, primary_key = True)
    inst = db.Column(db.String(500))
    def __init__(self,id,inst):
        self.id = id
        self.inst = inst

'''
con = pymysql.connect(host = 'localhost', user = 'root', passwd = 'Lin_1772815', db = 'biyesheji', port = 3306, charset = 'utf8')
cursor = con.cursor()
'''

@app.route('/home')
def Home_Page():
    return render_template('home.html')

@app.route('/query')
def query():
    return render_template('query_page.html')

@app.route('/zyxx',methods = ['POST','GET'])
def to_zyxx():
    if request.method == 'POST':
        univ = request.form['zsdw']
        major = request.form['zymc']
        stu_way = request.form['xxfs-sele']
        infs = informations.query.filter_by(
            zhaoshengdanwei = univ,xuexifangshi = stu_way).filter(
                informations.zhuanye.like("%"+major+"%")).all()
        return render_template('query_result.html',infos = infs)

@app.route('/to_adjust')
def to_adjust():
    return render_template('to_adjust.html')

@app.route('/adjust_result',methods = ['GET','POST'])
def adjust_result():
    if request.method == 'POST':
        col = request.form["tjxx"]
        mj = request.form["tjzy"]
        infs = adjust.query.filter_by(college = col).filter(adjust.major.like("%"+mj+"%")).all()
        return render_template('adjust_result.html',infs = infs)

@app.route('/predict')
def predict_page():
    return render_template('predict_page.html')

@app.route('/predict1')
def to_predict1():
    wds = instructs1.query.all()
    return render_template('predict1.html', wds = wds)

@app.route('/predict2')
def to_predict2():
    wds = instructs2.query.all()
    return render_template('predict2.html', wds = wds)

@app.route('/predict3')
def to_predict3():
    wds = instructs3.query.all()
    return render_template('predict3.html', wds = wds)

@app.route('/predict4')
def to_predict4():
    wds = instructs4.query.all()
    return render_template('predict4.html', wds = wds)

@app.route('/append')
def to_append():
    wds = instructs5.query.all()
    return render_template('append.html', wds = wds)

@app.route('/echarts')
def to_echarts():
    
    return render_template('echarts_test.html')
        
if __name__ == "__main__":
    app.run(debug = True)
    '''
    infs = db.session.query(informations.zhuanye,func.sum(informations.num)).group_by(informations.zhuanye).order_by(func.sum(informations.num).desc()).limit(5)
    for item in infs:
        print(item[0])
        print(item[1])

    '''