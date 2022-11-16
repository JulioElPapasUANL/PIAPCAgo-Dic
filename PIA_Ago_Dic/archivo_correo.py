import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.multipart import MIMEBase
from email import encoders


msg = MIMEMultipart()
msg['Subject'] = 'Correo con imagen Adjunta'
msg['From'] = 'jalcytestpias@gmail.com'
msg['To'] = 'julioadrianlanderos@gmail.com'

text = MIMEText("test")
msg.attach(text)

# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open('test.txt', 'rb')
 
# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" 'archivo de texto')
# Y finalmente lo agregamos al mensaje
msg.attach(adjunto_MIME)

try:
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login('jalcytestpias@gmail.com', 'eogomjrkwyrepfsx')
    mailServer.sendmail('jalcytestpias@gmail.com', 'hass20102010@hotmail.com', msg.as_string())
    mailServer.quit()
except Exception:
        print('no está conectado a una red wifi con internet')
else:    
    print('screenshot enviada con exito')