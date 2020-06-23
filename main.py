# document adinda papqa yaradiriq, icerisinde get request ile cekdiyimiz datani text.txt fayli yaradir
# ve datani ve bu gune olan tarixi icine yazir. Eger artiq bele bir papqa ve fayl varsa onda proqram isledikde onlari silecek

import source
import os
import time


source.creat_del_papqa()
print("Program running...")

time.sleep(2.5)
if (os.path.exists('document')): 
    url = input("URL: ")
    content = source.req(url)
    data = source.data()
    source.creat_file(data, content)
    print("Please, open 'document/text.txt file' ")
else:
    print("Remove document end text.txt file")


