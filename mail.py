#!/usr/bin/env python 
#coding:utf-8 
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys 
 
#邮箱smtp服务器地址
mail_host = 'smtp.xxx.com'
#邮箱用户名
mail_user = 'xxx@xxx.com'
#邮箱密码
mail_pass = 'xxx'
#邮箱地址后缀
mail_postfix = 'xxx.com'
 
def send_mail(to_list,subject,content):
    me = mail_user+"<"+mail_user+"@"+mail_postfix+">"
    msg = MIMEText(content,'plain','utf-8')
    msg['Subject'] = Header(subject,'utf-8')
    msg['From'] = me
    msg['to'] = to_list 
 
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False
 
if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
