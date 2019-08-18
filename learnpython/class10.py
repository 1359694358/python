'''
review：面向对象编程：class,实例
        self ：实例化本身
        init：特殊的类方法；
        类变量，实例变量
        私有属性，私有变量
        继承：当我们定义一个新的class的时候，可以从某个现有的class继承，新的class称为子类，而被继承的类称为基类(object)，父类，超类
              代码的重用
        class 类名(继承的类名):
        R如果子类和父类有相同的方法，会执行子类方法
'''


class Parent():
    '''现有的class'''
    x=100
    def __init__(self):
        print('这是父类的init方法')

    def parent_methon(self):
        print('这是父类的普通方法')


class Child(Parent):
    def __init__(self):
        print('这是子类的init方法')

    def child_methon(self):
        print('这是子类的普通方法')

#实例化对象
# A=Child()
# print(A.x)  #调用父类的类变量
# A.parent_methon()
#
# import unittest
# class Test(unittest.TestCase):
#     def test(self):
#         self.assertEqual()

'''继承多个类:C继承了A和B'''

# class A:
#     pass
# class B:
#     pass
# class C(A,B):
#     pass
#

'''例四：邮件内容包含附件，这里讲一种，附件为html测试报告；需要导入email模块中的MIMEMultipart()类
带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，
	1.可以构造一个MIMEMultipart对象代表邮件本身，然后往里面加上一个MIMEText作为邮件正文，
	2.再继续往里面加上表示附件的
	
	
	python字符串前面加u,r,b的含义
2017年12月02日 16:57:54 夕晟 阅读数 387更多
个人分类： python
u/U:表示unicode字符串 
不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。 
一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。 
建议所有编码方式采用utf8

r/R:非转义的原始字符串 
与普通字符相比，其他相对特殊的字符，其中可能包含转义字符，即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。而如果是以r开头，那么说明后面的字符，都是普通的字符了，即如果是“\n”那么表示一个反斜杠字符，一个字母n，而不是表示换行了。 
以r开头的字符，常用于正则表达式，对应着re模块。

b:bytes 
python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes 
python2.x里, b前缀没什么具体意义， 只是为了兼容python3.x的这种写法
'''
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart
def send_email_attch():
    '''发送纯文本邮件,在第二步声明一下发件人和收件人的主题'''
    #第一步：创建账号数据
    smtpserver='smtp.163.com'       #发送，邮件服务器
    sender ='15902127953@163.com'   #发送人账号
    password='test123456'           #发送人的密码
    revicer='15902127953@163.com'   #接收人

    # #第二步：构建邮件内容，MIMEText构造
    # content=MIMEText('我是Harvey老师，第一次用python发邮件','plain','utf-8')
    # content['From']=Header(sender,'utf-8')
    # content['To']=revicer
    # content['Subject']=Header("主题是自动化测试",'utf-8')

    #第二步：实例化MIMEMultipart对象，attch增加俩部分：邮件的正文,增加附件
    data=MIMEMultipart()
    data.attach(MIMEText('hello','plain','utf-8'))
    data['from']=Header(sender,'utf-8')
    data['To']=revicer
    data['Subject']=Header("主题是自动化测试",'utf-8')

    '''增加附件'''
    at=MIMEText(open(r'C:\Users\Administrator\PycharmProjects\classnote\firsthtml.html',encoding='utf-8').read())

    at['Content-Disposition']='attachment; filename="report.html"' #
    data.attach(at)

    #第三步：邮件的发送过程，smtplib
    serve=smtplib.SMTP(smtpserver,25)   #邮件服务器，和端口
    serve.login(sender,password)        #先登录邮件服务器，
    #serve.set_debuglevel(1)             #查看日志
    serve.sendmail(sender,revicer,data.as_string()) #1.发送人，2接收人 ，3将构建内容转换成字符串
    serve.quit()  #退出邮箱

