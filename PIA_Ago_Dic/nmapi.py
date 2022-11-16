import nmap
import re

def escaneo(ipingr,puertos):
 #Expresion regular para validar ip
 ip_patron= re.compile("^(?:[0-9]{1,3}.){3}[0-9]{1,3}$")
 #expresion regular para validar el rango de puertos
 patron_rangopts = re.compile("([0-9]+)-([0-9]+)")

 ptomin = 0
 ptomax = 65535

 open_ports = []
 #Validacion de ip
 while True:
     ip_ingresada = ipingr
     if ip_patron.search(ip_ingresada):
        print(f"{ip_ingresada} es una direccion valida")
     else:
        print("la direccione es invalida")
        break
 #Validacion de puertos
 while True:
    rangopts = puertos
    rangoptsv = patron_rangopts.search(rangopts.replace(" ",""))
    if rangoptsv:
        ptomin = int(rangoptsv.group(1))
        ptomax = int(rangoptsv.group(2))
    else:
        print("el rango de puertos es invalido")
        break

 nm = nmap.PortScanner()
 #escaneo
 for puerto in range(ptomin, ptomax + 1):
    try:
        result = nm.scan(ip_ingresada, str(puerto))
        port_status = (result['scan'][ip_ingresada]['tcp'][puerto]['state'])
        print(f"el estado del puerto {puerto} es: {port_status}")
    except:
        print(f"No fue posible escanear el puerto {puerto}.")