#Create one user interface dropdown and give option to the user for command selection
#and display the packages to related that command.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess
import os

def ui_show_command_packages():
    root=Tk()
    root.title("TAB-2")
    root.geometry("400x400")
    Label(root,text="Select Command: ",background="black",foreground="white",
              font=("Times new Roman",15)).grid(row=0,column=1,padx = 10, pady = 25)
    n =StringVar()
    monthchoosen = ttk.Combobox(root, width = 25, textvariable=n)
    monthchoosen['values'] = ["adb shell pm list packages -f",
    "adb shell pm list packages -d",
    "adb shell pm list packages -e",
    "adb shell pm list packages -s",
    "adb shell pm list packages -3",
    "adb shell pm list packages -i",
    "adb shell pm list packages -u","adb devices"]
    monthchoosen.grid(column = 2, row = 0) 
    e1=monthchoosen
    def show_packages():
        cmd=e1.get()
        resp = subprocess.check_output(cmd)
        resp = resp.decode('utf-8')
        messagebox.showinfo("show packages",resp)
    button = Button(root, text="OK", command=show_packages,
            height=2,width=10).place(x=10,y=100)
    root.mainloop()
if __name__=="__main__":
    ui_show_device_packages()
