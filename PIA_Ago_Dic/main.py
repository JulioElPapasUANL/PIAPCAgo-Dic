from screenshot_correo import *
from VirusTotal import *
from nmapi import *
from sub import *
from piec import *
from Cifr import *

import argparse, logging, time

logging.basicConfig(filename="historialMain.log",level=logging.INFO, format="%(levelname)s:%(asctime)s:%(message)s")

parser = argparse.ArgumentParser(description="***Se muestran los comandos necesarios para ejecutar las herramientas de CiberSeguridad***")

#Encriptado por base64
parser.add_argument("-b64e", "--encriptar", help="encriptado por base 64 \n", action="store_true")
parser.add_argument("-b64d", "--desencriptar", help="desencriptado por base 64 \n", action="store_true")

#Screenshot y que se mande por correo
parser.add_argument("-sc", "--screen", help="Envio de Screenshot por correo \n", action="store_true")

#Ejecusion de script de powershell
parser.add_argument("-ps", "--powershell", help="ejecucion de script con insturcciones para powershell y generar un reporte en un archivo de texto \n", action="store_true")

#Escaneo basico de dominios con la api virus total
parser.add_argument("-vt", "--virustotal", help="insertar url de dominios en el arachivo urls.csv para poder ejecutar este \n", action="store_true")

#escaneo de puertos de una ip ingresada
parser.add_argument("-nmap", "--escaneo", help="ingrese la ip y el puerto para hacer un escaneo en un rango \n", action="store_true")

parser = parser.parse_args()

#Opciones
if __name__=="__main__":

    if parser.screen:
        logging.info("Tomando screenshot ")
        print("Tomando screenshot...")
        SsCorreo()
        logging.info('Fin del proceso')
    
    elif parser.encriptar:
        logging.info("enctiptando")
        encript()
        logging.info('Fin del proceso')

    elif parser.desencriptar:
        logging.info("desenctiptando")
        decript()
        logging.info('Fin del proceso')

    elif parser.virustotal:
        logging.info("analizando urls...")
        VirusTotal()
        logging.info('Fin del proceso')

    elif parser.escaneo:
        ip = input('ingrese la direccion ip: ')
        puertos = input("Ingrese el rango de puertos con formato 0-100 (un numero, seguido de un guion, seguido de otro numero)\n")
        logging.info("inicio de escaneo de puertos")
        escaneo(ip,puertos)
        logging.info('Fin del proceso')

    elif parser.powershell:
        logging.info("inicio de script powershell")
        inf()
        time.sleep(2)
        envinf()
        logging.info('Fin del proceso')