#send_email_attch()
'''网易发送给qq'''
def send_email():
    '''发送纯文本邮件,在第二步声明一下发件人和收件人的主题'''
    #第一步：创建账号数据
    smtpserver='smtp.163.com'       #发送，邮件服务器  smtp.qq.com
    sender ='15902127953@163.com'   #发送人账号
    password='test123456'           #发送人的密码
    revicer='2595295841@qq.com'   #接收人

    #第二步：构建邮件内容，MIMEText构造
    content=MIMEText('我是Harvey老师，第一次用python发邮件','plain','utf-8')
    content['From']=Header(sender,'utf-8')
    content['To']=revicer
    content['Subject']=Header("主题是自动化测试",'utf-8')

    #第三步：邮件的发送过程，smtplib
    serve=smtplib.SMTP(smtpserver,25)   #邮件服务器，和端口
    serve.login(sender,password)        #先登录邮件服务器，
    #serve.set_debuglevel(1)             #查看日志
    serve.sendmail(sender,revicer,content.as_string()) #1.发送人，2接收人 ，3将构建内容转换成字符串
    serve.quit()  #退出邮箱

# send_email()

'''python操作mysql数据库
pymyql
'''
import  pymysql
#连接数据库
#con=pymysql.connect(host='localhost',user='root',password='test123456',database='test',)
#con=pymysql.connect('localhost','root','test123456','test')
#print(con)

'''char:定长，效率高 
   varchar（20）：存放20个数字、字母、或者汉子
   '''
#创建一个表:
#cursor方法获取游标
#execute执行sql语句
# cur=con.cursor()
# cur.execute('create table test1(id varchar(20) primary  key ,name char(10) )')

#插入数据
# cur=con.cursor()
# cur.execute('insert into test1 values (4,"小六")')
# con.commit() #提交 不是用游标去提交
#
#查询
#fetchone ()获取一条数据
#fetchall() 获取所有的数据
# cur=con.cursor()
# cur.execute('select * from test1 where id=3')
# result_one=cur.fetchone()
# print(result_one)
# result_all=cur.fetchall()
# print(result_all,type(result_all))
# print(result_all[0][1])

#关闭数据库
#con.close()


def  connet():
    '''连接数据库'''
    db = pymysql.connect(host='localhost', user='root', password='test123456', database='test', )
    return  db

def creat_table(db):
    '''创建表作者'''
    cur=db.cursor()
    sql='''create table authors(author_id char(20) primary  key ,author_name varchar(50) )'''
    cur.execute(sql)

def creat_table_book(db):
    '''创建书籍表'''
    cur=db.cursor()
    sql='''create table books(books_id char(20) primary  key ,author_id char(20),books_name varchar (50) )'''
    cur.execute(sql)

def creat_table_order(db):
    '''创建订单表'''
    cur=db.cursor()
    sql='''create table orders(order_id char(20) primary  key ,book_id char(20),price varchar (50) )'''
    cur.execute(sql)


def insert_data(db):
    '''插入数据'''
    cur=db.cursor()
    sql='''insert into authors values (1,"A"),(2,'B'),(3,'c')'''
    cur.execute(sql)
    db.commit()


def  query(db):
    '''查询数据库SELECT `authors`.*,books.books_name FROM `authors` LEFT JOIN books  on `authors`.author_id=books.author_id'''
    cur=db.cursor()
    #俩个表关联
    #sql='''SELECT `authors`.*,books.books_name FROM `authors` LEFT JOIN books  on `authors`.author_id=books.author_id'''
    #三个表关联
    sql="""SELECT `authors`.*,books.books_name,orders.price FROM `authors` LEFT JOIN books  on `authors`.author_id=books.author_id  LEFT JOIN orders  on books.books_id=orders.book_id"""
    cur.execute(sql)
    result=cur.fetchall()
    for i in result:
        print(i)
def close_db(db):
    db.close()


def main():
    '''主方法：执行顺序'''
    db=connet()
    #creat_table(db)
    #creat_table_book(db)
    #creat_table_order(db)
    #insert_data(db)
    query(db)
    close_db(db)
main()


'''写一个操作数据库的类'''


