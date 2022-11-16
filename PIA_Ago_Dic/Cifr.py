import base64

def encript():
    emsg=input("Escriba el mensaje que quiere encriptar: ")
    with open("Cifr.txt", "wb") as fh:
     fh.write(base64.b64encode(bytes(emsg, 'utf-8')))
def decript():
    with open ("Cifr.txt","r") as fh:
     msgr= fh.read().replace('\n','')
     msgd =base64.urlsafe_b64decode(msgr) 
     print(msgd)
