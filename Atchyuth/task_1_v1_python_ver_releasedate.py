#get the data from url python version and release date
import requests
from bs4 import BeautifulSoup as bs
page=requests.get('https://www.python.org/doc/versions/')
p_text=page.text
#print(p_text)
soup=bs(page.content,'html.parser')
ver=soup.find(id='python-documentation-by-version')
items=ver.find_all('li')
ver_rel=[]
"""
ver=(items[0].text.split()[0:2])
rel=(items[0].text.split()[5:8])
full=ver+rel
print(full)
str1=''
for ele in full:
    str1+=ele
#print(str1)
"""
for item in items:
    ver=(item.text.split()[0:2])
    rel=(item.text.split()[5:8])
    full=ver+rel
    #print(full)
    str1=''
    for ele in full:
        str1=str1+ele
    #print(str1)
    
    ver_rel.append(str1)
print(ver_rel)
        
    











    

