from email.header import Header
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib

from PythonEmail import PythonEmail


def sendEmailText():
    smtpserver="smtp.163.com"
    account="zouxudongatcd@163.com"
    psw=input("input account psw:")
    reciver="15902127953@163.com"
    content=MIMEText("我是烧饼哥 跟着你写")
    server=smtplib.SMTP(smtpserver,25)
    server.login(account,psw)
    content['Subject'] = Header("我是烧饼哥", 'utf-8')
    content['From'] = account
    content['To'] = reciver
    server.sendmail(account,reciver,content.as_string())
    server.quit()
    pass

# sendEmailText()

def sendEmailHTMLByMulipart():
    smtpserver = "smtp.163.com"
    account = "zouxudongatcd@163.com"
    psw = input("input account psw:")
    reciver = "1359694358@qq.com"
    # htmlfile = open("./baidu.html", "r+")
    # result = htmlfile.readlines()
    # htmlData = ""
    # for itemStr in result:
    #     htmlData = htmlData + itemStr
    content = MIMEMultipart()
    content.attach(MIMEText("email  muilpart","plain",'utf-8'))
    content.attach(MIMEText(open(r".\baidu.html",encoding='utf-8').read()))

    server = smtplib.SMTP(smtpserver, 25)
    server.login(account, psw)
    content['Subject'] = Header("我是烧饼哥HTML", 'utf-8')
    content['From'] = account
    content['To'] = reciver
    content['Content -Disposition']="attachment:filename='baidu.html'"
    server.sendmail(account, reciver, content.as_string())
    server.quit()
    pass


sendEmailHTMLByMulipart()
def sendEmailHTML():
    smtpserver = "smtp.163.com"
    account = "zouxudongatcd@163.com"
    psw = input("input account psw:")
    reciver = "1359694358@qq.com"
    htmlfile = open("./baidu.html", "r+")
    result = htmlfile.readlines()
    htmlData = ""
    for itemStr in result:
        htmlData = htmlData + itemStr
    content = MIMEText(htmlData,"HTML")
    server = smtplib.SMTP(smtpserver, 25)
    server.login(account, psw)
    content['Subject'] = Header("我是烧饼哥HTML", 'utf-8')
    content['From'] = account
    content['To'] = reciver
    server.sendmail(account, reciver, content.as_string())
    server.quit()
    pass

# sendEmailHTML()
# emailSend=PythonEmail(account='zouxudongatcd@163.com',psw='qvbvjai1989',reciver='1359694358@qq.com',subjectTitle='from python send email',emailContent='this is a test',mailType=PythonEmail._163)
# emailSend.send()

