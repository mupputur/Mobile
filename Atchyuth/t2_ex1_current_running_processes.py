#List all currently running processes
import psutil
c=0
for process in psutil.process_iter():
    c=c+1
    name=process.name()
    Id=process.pid
    print(Id,name)
print("total processes : ",c)
