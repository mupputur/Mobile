from tkinter import *
from tkinter import messagebox
import subprocess

def show_devices(cmd):
    top=Tk()
    top.geometry("300x300")
    res = subprocess.check_output(cmd)
    res = res.decode('utf-8')
    def helloCallBack():
        msg=messagebox.showinfo( b_name,res )
        var=StringVar()
        var.set(res)
        label = Label( top, textvariable=var, relief=RAISED )
        label.place(x=75,y=75)
    C = Button(top, text =b_name,command = helloCallBack)
    C.place(x=50,y=25)
    top.mainloop()
    
if __name__=="__main__":
    cmd='adb devices'
    b_name="show devices"
    show_devices(cmd)

    
    
    
    



