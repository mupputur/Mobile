#Create one user interface dropdown and give option to the user for command selection
#and display the packages to related that command.

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import subprocess

def ui_show_command_packages():
    root=Tk()
    root.title("TAB-2")
    root.geometry("400x400")
    Label(root,text="Select Command: ",background="black",foreground="white",
              font=("Times new Roman",15)).grid(row=0,column=1,padx = 10, pady = 10)
    cmdvariable=StringVar()
    commandchoosen = ttk.Combobox(root, width = 25, textvariable=cmdvariable)
    commandchoosen['values'] = ["adb shell pm list packages -f",
    "adb shell pm list packages -d",
    "adb shell pm list packages -e",
    "adb shell pm list packages -s",
    "adb shell pm list packages -3",
    "adb shell pm list packages -i",
    "adb shell pm list packages -u"]
    commandchoosen.grid(column=2, row=0) 
    def show_packages():
        cmd=commandchoosen.get()
        resp = subprocess.check_output(cmd)
        resp = resp.decode('utf-8')
        messagebox.showinfo("show packages",resp)
    button = Button(root, text="OK", command=show_packages,
            height=2,width=10).grid(row =3,column=2)
    root.mainloop()
if __name__=="__main__":
    ui_show_command_packages()
