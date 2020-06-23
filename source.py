import os
import requests
import time


def creat_del_papqa():
    if (os.path.exists('document')):     #bele bir path olub olmadigini yoxlayir
        os.remove('document/text.txt')
        os.rmdir('document')             #document adli papaqani silir                 
    else:
        os.mkdir("document")             #document adli papaqa yaratdiq
        
def req(url):
    get_req = requests.get(url)
    if (get_req.status_code == 200):
        content = get_req.text
    return content

def creat_file(*args):
    if (os.path.exists('document')): 
        with open("document/text.txt", 'w+') as file:  #
            for i in args:
                file.write(i) 

def data():
    seconds = time.time()
    local_time = time.ctime(seconds)
    return f'<!-- Time: {local_time} -->\n\n'





