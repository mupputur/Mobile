import subprocess
import os
def uninstall_pakage(pkg_name):
    try:
        if pkg_name.startswith('com')or pkg_name.endswith('com'):
            pass
        else:
            raise Exception
    except Exception:
        return 'Please provide valid pakage'
    cmd='adb uninstall'+' '+ pkg_name
    res = subprocess.getoutput(cmd)
    if res.split()[-1]=='Success':
        return True
    else:
        return False
if __name__=="__main__":
    pkg_name='com.bak.mnr.calculatrice'
    print(uninstall_pakage(pkg_name))
    #innovationlabs.python.com
    
    




