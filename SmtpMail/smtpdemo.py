# -*- coding: utf-8 -*-
__author__ = 'boqingfu'

import smtplib
from email.mime.text import MIMEText

mailto_list = ["florije1988@gmail.com"]
mail_host = "smtp.XXX.com"  #设置服务器
mail_user = "XXXX"  #用户名
mail_pass = "XXXXXX"  #口令
mail_postfix = "XXX.com"  #发件箱的后缀


def send_mail(to_list, sub, content):
    me = "hello" + "<" + mail_user + "@" + mail_postfix + ">"
    msg = MIMEText(content, _subtype='plain', _charset='gb2312')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user, mail_pass)
        server.sendmail(me, to_list, msg.as_string())
        server.close()
        return True
    except Exception, e:
        print str(e)
        return False


if __name__ == '__main__':
    if send_mail(mailto_list, "hello", "hello world！"):
        print "发送成功"
    else:
        print "发送失败"