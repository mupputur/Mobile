#copy a file device to computer by using adb commands
import os
import subprocess
def copy_a_file_device_to_computer(cmd_list):
      try:
            proc = subprocess.check_output(cmd).decode('utf-8')
      except Exception as e:
            print("Error :{}".format(str(e)))
      raise Exception("check source path and destination path")
      return proc
if __name__=="__main__":
      cmd='adb pull /sdcard/IMG_5778.JPG Desktop'
      print(copy_a_file_device_to_computer(cmd))


