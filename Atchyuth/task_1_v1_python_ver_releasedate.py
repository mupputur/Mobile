#get the data from url python version and release date
import requests,os
from bs4 import BeautifulSoup as bs
def web_pyh_ver(url):
    page=requests.get(url)
    p_text=page.text
    soup=bs(page.content,'html.parser')
    ver=soup.find(id='python-documentation-by-version')
    items=ver.find_all('li')
    ver_rel=[]
    for item in items:
        ver=(item.text.split()[0:2])
        rel=(item.text.split()[5:8])
        full=ver+rel
        str1=""
        for ele in full:
            str1=str1+ele
        ver_rel.append(str1)
    ver_rel=str(ver_rel)
    fobj=open(path,'w')
    pro_file=fobj.write(ver_rel)
    fobj.close()
    gen_files=os.walk('D:\\')
    for root,folders,files in gen_files:
        for file in files:
            if "web_scrapping_pyh_re.txt" in file:
                return True
    else:
        return "File not available"
if __name__=="__main__":
    url='https://www.python.org/doc/versions/'
    path='D:\\Practice_ex\\Practice_real\\web_scrapping_pyh_rel.txt'
    print(web_pyh_ver(url))
        
    











    

