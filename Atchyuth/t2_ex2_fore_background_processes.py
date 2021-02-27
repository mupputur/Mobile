#get foreground process and background process

#task manager 
import subprocess
cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
for line in proc.stdout:
    if b'Program' in line:
        print(line)

#background process
import os, time, sys, subprocess
if len(sys.argv) == 2:
    time.sleep(5)
    print ('track end')
    if sys.platform == 'darwin':
        subprocess.Popen(['say', 'hello'])
else:
    print ('main begin')
    subprocess.Popen(['python', os.path.realpath(__file__), '0'], close_fds=True)
    print ('main end')
