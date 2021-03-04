# find the given package available or not.

import subprocess
import os

def package_avail_not(cmd,pkg_name):
    resp=None
    try:
        resp = subprocess.check_output(cmd)
        resp = resp.decode('utf-8')
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
    
    path="package:com.veronicaapps.veronica.simplecalculator\r"
    cmd ="adb shell pm list packages -3"
    print(package_avail_not(cmd,path))

    
