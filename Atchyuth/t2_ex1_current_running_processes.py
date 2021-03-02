#List all currently running processes
import psutil
import os
def cur_run_processes():
    pro_str=''
    for process in psutil.process_iter():
        pro_name=process.name()
        Id=process.pid
        process=str(Id)+' '+pro_name
        pro_str=pro_str+'  '+process
    fobj=open(path,'w')
    pro_file=fobj.write(pro_str)
    fobj.close()
    gen_files=os.walk('D:\\')
    for root,folders,files in gen_files:
        for file in files:
            if file.endswith('.txt')and file.startswith('cur_'):
                return True
    else:
        return "File not available"
if __name__=="__main__":
    path='D:\\Practice_ex\\Practice_real\\cur_running_processes.txt'
    print(cur_run_processes())

