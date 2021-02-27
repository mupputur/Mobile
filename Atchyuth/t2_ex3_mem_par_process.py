#get a memory consumption for particular process

import os, psutil
process = psutil.Process(os.getpid())
print(process)
print(process.memory_info().rss)
print(process.memory_info())



