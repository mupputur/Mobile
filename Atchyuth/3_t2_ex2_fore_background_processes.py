#get foreground processes and background processes
import os, time, sys, subprocess
def fore_pro():
    pro_str=''
    cmd = 'WMIC PROCESS get Caption,Commandline,Processid'
    #proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    res = subprocess.getoutput(cmd)
    pro_str+=res
    fobj=open(path,'w')
    pro_file=fobj.write(pro_str)
    fobj.close()
    gen_files=os.walk('D:\\')
    for root,folders,files in gen_files:
        for file in files:
            if file.endswith('.txt')and file.startswith('fore'):
                return True
    else:
        return "File not available"
#background process
def back_pro():
    if len(sys.argv) == 2:
        time.sleep(5)
        print ('track end')
        if sys.platform == 'darwin':
            subprocess.Popen(['say', 'hello'])
    else:
        print ('main begin')
        subprocess.Popen(['python', os.path.realpath(__file__), '0'], close_fds=True)
        print ('main end')
if __name__=="__main__":
    path='D:\\Practice_ex\\Practice_real\\foreground_processes.txt'
    print(fore_pro())
    print(back_pro())
    


    
