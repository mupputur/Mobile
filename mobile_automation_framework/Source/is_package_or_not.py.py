# find the given package available or not.

import subprocess

def is_package_or_not(pkg_name,cmd="-3"):
    cmd="adb shell pm list packages"+" "+cmd
    resp=None
    try:
        resp = subprocess.check_output(cmd)
        resp = resp.decode('utf-8')
        #resp=subprocess.getoutput(cmd)##### direct conversion bytes to string
    except Exception:
        raise Exception("Invlid command")
    resp=resp.split("\n")
    for package in resp:
        if "package:" not in pkg_name:
            pkg_name="package:"+pkg_name
        if package == pkg_name:
            return True
    return False
if __name__=="__main__":
    
    pkg_name="com.veronicaapps.veronica.simplecalculator\r"
    cmd ="-3"
    print(is_package_or_not(pkg_name,cmd))

    
