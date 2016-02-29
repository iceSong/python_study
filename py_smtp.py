# -*- coding:utf-8 -*-
# SMTP发送邮件 Python对SMTP支持有smtplib和email两个模块，
# email负责构造邮件，smtplib负责发送邮件。
from email.mime.text import MIMEText
msg = MIMEText('hello, send py Python……', 'plain', 'utf-8')
from_addr = input('Frome:')
passwd = input('Passwd:')
to_addr = input('To:')
smtp_server = input('SMTP server:')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()