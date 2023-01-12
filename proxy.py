from urllib3 import ProxyManager, make_headers
import threading
import time

default_headers = make_headers()
f = open("proxy.txt", "r")
url = input("Url : ")
def spam():
    r = http.request('GET', url)

while True:
    try:
        i = f.readline()
        if i == "":
            break
        else:
            http = ProxyManager("http://"+i+"/", proxy_headers=default_headers)
            t1 = threading.Thread(target=spam)
            t1.start()
            print("başarılı proxy:"+i)
    except:
        print("geçersiz proxy")