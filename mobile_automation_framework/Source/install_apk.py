#Install .apk file into connected adb device 
import subprocess

def m_install_apk(apk_file_path):
    if apk_file_path.endswith('.apk'):
        cmd='adb install'+' '+ apk_file_path
        res = subprocess.getoutput(cmd)
        if res.split()[-1]=='Success':
            return True
        else:
            return False
    else:
        raise Exception("Please provide .apk file")

if __name__=="__main__":
    apk_file_path='C:\\Andriod\\platform-tools\\cal.apk'
    print(m_install_apk(apk_file_path))
    
    
    
        
    
        


        
