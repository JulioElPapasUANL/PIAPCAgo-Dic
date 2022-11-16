import subprocess, sys    
def inf():
 p = subprocess.Popen('powershell.exe -ExecutionPolicy unrestricted -file "EPC.ps1"', stdout=sys.stdout)
 p.communicate()