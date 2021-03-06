import Queue
import threading
import os
import urllib.request

threads = 10
target = "http://www.safeca.net"
dirctory = ""
filters = [".jpg",".gif",".png",".css"]
os.chdir(dirctory)
web_paths = Queue.Queue()

for r,d,f in os.walk(".."):
    for files in f:
        remote_path = "%s%s"%(r,files)
        if remote_path.startswith("."):
            remote_path = remote_path[1:]
            if os.path.splitext(files)[1] not in filters:
                web_paths.puts(remote_path)
def test_remote():
    while not web_paths.empty():
        path = web_paths.ger()
        url = "%s%s"%(target,path)

        request = urllib.request.Request(url)
        try:
            response = urllib.request.urlopen(request)
            content = response.read()
            print("[%d]=>%s"%(response.code,path))
            response.close()
        except urllib.request.HTTPErrorProcessor as error:
            print("Failed %s"%error.code)
            pass

for i in range(threads):
    print("Spawning thread :%d"%i)
    t = threading.Thread(target=test_remote)
    t.start()