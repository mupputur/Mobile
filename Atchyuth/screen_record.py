import time,subprocess,os

def screen_record(cmd_list):
    b_res=subprocess.getoutput(cmd_list[0])
    lines=b_res.split('\n')
    try:
        for line in lines:
            if not line.endswith('device'):
                raise Exception ('device not found')
    except:
        s_cmd=cmd_list[1]+s_path
        s_record=subprocess.getoutput(s_cmd)
        time.sleep(30)
        p_cmd=cmd_list[2]+s_path+d_path
        s_pull=subprocess.getoutput(p_cmd)
        mp4_feach=os.walk('D:\\')
        for root,dirs,files in mp4_feach:
            for file in files:
                try:
                    if file==d_file:
                        return True
                        break
                except:
                    raise Exception('file not found')
            
if __name__=='__main__':
    cmd_list=['adb devices','adb shell screenrecord ','adb pull ']
    s_path='//sdcard//s_record.mp4 '
    d_path='D:\\adb_fastboot\\screen_record.mp4'
    d_file='screen_record.mp4'
    print(screen_record(cmd_list))
