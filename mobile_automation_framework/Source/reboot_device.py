#reboot the connected device through adb
import time,subprocess

def reboot_dev(cmd_list):
    before_res=subprocess.getoutput(cmd_list[0])
    #res=res.decode('utf-8')
    res=subprocess.getoutput(cmd_list[1])
    time.sleep(45)
    after_res=subprocess.getoutput(cmd_list[0])
    if before_res == after_res:
        return True
    else:
        return False

if __name__=='__main__':
    cmd_list=['adb devices','adb reboot']
    print(reboot_dev(cmd_list))
    
    
