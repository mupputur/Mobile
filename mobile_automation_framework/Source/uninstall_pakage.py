#uninstall app or application in the device using adb command line
import subprocess

def m_uninstall_pak(pkg_name):
    cmd='adb uninstall'+' '+ pkg_name
    res = subprocess.getoutput(cmd)
    if res.split()[-1]=='Success':
        return True
    else:
        raise Exception("Please provide valid pakage name")

if __name__=="__main__":
    pkg_name='com.bak.mnr.calculatrice'
    print(m_uninstall_pak(pkg_name))
        
    




