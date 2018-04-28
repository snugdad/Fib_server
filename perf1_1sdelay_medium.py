# perf1.py
# Time of a long running request

from socket import *
import time

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))

while True:
    time.sleep(1)
    start = time.time()
    sock.send(b'35')
    resp = sock.recv(100)
    end = time.time()
    print(format(end - start, '.2f') + ' sec')