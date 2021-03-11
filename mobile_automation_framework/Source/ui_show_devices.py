#create user interface to click the button to display adb command response
from tkinter import *
from tkinter import messagebox
import subprocess

def show_dev(cmd,button_name):
    window=Tk()
    window.geometry("300x300")
    bytes_res = subprocess.check_output(cmd)
    bytes_to_str_res = bytes_res.decode('utf-8')
    def msg_box():
        msg=messagebox.showinfo( button_name,bytes_to_str_res )
        var=StringVar()
        var.set(bytes_to_str_res)
        res_text = Label( window, textvariable=var, relief=RAISED )
        res_text.place(x=75,y=75)
    show_devices_button= Button(window, text =button_name,command =msg_box )
    show_devices_button.place(x=50,y=25)
    window.mainloop()
    return True
    
if __name__=="__main__":
    cmd='adb devices'
    button_name="show devices"
    show_dev(cmd,button_name)

    
    
    
    



