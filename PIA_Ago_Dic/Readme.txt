Este script tiene como objetivo brindar herramientas de seguridad comunes para los usuarios

funciona de la siguiente manera:

El script principal es main.py, el cual debe ser ejecutado desde cmd para su correcto funcionamiento, por medio de parametros indicaremos que funciones son las que vamos a utilizar
por ejemplo si escribimos --screen o -s se ejecutara el script de enviar capturas de pantalla por correo, de igual manera los demas scripts tienen sus argumentos, cada script esta establecido
en funciones por lo que no es necesario pasarle argumentos al momento de invocar la funcion, los parametros que necesiten ser ingresados por el usuario se pediran una vez se ejecute,
la unica excepcion es el script de nmap, en el cual si se le necesitan establecer argumentos.

funcionamiento del script nmap:
Este unico script es el que se le tienen que establecer parametros a la hora de mandar a llamar la funcion los cuales seran pedidos si se quiere llamar al script.
el funcionamiento de este es sencillo, se escanean los puertos de un rango de puertos que nosotros ingresemos de la ip dada, para validar que los puertos y la ip son correctos
se usan expresiones regulares, una vez confirmados se inicia el escaneo

Funcionamiento cifrado:
Se cifra un mensaje ingresado por el usuario, dicho mensaje se guarda en un txt en la misma carpeta que se encuentra el script, si se quiere desencriptar se recupera el archivo guardado
lo que contiene el txt se guarda en una variable y se desencripta, imprimiendo el mensaje

Funcionamiento screenshots:
Usando la libreria de smtplib y mime para el formato asi como el envio de protocolo smtp y pyautogui para el tomado de screenshots.
Se toman capturas de pantalla las cuales se mandan por correo a una direccion de correo prestablecidas por nosotros,abriendo la imagen y leeyendola
dando formato como ya se menciono con mime y adjuntandola para mandarla, se hace la conexion, se conecta a la cuenta y luego ya hecho el ingreso se manda el correo

funcionamiento de script en powershell:
Mediante comandos de cmd se crea una carpeta en la unidad de almacenamiento en la cual por medio de mas comandos se obtiene informacion de la bios, datos del host
asi como tambien datos de ip y por ultimo la dns del equipo. cada una de estas informaciones se guarda en un txt con su respectiva informacion.
Este script va de la mano con otro en el cual funciona igual que el envio de screenshots a excepcion de que aqui se envian los 4 archivos.

funcionamiento de virustotal:
Virus total es una api que puede escanear archivos, dominios y hashes para saber si son maliciosos o no, en nuestro caso le dimos una lista de urls alimentadose desde un csv, cuando escanea
las direcciones las separa en archivos txt diferentes, maliciosos, no maliciosos y no encontrados.
