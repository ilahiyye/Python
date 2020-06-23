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
    print("Removed document/text.txt file")


