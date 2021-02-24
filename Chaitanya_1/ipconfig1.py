import subprocess
proc = subprocess.check_output("ipconfig" ).decode('utf-8')
print (proc)
