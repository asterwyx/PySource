# email module for forming mail
import email
# smtp module for sending email
import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(Header(name, 'utf-8'), addr)


from_addr = input("From:")
passwd = input("Password:")
# receiver address
to_addr = input("To:")
smtp_server = input("SMTP server:")

msg = MIMEText("Hello, send by python...", 'plain', 'utf-8')
msg['From'] = _format_addr('Cecil <%s>' % from_addr)
msg['To'] = _format_addr('Administrator <%s>' % to_addr)
msg['Subject'] = Header('greeting...', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, passwd)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
