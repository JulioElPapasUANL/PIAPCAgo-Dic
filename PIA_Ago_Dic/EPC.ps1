#Creacion de ruta y archivo a guardar
New-Item C:\Info\ -type directory
New-Item c:\Info\dns.txt -type file
New-Item c:\Info\sbios.txt -type file
New-Item c:\Info\host.txt -type file
New-Item c:\Info\ip.txt -type file

#Obtencion de datos de la BIOS
Get-WmiObject -Class Win32_Bios | Format-List -Property * | Out-File c:\Info\sbios.txt

#Obteniendo datos de HOST
Get-Host | Out-File c:\Info\host.txt

#Consiguiendo datos de la IP
Get-NetIPConfiguration -detailed  | Out-File c:\Info\ip.txt

#Obtencion de dns del equipo
ipconfig /displaydns | Out-File c:\Info\dns.txt

