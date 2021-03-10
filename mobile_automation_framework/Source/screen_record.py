#To connect adb device to perform screen record store in device and pull to our system one copy
import time,subprocess,os
def screen_rec(cmd_list,s_path_filename,d_path_filename,d_filename):
    b_res=subprocess.getoutput(cmd_list[0])
    lines=b_res.split('\n')
    try:
        for line in lines:
            if not line.endswith('device'):
                raise Exception ('device not found')
    except:
        s_cmd=cmd_list[1]+s_path_filename
        s_record=subprocess.getoutput(s_cmd)#store in adb device 
        time.sleep(15)
        p_cmd=cmd_list[2]+s_path_filename+' '+d_path_filename
        s_pull=subprocess.getoutput(p_cmd)#pull to system
        mp4_feach=os.walk('D:\\')
        for root,dirs,files in mp4_feach:
            for file in files:
                try:
                    if file==d_filename:
                        return True
                except:
                    raise Exception('file not found')
            
if __name__=='__main__':
    cmd_list=['adb devices','adb shell screenrecord ','adb pull ']
    s_path_filename='//sdcard//s_record.mp4 '
    d_path_filename='D:\\adb_fastboot\\d_record.mp4'
    d_filename="d_record.mp4"
    print(screen_rec(cmd_list,s_path_filename,d_path_filename,d_filename))
