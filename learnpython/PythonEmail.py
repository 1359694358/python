import smtplib
from email.header import Header
from email.mime.text import  MIMEText

class PythonEmail:
    _163='163'
    SINA='SINA'
    QQ='QQ'
    SMTP_QQ='smtp.qq.com'
    SMTP_163='smtp.163.com'
    SMTP_SINA='smtp.sina.com'

    server=None
    account=None
    account=None
    content=None
    psw=None
    subjectTitle,emailContent=None,None
    reciver,mailType=None,None
    def __init__(self,account,psw,reciver,subjectTitle,emailContent,mailType):
        self.account=account
        self.psw=psw
        self.reciver=reciver
        self.subjectTitle=subjectTitle
        self.mailType=mailType
        self.emailContent=emailContent
    def send(self):
        self.content = MIMEText(self.emailContent)
        server=PythonEmail.GetSmtpServer(self.mailType)
        self.server = smtplib.SMTP(server, 25)
        self.server.login(self.account, self.psw)
        self.content['Subject'] = Header(self.subjectTitle, 'utf-8')
        self.content['From'] = self.account
        self.content['To'] = self.reciver
        self.server.sendmail(self.account, self.reciver, self.content.as_string())
        self.server.quit()

    @staticmethod
    def GetSmtpServer(emailType):
        '''
        获取smtp服务器
        :param emailType: 163  sina  qq
        :return:
        '''
        if emailType==PythonEmail._163:
            return PythonEmail.SMTP_163
        elif str(emailType).upper()==PythonEmail.QQ:
            return PythonEmail.SMTP_QQ
        elif str(emailType).upper()==PythonEmail.QQ:
            return PythonEmail.SMTP_SINA
