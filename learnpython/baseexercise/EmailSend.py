from email.header import Header
from email.mime.text import  MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


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
    reciver = "1059315239@qq.com"
    # htmlfile = open("./baidu.html", "r+")
    # result = htmlfile.readlines()
    # htmlData = ""
    # for itemStr in result:
    #     htmlData = htmlData + itemStr
    content = MIMEMultipart()
    content.attach(MIMEText("小星星  收到了么","plain",'utf-8'))
    htmldata=open("./baidu.html",encoding='utf-8').read()
    print(type(htmldata))
    appendix=MIMEText(htmldata)
    appendix['Content-Disposition']='attachment; filename="baidu.html"'

    content.attach(appendix)

    server = smtplib.SMTP(smtpserver, 25)
    server.login(account, psw)
    content['Subject'] = Header("我是烧饼哥HTML", 'utf-8')
    content['From'] = account
    content['To'] = reciver
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

