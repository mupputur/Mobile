import time,subprocess

def reboot_device(cmd_list):
    b_res=subprocess.getoutput(cmd_list[0])
    #res=res.decode('utf-8')
    res=subprocess.getoutput(cmd_list[1])
    time.sleep(45)
    a_res=subprocess.getoutput(cmd_list[0])
    if b_res == a_res:
        return True
    else:
        return False

if __name__=='__main__':
    cmd_list=['adb devices','adb reboot']
    print(reboot_device(cmd_list))
    
    
