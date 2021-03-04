import os
import subprocess
def install_apk(apk_path):
    try:
        apk=apk_path.endswith(".apk")
        if apk==True:
            pass
        else:
            raise Exception
    except Exception:
          return "Please provide .apk file extention"
    cmd='adb install'+' '+ apk_path
    res = subprocess.getoutput(cmd)
    if res.split()[-1]=='Success':
        return True
    else:
        return False
if __name__=="__main__":
    path='C:\\Andriod\\platform-tools\\cal.apk'
    print(install_apk(path))
    
    
        
    
        


        
