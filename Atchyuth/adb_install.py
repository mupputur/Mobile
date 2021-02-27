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
cmd='adb install C:\Andriod\platform-tools\cal.apk'
cmd='adb install C:\Andriod\platform-tools\python_sample_mobile_app.apk'
res=run_adb(cmd)
res=run_adb(cmd)
print(res)
print(res)
"""
def path_apk():
    resp = os.walk("C:\")
    
    l_apks=[]
    for root,folder,files in resp:
        for f in files:
            if f.endswith('.apk'):
                
                l_apks.append(f)
        return l_apks
#apk=path_apk()
#print(apk)
def install_apk():
    a=run_adb('adb install C:\Andriod\platform-tools\cal.apk')
    b=run_adb('adb install C:\Andriod\platform-tools\python_sample_mobile_app.apk')
    return a,b
print(install_apk())
"""
    
