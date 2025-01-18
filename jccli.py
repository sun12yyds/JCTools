import socket,datetime,time,os

print(os.getcwd())
LogFile=f"KeyLog{datetime.datetime.now().strftime("%Y-%m-%d-%H:%M:%S")}.log"

print(socket.gethostbyname(""))


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

ip=socket.gethostbyname(socket.gethostname())
port=5060

sock.bind(("",port))

while True:
    data,addr=sock.recvfrom(1048576)
    nowtime=datetime.datetime.now().strftime("%Y/%m/%d-%H:%M:%S:%f")
    msg=f"[{nowtime}:FROM{str(addr)} ] == {data.decode("utf-8")}"
    open(LogFile,'a').write(msg+"\n")
    print(msg)