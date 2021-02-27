import subprocess
import os
def run_adb(cmd_list):
    res=None
    try:
        res = subprocess.check_output(cmd)
        res = res.decode('utf-8')
    except Exception as e:
        print("Error : {}".format(str(e)))
    return res
#cmd='adb uninstall C:\Andriod\platform-tools\cal.apk'
#cmd='adb uninstall C:\Andriod\platform-tools\python_sample_mobile_app.apk'
#res=run_adb(cmd)
#res=run_adb(cmd)
#print(res)
#print(res)
#cmd='adb shell pm list packages -3'
#res=run_adb(cmd)
#print(res)
cmd='adb uninstall innovationlabs.python.com'
res1=run_adb(cmd)
print(res1)
cmd='adb uninstall com.bak.mnr.calculatrice'
res2=run_adb(cmd)
print(res2)



