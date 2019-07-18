from email.header import Header
from email.mime.text import  MIMEText
import smtplib
def sendEmailText():
    smtpserver="smtp.163.com"
    account="zouxudongatcd@163.com"
    psw="qvbvjai1989"#input("input account psw:")
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

sendEmailText()