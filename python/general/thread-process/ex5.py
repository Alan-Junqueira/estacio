import threading
import urllib.request
import time

start = time.time()
urls = ["http://google.com", "http://apple.com",
        "http://microsoft.com", "http://instagram.com"]


def call_url(url):
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    the_page = response.read()
    print("'%s\' carregado em %ss" % (url, (time.time() - start)))
    # print(the_page)


threads = [threading.Thread(target=call_url, args=(url,)) for url in urls]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()

print("Elapsed time: %s" % (time.time() - start))
